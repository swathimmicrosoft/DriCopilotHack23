import datetime
import logging
import azure.functions as func      
 
# now we can import mod
from DriCopilotHack23.scripts import mdtopdf, stackoverflow

app = func.FunctionApp()

@app.schedule(schedule="0 10 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def CopilotTimerTrigger(myTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    mdtopdf.main()
    stackoverflow.main()

    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)