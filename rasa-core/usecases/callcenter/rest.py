# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Callable, Optional, Text

from rasa_core.channels.channel import InputChannel
from rasa_core.channels.channel import UserMessage
from flask import Blueprint, request, jsonify
import traceback
import json
import logging


class HttpInputChannel(InputChannel):
    """An input channel that collects messages from an HTTP endpoint.

    There is no actual API definition of the HTTP endpoint here. Instead, the
    channel expects `listener_components` to be passed in. These components
    define API endpoints, e.g. there can be a rasa REST endpoint, a facebook
    REST endpoint and so on. This channel will then start a HTTP server for
    accepting the incoming HTTP requests and redirecting them to the appropriate
    listener components."""

    def __init__(self, http_port, url_prefix, *listener_components):
        # type: (int, Optional[Text], *HttpInputComponent) -> None
        self.listener_components = listener_components
        self.http_port = http_port
        self.url_prefix = url_prefix

    def start_async_listening(self, message_queue):
        # type: (Dequeue) -> None
        """Start to push the incoming messages from channel into the queue."""
        self._record_messages(message_queue.enqueue)

    def start_sync_listening(self, message_handler):
        # type: (Callable[[UserMessage], None]) -> None
        """Should call the message handler for every incoming message."""
        self._record_messages(message_handler)

    def _has_root_prefix(self):
        # type: () -> bool
        """Check if the stored url prefix corresponds to the root of an url."""
        return (not self.url_prefix or
                self.url_prefix == "" or
                self.url_prefix == "/")

    def _record_messages(self, on_message):
        # type: (Callable[[UserMessage], None]) -> None
        from flask import Flask

        app = Flask(__name__)
        for component in self.listener_components:
            if self._has_root_prefix():
                app.register_blueprint(component.blueprint(on_message))
            else:
                app.register_blueprint(component.blueprint(on_message),
                                       url_prefix=self.url_prefix)

        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer(('0.0.0.0', self.http_port), app)
        http_server.serve_forever()


def process_res(res, session):
    session_entity = {
        "type": "session",
        "entity": session
    }
    res["entities"].append(session_entity)

    answer = "/" + res["intent"].lower()
    if "greet" not in res["intent"]:
        if res["entities"]:
            print("entities: ", res["entities"])
            answer = answer + "{"
            for i in range(len(res["entities"])):
                if i is not 0:
                    answer += ", "
                val = res["entities"][i]["entity"]
                try:
                    answer += "\"" + res["entities"][i]["type"].lower() + "\" : \"" + str(val) + "\""
                except:
                    answer += "\"" + res["entities"][i]["type"].lower() + "\" : \"" + val + "\""
            answer += "}"
    else:
        answer = "/greet{\"session\":\"" + session + "\"}"
    return answer


class HttpInputComponent(object):
    def blueprint(self, on_new_message):
        # type: (Callable[[UserMessage], None])-> None
        """Defines a Flask blueprint.

        The blueprint will be attached to a running flask server and handel
        incoming routes it registered for."""

        rasa_webhook = Blueprint('rasa_webhook', __name__)

        @rasa_webhook.route("/", methods=['GET', 'POST'])
        def hello():
            session = "UNDEFINED"

            try:
                content = request.json
                session = content["session"]

                text = process_res(content, session)
                print("text is: ", text)

                answer = on_new_message(UserMessage(str(text), None, session))
                print("answer is: ", answer)
                print(answer)
                if answer:
                    answer = answer[0]["text"]
                    try:
                        answer = json.loads(answer)
                        answer["answer"]["session"] = session

                    except:
                        if type(answer) != dict:
                            answer = {
                                "session": session,
                                "answer":
                                    {
                                        "intent": "",
                                        "next": "",
                                        "response": answer
                                    }
                            }
                            answer = json.loads(json.dumps(answer))
                        else:
                            answer = {
                                "session": session,
                                "answer": [
                                    {
                                        "intent": answer['answer'][0]['intent'],
                                        "next": answer['answer'][0]['next'],
                                        "response": answer['answer'][0]['response']
                                    }
                                ]
                            }
                            answer = json.loads(json.dumps(answer))
                        print(type(answer))
                        print(answer)

                    # logger.info(session, json.dumps(answer) + "\n\n")
                    answer = jsonify(answer)
                    return answer
                else:
                    raise ValueError('BLANK RESPONSE FROM RASA!')
            except ValueError as e:
                logging.error(e)

                content = {
                    "session": session,
                    "answer": {
                        "intent": "None",
                        "next": "",
                        "response": "Disculpa, no le he entendido. ¿Podría volver a repetir?",
                    }
                }

                return jsonify(content)
            except Exception as e:
                logging.error(e)

                logging.debug("\n" + traceback.format_exc())
                answer_exception = ["Internal server error"]

                content = {
                    "session": session,
                    "answer": {
                        "intent": "None",
                        "next": "ask",
                        "response": answer_exception,
                    }
                }
                return jsonify(content)

        return rasa_webhook

        raise NotImplementedError(
            "Component listener needs to provide blueprint.")
