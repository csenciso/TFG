#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Literals:

    def __init__(self, session, user_name):
        self.session = session
        self.user_name = user_name

    def get_backend_error(self):
        message = {
            "session": self.session,
            "answer": [{
                "intent": "backend_error",
                "response": "Actualmente nuestros servicios no estan disponibles, para resolver su consulta "
                            "llame al 912 345 678. Disculpe las molestias.",
                "next": ""
            }],
            "options": {}
        }
        return message

    def get_token_error(self):
        message = {
            "session": self.session,
            "answer": [{
                "intent": "backend_error",
                "response": "La sesión ha expirado, para realizar otra consulta ponte en contacto en el 912 345 678",
                "next": ""
            }],
            "options": {}
        }
        return message

    def get_finish(self):
        message = {
            "session": self.session,
            "answer": [{
                "intent": "finish",
                "response": "Gracias por tu petición, para otra consulta llame al 912 345 678.",
                "next": ""
            }],
            "options": {}
        }
        return message
