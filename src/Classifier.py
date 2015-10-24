__author__ = 'Hayden'
__name__ = "Classifier"

import nltk;

# response categories
RESPONSE_CATEGORIES = ["NAMED ENTITY", "LIST", "THING", "EXPLANATION"]

# this is a dictionary
RESPONSE_SUBCATEGORIES = {'NAMED ENTITY': ["PERSON", "LOCATION", "TIME"]}

class Classifier:
    def __init__(self, sentence):
       self.sentence = sentence









