import requests
import pdfkit
# Replace 'YOUR_API_KEY' with your Stack Overflow API key
API_KEY = 'EFTu48nd)ulszUXg4YMOEA(('

# Stack Overflow API endpoints
BASE_URL = f'https://stackoverflow.microsoft.com/api/2.2/questions'

# Specify the tags you are interested in
tags = ['objectstore']

# Construct the URL for fetching questions
questionsAnswers = []
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files (x86)/wkhtmltopdf/bin/wkhtmltopdf.exe")

def fetchQuestionsAnswers():
    page=0
    hasMoreResults=True
    
    while(hasMoreResults):
        page+=1
        params = {
        'order': 'desc',
        'sort': 'activity',
        'tagged': ';'.join(tags),
        'filter': 'withbody',  # Include question body
        'key': API_KEY,
        'pagesize': '100',
        'page': page
        }
        response =  requests.get(BASE_URL,params)
        question_title_id={}
        id_string=""
        if response.status_code == 200:
            data = response.json()
            # Check if there are more results to be fetched 
            if(data['has_more']!=True):
                hasMoreResults=False
            # Batch the requests upto max ids which is 100 to fetch answers for 100 questions in a single call
            # Get all the ids of question & separate thm by ; 
            count=0
            for question in data['items']:
                count+=1
                if(count==1):
                    id_string+=str(question['question_id'])
                else:
                    id_string=id_string +";" + str(question['question_id'])
                question_title_id[question['question_id']]=(question['title'], question['body'])
            # Make a single call to fetch the answers   
            # Fetch all answers for the question
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'filter': 'withbody',  # Include answer body
                'key': API_KEY,
                'pagesize': '100'
            }
            response = requests.get(BASE_URL + f'/{id_string}/answers', params=params)
            if response.status_code == 200:
                try:
                    answers=response.json()
                    for answer in answers['items']:
                        item = {"title": "", "body": "", "id": "", "answer": ""}
                        item['answer'] = answer['body']
                        item['title'] = question_title_id[answer['question_id']][0]
                        item['body'] = question_title_id[answer['question_id']][1]
                        item['id'] = answer['question_id']
                        questionsAnswers.append(item)
                except:
                        print("No answer found")
                else:
                    print("No answer found")
        else:
            print("Failed to fetch questions")

def buildPDF(fileName):
    html='<html><body style="font-family: Arial;">'
    for entry in questionsAnswers:
        html+=f'<h2>{entry["title"]}</h2>'
        html+=f'<p>{entry["body"]}</p>'
        html+='<h3>Answer</h3>'
        html+=f'<p>{entry["answer"]}</p>'
    html+='</body></html>'
    pdfkit.from_string(html, fileName, configuration=config,options={"enable-local-file-access": ""})

fetchQuestionsAnswers()
fileName = "questions_and_answers.pdf"
buildPDF(fileName)

