__author__ = 'Mike'
__name__ = "QAMatcher"

import sys
import math
import string
import overlap
import os.path
import SClassifier
import Classifier
import VOverlap
from textblob import TextBlob
from nltk.corpus import wordnet as wn
import operator

class QAMatcher:

    stopWords = ['A','a','an','The','the','are','as','at','be','by','far','from'
        'has','he','in','is','it','its','it\'s','of','on','that','the',
        'to','was','were','will','with' 'a','an','the','are','as','at','be','by','far','from'
        'has','he','in','is','it','its','on','that','the',
        'to','was','were', 'with', 'when', 'may', 'some', 'what', 'for', 'Question']

    questionVerbs = []
    questionNouns = []

    def __init__(self, question, sentenceCategories, properNames):

        self.sentenceCandidates = {}

        #get lists of nouns and verbs in question
        qWiki = TextBlob(question)
        self.questionVerbs = self.getVerbs(qWiki)
        self.questionNouns = self.getNouns(qWiki)

        #get question categories
        cl = Classifier.Classifier(question, properNames)
        qCat1 = cl.category1
        qSubCat1 = cl.subcategory1
        qCat2 = cl.category2
        qSubCat2 = cl.subcategory2

        #get possible categories for each sentence and match up with question subcategory
        #(just working with question category 1 for now)
        for sentence in sentenceCategories:
            if qSubCat1 in sentenceCategories[sentence]:
                self.sentenceCandidates[sentence] = 0

        print ("CANDIDATE SENTENCES FOR CATEGORY: " + qSubCat1)
        for line in self.sentenceCandidates:
            print (line)

        #*******NOW WHAT? We can get best verb score, best noun score, and best overlap in code below
        #*******We need to come up with the best way to combine these to get a sentence score

        #for sentence in self.sentenceCandidates:
        #     self.getBestVerbScore(sentence)
        #     self.getBestNounScore(sentence)
        #     #self.sentenceCandidates[sentence] += overlap.overlapCount(question, sentence)
        #
        # if self.sentenceCandidates:
        #     bestSentence = max(self.sentenceCandidates, key=self.sentenceCandidates.get)
        #     self.getBestAnswer(clSubcat, bestSentence, properNames)
        # else:
        #     print ("Answer: " + overlap.bestOverlapCount(question, sentences) + "\n")




    #**************This is where we'll get the actual noun phrase from the answer
    #*************when we figure out how to score
    # def getBestAnswer(self, clSubcat, sentence, properNames):
    #     sCat = SClassifier.SClassifier(sentence, properNames)
    #     if clSubcat == "PERSON":
    #         print ("Answer: " + sCat.personArray[0] + '\n')
    #     elif clSubcat == "GROUP":
    #         print ("Answer: " + sCat.groupArray[0] + '\n')
    #     elif clSubcat == "PERSONORGROUP":
    #         print ("Answer: " + sCat.personOrGroupArray[0] + '\n')
    #     elif clSubcat == "LOCATION":
    #         print ("Answer: " + sCat.locationArray[0] + '\n')
    #     elif clSubcat == "TIME":
    #         print ("Answer: " + sCat.timeArray[0] + '\n')
    #     elif clSubcat == "EVENT":
    #         print ("Answer: " + sCat.eventArray[0] + '\n')



    def getBestVerbScore(self, sentence):
        count = 0
        sWiki = TextBlob(sentence)
        sVerbs = self.getVerbs(sWiki)
        bestVerb = ""

        if self.questionVerbs:
            #compare verbs for similarities and based on wordnet's similarity score
            #if they're exactly the same, they'll score 1
            for qverb in self.questionVerbs:
                synq = wn.synset(qverb + '.v.01')
                for sverb in sVerbs:
                    syns = wn.synset(sverb + '.v.01')
                    if syns.path_similarity(synq) > count:
                        count = syns.path_similarity(synq)
                        bestVerb = sverb

        self.sentenceCandidates[sentence] += count

    def getBestNounScore(self, sentence):
        count = 0
        sWiki = TextBlob(sentence)
        sNouns = self.getNouns(sWiki)
        bestNoun = ""

        if self.questionNouns and sNouns:
            #compare verbs for similarities and based on wordnet's similarity score
            #if they're exactly the same, they'll score 1
            for qnoun in self.questionNouns:
                synq = wn.synset(qnoun + '.n.01')
                for snoun in sNouns:
                    syns = wn.synset(snoun + '.n.01')
                    if syns.path_similarity(synq) > count:
                        count = syns.path_similarity(synq)
                        bestNoun = snoun

        self.sentenceCandidates[sentence] += count

    def getVerbs(self, blob):
        verbArray = []
        for tag in blob.tags:
            if tag[1][:1] is "V":
                verbmorph = wn.morphy(tag[0], wn.VERB) #pull out the normalized version of the verb
                if verbmorph is not None:
                    verbArray.append(verbmorph)

        return self.removeStopWordsArray(verbArray)

    def getNouns(self, blob):
        nounArray = []
        for tag in blob.tags:
            if tag[1] == "NN" or tag[1] == "NNS":
                nounmorph = wn.morphy(tag[0], wn.NOUN) #pull out the normalized version of the noun
                if nounmorph is not None:
                    nounArray.append(nounmorph)

        return self.removeStopWordsArray(nounArray)

    #TODO : Get closest verb frame
    # def getVerbFrames(self, blob):
    #     verbArray = []
    #     for tag in blob.tags:
    #         if tag[1][:1] is "V":
    #             verbArray.append(tag[0])
    #             print ("FRAME: " + tag[0])
    #             print (wn.synsets(tag[0]))
    #
    #     return verbArray


    def removeStopWords(self, sentence):

        s = set(sentence.split())
        r = (' '.join([i for i in s if i not in self.stopWords]))
        s = r.split()

        return s

    def removeStopWordsArray(self, sentenceArray):

        s = set(sentenceArray)
        r = (' '.join([i for i in sentenceArray if i not in self.stopWords]))
        s = r.split()

        return s

    def arrayToString(self, sentenceArray):

        s = (' '.join([i for i in sentenceArray]))

        return s





