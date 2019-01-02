#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime

from util import Logger


def get_answer_rasa(session, intent, entities):
    time_1 = datetime.now()
    Logger.log("Entra en RASA DialogManager: " + str(time_1) + "\n\n")

    payload = {
        "session": session,
        "intent": str(intent),
        "entities": entities
    }

    headers = {
        'content-type': "application/json"
    }
    url = "http://127.0.0.1:5002/"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    response.raise_for_status()

    answer_dm = json.loads(response.text)

    time_2 = datetime.now()
    Logger.log("\n\nSale de RASA DialogManager: " + str(time_2))

    return answer_dm
