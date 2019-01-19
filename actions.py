# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

import requests
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


class FallbackAction(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "fallback_action"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        dispatcher.utter_message("Sorry, I don't understand you")  # send the message back to the user
        return []
