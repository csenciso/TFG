#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import json

from util import Logger


def _get_standard_answer_luis(user_query, url):
    json_response = requests.request("GET", url + "&timezoneOffset=60&q=" + user_query)

    Logger.log(json_response.text)

    answer_json = json.loads(json_response.text)
    Logger.log(answer_json)

    answer_json["intent"] = answer_json["topScoringIntent"]["intent"]
    answer_json["score"] = answer_json["topScoringIntent"]["score"]

    del answer_json["topScoringIntent"]

    i = 0

    for entity in answer_json["entities"]:

        answer_json["entities"][i]["value"] = entity["entity"]

        del answer_json["entities"][i]["startIndex"]

        del answer_json["entities"][i]["endIndex"]

        if "resolution" in answer_json["entities"][i]:
            del answer_json["entities"][i]["resolution"]

        del answer_json["entities"][i]["entity"]

        i += 1

    del answer_json["query"]

    Logger.log(answer_json)

    return answer_json


def get_answer_luis(question):
    try:
        time_1 = datetime.now()
        Logger.log("\n\nEntra en NLU: " + str(time_1))

        Logger.log(question)

        url = "https://westeurope.api.cognitive.microsoft.com/luis/v2.0/apps/96683db4-08ff-48ed-abdf-d631c05e8b0c/"

        query_answer = _get_standard_answer_luis(question, url + "?subscription-key=82168a5b9f74402ca8e5e4eba77adb0e")

        intent = query_answer['intent']
        entities = query_answer['entities']

        time_6 = datetime.now()
        Logger.log("Envia respuesta NLU: " + str(time_6) + "\n\n")

        return intent, entities

    except Exception as exc:
        Logger.error(exc)
        return "ERROR: Llamada a API NLU"
