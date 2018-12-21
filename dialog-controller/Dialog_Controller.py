#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import sys
from datetime import datetime
from flask import request, Flask

from util import Logger
from Literals import Literals
from src.luis.LUISController import get_answer_luis
from src.rasa.RASAController import get_answer_rasa
from src.context_handler.RedisContextHandler import RedisContextHandler
from util.response_utils import make_error_response, make_response


reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)



@app.route('/api/login', methods=['POST'])
def login():
    try:
        content = request.json
        if content:
            time_1 = datetime.now()
            Logger.log("Entra en Login: " + str(time_1) + "\n\n")

            # Recoger la sesion del contenido
            session = content['session']
            intent_redis_context_handler.save_field("greet", session)

            # Coge la respuesta de RASA
            answer = get_answer_rasa(session, "greet", [])

            Logger.log("\nRASA dice " + str(answer) + "\n\n")

            # Guardo la conversacion en REDIs para tener un registro
            save_conversation(content, answer)

            response = generate_answer(answer, "greet", session)

            time_2 = datetime.now()
            Logger.log("Sale de Login: " + str(time_2) + "\n\n")

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
            time_1 = datetime.now()
            Logger.log("Entra en GetAnswer: " + str(time_1) + "\n\n")

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
                intent, entities = call_natural_language_service(content, previous_intent)

                if entities['type'] == "user_name":
                    username_redis_context_handler.save_field(entities['entity'], session)

                # Coge la respuesta de RASA
                answer = get_answer_rasa(session, intent, entities)

                Logger.log("\nRASA dice " + str(answer) + "\n\n")

                # Guardo la conversacion en REDIs para tener un registro
                save_conversation(content, answer)

                response = generate_answer(answer, intent, session, literal)

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

    # Llamo a LUIS
    intent, entities = get_answer_luis(question)

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

    intent_name = intent_name.replace('_no', '')

    intent_redis_context_handler.save_field(intent_name, session)

    return final_answer


def save_conversation(content, answer):
    session = content['session']
    question = content['query']
    question = question.encode('utf-8')

    user_query = "//:user: " + question
    chatbot_response = "//:virtual_assistant:"

    for response in answer['answer']:
        chatbot_response = chatbot_response + " " + response['response']['transcript']

    conversation = user_query + chatbot_response
    conversation_formatted = conversation.replace('\n', ' ')

    prev_conversation = str(conversation_redis_context_handler.get_field(session))

    conversation_redis_context_handler.save_field(prev_conversation + " " + conversation_formatted, session)


if __name__ == "__main__":
    Logger.log('Running app with rules: ' + str(app.url_map), )

    conversation_redis_context_handler = RedisContextHandler("conversationInfo")
    intent_redis_context_handler = RedisContextHandler("intent")
    username_redis_context_handler = RedisContextHandler("userName")

    # app.run(debug=True, port=int(config.get('AICONTROLLER', 'PORT')))
    app.run(debug=True, host='0.0.0.0', port=8080)
