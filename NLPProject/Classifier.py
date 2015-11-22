__author__ = 'Hayden'
__name__ = "QuestionType"

import string
import re
from textblob import TextBlob
from nltk.corpus import wordnet as wn



tokens = []

familyReferences = ['wife', 'husband', 'father', 'mother', 'grandmother', 'grandfather',
                    'uncle', 'aunt', 'sister', 'brother', 'married', 'spouse', 'cousin',
                    'relative', 'boyfriend', 'girlfriend', 'sibling'];


class Classifier:
    # ************MEMBER VARIABLES *************************


    # these variables will hold the top two response categories
    category1 = "OTHER"
    subcategory1 = "UNKNOWN"
    category1Prob = 0.0

    category2 = "OTHER"
    subcategory2 = "UNKNONW"
    category2Prob = 0.0

    sentence = ""
    tags = None

    # ****************************************************



    # make sure sentence has punctuation removed but retains case
    def __init__(self, _sentence, _nameDictionary):
        self.sentence = _sentence
        self.nameDictionary = _nameDictionary
        lower = str.lower(_sentence).rstrip('\r\n')
        self.tokens = lower.split()
        wiki = TextBlob(_sentence)
        self.tags = wiki.tags
        keyWord = self.tokens[0]

        # call the appropriate function to handle the keyword


        options = {
            "who": self.handle_who,
            "where": self.handle_where,
            "when": self.handle_when,
            "why": self.handle_why,
            "what": self.handle_what,
            "how": self.handle_how
        }
        if (keyWord in options.keys()):
            options[keyWord]()

            # The question begins with 'who'

    def handle_who(self):
        # these are base probabilities estimated from analysis
        personProb = 0.9
        groupProb = 0.8
        otherProb = 0.7
        if self.containsNNP():
            personProb *= 0.438
            groupProb *= 0.219
            otherProb *= 0.328

        if self.containsName():
            personProb *= 0.228
            groupProb *= 0.114
            otherProb *= 0.657


        if self.containsNamePossessive():
            personProb *= 1
            groupProb *= 0.3
            otherProb *= 0.3


        for t in self.tokens:
            if t in familyReferences:
                personProb *= 1
                groupProb *= 0.8
                otherProb *= 0.8

        # figure out highest and second highest probabilities

        probs = [personProb, groupProb, otherProb]
        highestProb = max(personProb, groupProb, otherProb)

        for x in range(0, 3):
            if probs[x] == highestProb:
                probs.remove(probs[x])
                break

        secondHighestProb = max(probs[0], probs[1])

        # assign results to member variables
        self.category1Prob = highestProb
        self.category2Prob = secondHighestProb

        if(highestProb != otherProb):
            self.category1 = "NAMEDENTITY"
            if highestProb == personProb:
                self.subcategory1 = "PERSON"

            else:
                self.subcategory1 = "GROUP"
            self.category1Prob = highestProb

        else:
            self.subcategory1 = "EXPLANATION"


        if(secondHighestProb != otherProb):
            self.category2 = "NAMEDENTITY"
            if secondHighestProb == personProb:
                self.subcategory2 = "PERSON"

            else:
                self.subcategory2 = "GROUP"
        else:
            self.subcategory2 = "EXPLANATION"


    # WHERE questions are nearly always named entity locations
    def handle_where(self):
        self.category1 = "NAMEDENTITY"
        self.subcategory1 = "LOCATION"
        self.category1Prob = 0.95

        self.category2 = "OTHER"
        self.subcategory2 = "EXPLANATION"
        self.category2Prob = 0.05

    # WHEN QUESTIONS ARE BEST HANDLED BY LOOKING FOR NAMED ENTITIES FIRST THEN TRYING TO EXTRACT TIME PHRASES
    def handle_when(self):
        self.category1 = "NAMEDENTITY"
        self.subcategory1 = "TIME"
        self.category1Prob = 0.6

        self.category2 = "OTHER"
        self.subcategory2 = "TIME"
        self.category2Prob = 0.4

    # WHY QUESTIONS TYPICALLY RESULT IN EXPLANATION ANSWERS
    def handle_why(self):
        self.category1 = "OTHER"
        self.subcategory1 = "EXPLANATION"
        self.category1Prob = 1.0

    # WHAT QUESTIONS TYPICALLY RESULT IN EXPLANATIONS OR NOUN PHRASES,
    # OCCASIONALLY THEY MAY RESULT IN NAMED ENTITIES
    def handle_what(self):
        for tag in self.tags:
            if str(tag).__contains__("name"):
                self.category1="NAMEDENTITY"
                self.category1Prob = 1.0
                self.subcategory1= "UNKNOWN"
                self.category2Prob = 0.0
                self.category2 = "OTHER"
                self.subcategory2 = "EXPLANATION"
                return
            if str(tag).__contains__("date"):
                self.category1 = "NAMEDENTITY"
                self.category1Prob = 0.8
                self.subcategory1 = "TIME"
                self.category2Prob = 0.2
                self.category2 = "OTHER"
                self.subcategory2 = "EXPLANATION"
                return
        self.category1 = "OTHER"
        self.category1Prob = 1.0
        self.subcategory1 = "EXPLANATION"

    # HOW QUESTIONS ARE OFTEN EXPLANATIONS OR
    def handle_how(self):
        if self.tags[1][1] == "DT" or self.tags[1][1] == "JJ" or self.tags[1][1] == "RB":
            self.category1 = "OTHER"
            self.subcategory1 = "QUANT"
            self.category1Prob = 0.75

            self.category2 = "OTHER"
            self.category2 = "EXPLANATION"
            self.category2Prob = 0.25
        else:
            self.category1 = "OTHER"
            self.subcategory1 = "EXPLANATION"
            self.category1Prob = 0.75

            self.category2 = "OTHER"
            self.category2 = "QUANT"
            self.category2Prob = 0.25


    # returns whether or not the question contains a proper noun phrase
    def containsNNP(self):

        if self.tags[1][1] == "NNP":
            return True
        else:
            return False



    def containsNamePossessive(self):
        result = False
        possessive = ""
        for t in self.tokens:
            m = re.search("([a-z]+s)$", t)
            if m is not None:
                possessive = t[:-1]
            try:
                value = self.nameDictionary[possessive]
                result = True
            except KeyError:
                pass
        return result




    def containsName(self):

        result = False
        for t in self.tokens:
            try:
                value = self.nameDictionary[t]
                result = True
            except KeyError:
                pass

        return result


