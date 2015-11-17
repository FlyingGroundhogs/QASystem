__author__ = 'Hayden'
__name__ = "QAnalyzer"

import string
from textblob import TextBlob
from nltk.corpus import wordnet as wn

import sys


#this is a question analyzer, it's being used in order to figure out how pos tags in the first few words of a question
#correlate with answer categories
class QAnalyzer:
    def __init__(self, filename):

        questionCount = 0
        #read in the questions line by line
        inputFile = open(filename, 'r')
        for line in inputFile:
            tokens = line.split()
            if(len(tokens) != 0):
                if str(tokens[0]).lower()== "question:":
                    blob = TextBlob(line)
                    questionCount +=1

                    print(line + str(blob.tags))

                elif str(tokens[0]).lower() == "answer:":
                    print(line)

        print(questionCount)

