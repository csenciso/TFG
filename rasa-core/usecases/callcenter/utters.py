#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Utters:

    def __init__(self):
        # ID 1
        self.utter_greet_action = [
            "Hola, soy Luca, el Asistente Virtual del hospital y voy a necesitar ciertos datos suyos para poder "
            "empezar. Lo primero, necesitaría saber el número de su carnet de identidad. "
        ]

        # ID 2
        self.ask_name = [
            "¿Podría facilitarme su nombre y sus apellidos?"
        ]

        # ID 3
        self.ask_date_of_birth = [
            "Hola {user_name}. A continuación, dígame el día, el mes y el año de su nacimiento, por favor"
        ]

        # ID 4
        self.ask_site = [
            "Ahora voy a necesitar que sea preciso para poder prestarle el mejor servicio posible. ¿Qué y dónde "
            "le duele exactamente?"
        ]

        # ID 5
        self.ask_character = [
            "De qué características tiene el dolor? ¿Es un dolor agudo? ¿Es un dolor tenso? ¿Es un dolor ardiente?"
        ]

        # ID 6
        self.ask_location = [
            "¿Es un dolor localizado en un punto?"
        ]

        # ID 7
        self.ask_radiation = [
            "¿Hacia qué zona del cuerpo se propaga?"
        ]

        # ID 8
        self.ask_associated_symptoms = [
            "¿Tiene otros síntomas asociados como vómitos, sudores o mareos? Por favor, si es así sea preciso con los "
            "detalles. "
        ]

        # ID 9
        self.ask_night_pain = [
            "¿Se despierta usted por el dolor?"
        ]

        # ID 10
        self.ask_exacerbating_relieving_factor = [
            "¿Hay algo que lo haga mejorar o empeorar? Por ejemplo, le duele al hacer algun gesto o movimiento en "
            "particular, le duele al presionar o si ha tomado alguna tipo de medicamento para aliviarlo "
        ]

        # ID 11
        self.ask_severity = [
            "En una escala del uno al diez, califique el dolor con un solo numero."
        ]

        # ID 12
        self.ask_allergy = [
            "Gracias {user_name}, ahora voy a preguntarle sobre sus antecedentes tanto personales como familiares y"
            " como ha estado haciendo hasta ahora, le ruego precisión. ¿Es usted alérgico a algún medicamento? "
        ]

        # ID 13
        self.ask_illness = [
            "¿Padece usted de algún otro tipo de enfermedad que no haya mencionado?"
            "¿Hay alguna tipo de enfermedad genética en su familia?"
        ]

        # ID 14
        self.ask_medication = [
            "¿Toma usted alguna tipo de medicamento de manera regular o incluso esporádicamente?"
        ]

        # ID 15
        self.ask_cardio = [
            "¿Padece de alguna tipo de cardiopatía? Si es así, indíquemelo por favor."
        ]

        # ID 16
        self.ask_neoplasm = [
            "¿Padece de alguna neoplasia? ¿Algún tipo de tumor tanto benigno como maligno?"
            "de indicarlo "
        ]

        # ID 17
        self.ask_transfusion = [
            "¿Ha necesitado usted alguna transfusion?"
        ]


        # ID 18
        self.ask_toxic_habits = [
            "¿Practica usted alguna hábito tóxico? En esta pregunta se consideran relevantes el alcohol y el tabaco. "
            "Si es así, indique cual."
        ]


        # ID 19
        self.goodbye = [
            "Muchas gracias por la información dada, se le hará llegar al médico que en breves instantes le atenderá. "
            "¡Espero que tenga una rápida recuperación! "
        ]

        # ID 20
        self.utter_handover = [
            "En breves momentos le atenderá un médico. ¡Espero que tenga una rápida recuperación! "
        ]