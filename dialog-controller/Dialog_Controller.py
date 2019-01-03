#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import sys
from datetime import datetime
from flask import request, Flask

from util import Logger
from Literals import Literals
from luis.LUISController import get_answer_luis
from rasa.RASAController import get_answer_rasa
from context_handler.RedisContextHandler import RedisContextHandler
from util.response_utils import make_error_response, make_response

reload(sys)
sys.setdefaultencoding('utf8')


app = Flask(__name__)

yes_no_intents = [
    "evaluate_name",
    "evaluate_character",
    "evaluate_associated_symptoms"
]


@app.route('/api/login', methods=['POST'])
def login():
    try:
        content = request.json
        if content:
            # Recoger la sesion del contenido
            session = content['session']

            intent = "greet"
            entities = []

            # Coge la respuesta de RASA
            answer = get_answer_rasa(session, intent, entities)

            Logger.log("\nRASA dice " + str(answer) + "\n\n")

            # Guardo la conversacion en REDIs para tener un registro
            save_conversation(content, answer)

            response = generate_answer(answer, intent, session)

            time_2 = datetime.now()
            Logger.log("Sale de GetAnswer: " + str(time_2) + "\n\n")

            return make_response(response, 200)

        else:
            return make_error_response(400)

    except Exception as e:
        Logger.log(e)
        traceback.print_exc()

        return make_error_response(500)


@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    try:
        content = request.json
        if content:
            # Recoger la sesion del contenido
            session = content['session']

            previous_intent = str(intent_redis_context_handler.get_field(session))
            user_name = str(username_redis_context_handler.get_field(session))

            literal = Literals(session, user_name)

            # CONTROL DE ERRORES
            if previous_intent == "finish":
                response = literal.get_finish()

            # 403 error o fallo de conexion o datos
            elif previous_intent == "backend_error":
                response = literal.get_backend_error()

            # 501 error de autenticacion
            elif previous_intent == "token_error":
                response = literal.get_token_error()

            else:
                # Recoge los datos de LUIS
                intent, entities = call_natural_language_service(content, previous_intent)

                for entity in entities:
                    Logger.log(entity)
                    if entity['type'] == "user_name":
                        username_redis_context_handler.save_field(entity['entity'], session)

                    if 'date' in entity['type'] and previous_intent in yes_no_intents:
                        entity['type'] = "date"

                # Coge la respuesta de RASA
                answer = get_answer_rasa(session, intent, entities)

                Logger.log("\nRASA dice " + str(answer) + "\n\n")

                # Guardo la conversacion en REDIs para tener un registro
                save_conversation(content, answer)

                response = generate_answer(answer, intent, session, literal=literal)

            time_2 = datetime.now()
            Logger.log("Sale de GetAnswer: " + str(time_2) + "\n\n")

            return make_response(response, 200)

        else:
            return make_error_response(400)

    except Exception as e:
        Logger.log(e)
        traceback.print_exc()

        return make_error_response(500)


def call_natural_language_service(content, previous_intent):
    question = content['query']
    question = question.encode('utf-8')

    Logger.log("Previous Intent: " + previous_intent)

    # Llamo a Microsoft LUIS
    if previous_intent in yes_no_intents:
        intent, entities = get_answer_luis(question, template="yes_no")

    else:
        intent, entities = get_answer_luis(question)

        if previous_intent == "evaluate_radiation":
            previous_intent = "evaluate_associated_symptoms"

        if intent == "deny":
            intent = previous_intent + "_no"

    return intent, entities


def generate_answer(answer, intent_name, session, literal=None):

    if intent_name == "backend_error":
        final_answer = literal.get_backend_error()

    elif intent_name == "token_error":
        final_answer = literal.get_token_error()

    else:
        final_answer = {
            "session": session,
            "answer": answer['answer'],
            "options": {}
        }

    if answer['answer']['next_intent'] == "evaluate_associated_symptoms":
        intent_name = "evaluate_radiation"

    elif answer['answer']['next_intent'] == "evaluate_exacerbating_relieving_factor":
        intent_name = "evaluate_exacerbating_relieving_factor"

    else:
        intent_name = intent_name.replace('_no', '')

    intent_redis_context_handler.save_field(intent_name, session)

    return final_answer


def save_conversation(content, answer):
    session = content['session']
    question = content['query']
    question = question.encode('utf-8')

    user_query = "//:user: " + question
    chatbot_response = "//:virtual_assistant:"

    chatbot_response = chatbot_response + " " + answer['answer']['response']

    conversation = user_query + chatbot_response
    conversation_formatted = conversation.replace('\n', ' ')

    prev_conversation = conversation_redis_context_handler.get_field(session)

    if prev_conversation is None:
        conversation_redis_context_handler.save_field(conversation_formatted, session)

    else:
        conversation_redis_context_handler.save_field(prev_conversation + " " + conversation_formatted, session)


if __name__ == "__main__":
    Logger.log('Running app with rules: ' + str(app.url_map), )

    conversation_redis_context_handler = RedisContextHandler("conversationInfo")
    intent_redis_context_handler = RedisContextHandler("intent")
    username_redis_context_handler = RedisContextHandler("userName")

    app.run(debug=True, host='0.0.0.0', port=8080)
