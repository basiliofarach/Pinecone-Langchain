import logging
import os
import azure.functions as func
from text_indexer import TextIndexer

app = func.FunctionApp()

@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    TextIndexer(os.environ.get("PINECONE_INDEX_NAME"), "./FixBlueScreen.txt").index()

    logging.info('Python timer trigger function executed.')