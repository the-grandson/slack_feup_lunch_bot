# *****************************************************************************************
# *    Copyright 2024 by the_grandson and Google Gemini.                                  *
# *    You may use, edit, run or distribute this file                                     *
# *    as long as the above copyright notice remains                                      *
# * THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED           *
# * OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF                    *
# * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.          *
# * the_grandson and Google Gemini SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL,*
# * INCIDENTAL, OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.                      *
# * For more information visit: https://digi2.fe.up.pt                                    *
# *****************************************************************************************

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import fetch_lunch
from prettytable import PrettyTable
import json

from dotenv import load_dotenv

load_dotenv()

SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_app_mention_events(body, say, logger):
    logger.info(body)
    tables = fetch_lunch.check_table_dates("https://sigarra.up.pt/feup/pt/cantina.ementashow")
    if len(tables) <= 0:
        say("No lunch today... \_('',)_/")
    else:
        for table in tables:
            say("```\n" + table + "```\n")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
    