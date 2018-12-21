from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rest import HttpInputChannel, HttpInputComponent
import logging
import sys

#Reinicio el sistema para que funcione con utf8 y no con ASCII para evitar problemas de formatos
reload(sys)
sys.setdefaultencoding('utf8')

def run(serve_forever = True):

    agent = Agent.load("usecases/callcenter/models/policy/init",
                       interpreter = RegexInterpreter())

    if serve_forever:
        logging.warn("Cognitive Callcenter chatbot has been initialized")
        agent.handle_channel(HttpInputChannel(5002, '/', HttpInputComponent()))
    return agent


if __name__ == '__main__':
    logging.basicConfig(level = "DEBUG", format='%(levelname)s - %(message)s') #Options: "DEBUG" for information about intent and entities
    logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
    run()
