#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from random import randint

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction
from rasa_core.actions.forms import EntityFormField
from utters import Utters

import json
import logging

answers = Utters()
MOCK = False


def pickutter(utter_arr):
    rand = randint(0, len(utter_arr) - 1)

    return str(utter_arr[rand])


def replace_u(text, a, b):
    return text.replace(a, b)


def build_answer(session, intent, question, next_intent=""):
    answer = {
        "answer":
            {
                "intent": intent,
                "next_intent": next_intent,
                "response": question,
            }
    }

    return json.dumps(answer)


class GreetAction(Action):
    ACTION_NAME = "utter_greet_action"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)
        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_identification_number"
        message = pickutter(answers.utter_greet_action)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateIdentificationNumberAction(FormAction):
    RANDOMIZE = False
    ACTION_NAME = "ask_name"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    @staticmethod
    def required_fields():
        """
            Function that includes in the returns all the fields that are required in this action.
        """

        return [EntityFormField("identification_number", "identification_number")]

    def submit(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Save the Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_name"

        # Save in a variable the utterance that it is going to be send of the utters.py file.
        message = pickutter(answers.ask_name)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)
        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateNameAction(FormAction):
    RANDOMIZE = False
    ACTION_NAME = "ask_date_of_birth"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    @staticmethod
    def required_fields():
        """
            Function that includes in the returns all the fields that are required in this action.
        """

        return [EntityFormField("user_name", "user_name")]

    def submit(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")
        user_name = tracker.get_slot("user_name")

        # Save the Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_date_of_birth"


        # Save in a variable the utterance that it is going to be send of the utters.py file.
        message = pickutter(answers.ask_date_of_birth)

        message_completed = message.replace("{user_name}", user_name)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message_completed, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateDateOfBirthAction(FormAction):
    RANDOMIZE = False
    ACTION_NAME = "ask_site"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    @staticmethod
    def required_fields():
        """
            Function that includes in the returns all the fields that are required in this action.
        """

        return [EntityFormField("date", "date")]

    def submit(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")
        user_name = tracker.get_slot("user_name")
        # Save the Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_site"

        message = pickutter(answers.ask_site)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateSiteAction(Action):
    ACTION_NAME = "ask_character"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_character"

        message = pickutter(answers.ask_character)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateCharacterAction(Action):
    ACTION_NAME = "ask_radiation"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_radiation"

        message = pickutter(answers.ask_radiation)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateRadiationAction(Action):
    ACTION_NAME = "ask_location"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = tracker.latest_message.intent.get("name")

        message = pickutter(answers.ask_location)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateLocationAction(Action):
    ACTION_NAME = "ask_associated_symptoms"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_associated_symptoms"

        message = pickutter(answers.ask_associated_symptoms)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateAssociatedSymptomsAction(Action):
    ACTION_NAME = "ask_night_pain"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = tracker.latest_message.intent.get("name")

        message = pickutter(answers.ask_night_pain)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateSleepAction(Action):
    ACTION_NAME = "ask_exacerbating_relieving_factor"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_exacerbating_relieving_factor"

        message = pickutter(answers.ask_exacerbating_relieving_factor)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateFactorsAction(Action):
    ACTION_NAME = "ask_severity"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_severity"

        message = pickutter(answers.ask_severity)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateSeverityAction(Action):
    ACTION_NAME = "ask_allergy"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")
        user_name = tracker.get_slot("user_name")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_allergy"

        message = pickutter(answers.ask_allergy)
        message_completed = message.replace("{user_name}", user_name)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message_completed, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateAllergyAction(Action):
    ACTION_NAME = "ask_medication"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_medication"

        message = pickutter(answers.ask_medication)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateMedicationAction(Action):
    ACTION_NAME = "ask_cardio"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_cardio"

        message = pickutter(answers.ask_cardio)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateCardioAction(Action):
    ACTION_NAME = "ask_neoplasm"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_neoplasm"

        message = pickutter(answers.ask_neoplasm)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateNeoplasmAction(Action):
    ACTION_NAME = "ask_illness"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_illness"

        message = pickutter(answers.ask_illness)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateIllnessAction(Action):
    ACTION_NAME = "ask_toxic_habits"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")
        next_intent = "evaluate_toxic_habits"

        message = pickutter(answers.ask_toxic_habits)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message, next_intent=next_intent)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class EvaluateToxiHabitAction(Action):
    ACTION_NAME = "goodbye"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")

        message = pickutter(answers.goodbye)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""


class HandOver(Action):
    ACTION_NAME = "utter_handover"

    def name(self):
        """
            Function that it is used when in the stories.py file an action is called. The returned value has to be
            exactly the same as the value of the story.
        """

        return self.ACTION_NAME

    def run(self, dispatcher, tracker, domain):
        """
            Function that executes the actions if a specific intent has been recognized and the required entities are
            collected.

                :param tracker: User state tracker.
                :param dispatcher: Communication channel.
                :param domain: Bots custom domain.

                :return: Reset all the Slots that have been saved in the story.
        """

        logging.info("Executing action: " + self.ACTION_NAME)

        # Get Slot Information & Save into a new variable
        session = tracker.get_slot("session")

        # Get Intent Name that it has been recognized & Save into a new variable.
        intent = tracker.latest_message.intent.get("name")

        message = pickutter(answers.utter_handover)

        # Build the answer that it has to be sent.
        answer = build_answer(session, intent, message)

        # Send back the built answer.
        dispatcher.utter_message(answer)

        return ""
