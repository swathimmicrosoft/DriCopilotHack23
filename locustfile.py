import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [{"user": random.choice(["What is the deadline for Bring your own KV in Falcon", "What is clusterfleet and falconfleet", "Why choose clusterfleet over AKS", "How to onboard to clusterfleet?"])}],
                "approach": "rrr",
                "overrides": {"retrieval_mode": "hybrid", "semantic_ranker": True, "semantic_captions": False, "top": 3, "suggest_followup_questions": True},
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "user": "What is the deadline for bring your own kv in falcon",
                        "bot": "Deadline enforce by falcon to deprecated shared key vault is 30th september 2023.",
                    },
                    {"user": "Does my plan cover eye exams?"},
                ],
                "approach": "rrr",
                "overrides": {"retrieval_mode": "hybrid", "semantic_ranker": True, "semantic_captions": False, "top": 3, "suggest_followup_questions": False},
            },
        )
