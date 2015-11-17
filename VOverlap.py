__author__ = 'Mike'
__name__ = "VOverlap"

from textblob import TextBlob
from nltk.corpus import wordnet as wn

class Overlap:

    stopWords = ['A','a','an','The','the','are','as','at','be','by','far','from'
            'has','he','in','is','it','its','it\'s','of','on','that','the',
            'to','was','were','will','with' 'a','an','the','are','as','at','be','by','far','from'
            'has','he','in','is','it','its','on','that','the',
            'to','was','were', 'with', 'when', 'may', 'some', 'what', 'for']

    questionVerbs = []
    question = ''
    bestOverlap = ''
    qList = []

    def __init__(self, q, sentences):
        self.sentence = sentences
        self.qList = self.removeStopWords(q)
        self.question = self.arrayToString(self.qList)
        qWiki = TextBlob(self.question)
        self.questionVerbs = self.getVerbs(qWiki)

        # print ("Question verbs: ")
        # print (self.questionVerbs)

        print("BEST SENTENCE: " + self.bestOverlapCount(sentences))
        self.bestOverlap = self.bestOverlapCount(sentences)

    def getVerbs(self, blob):
        verbArray = []
        for tag in blob.tags:
            if tag[1][:1] is "V":
                verbmorph = wn.morphy(tag[0], wn.VERB) #pull out the normalized version of the verb
                if verbmorph is not None:
                    verbArray.append(verbmorph)
        return verbArray

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

    def bestOverlapCount(self, sentences):
        bestCount = 0
        bestSentence = ''

        for sentence in sentences:
            currentCount = self.overlapCount(sentence)
            if currentCount > bestCount:
                bestCount = currentCount
                bestSentence = sentence

        #print ("Best overlap count: %d" % bestCount)
        return bestSentence


    def overlapCount(self, sentence):
        #set count to be one so we can guess in case there are no sentences with overlap
        count = 1

        #remove stop words from sentence
        s = self.removeStopWords(sentence)
        sLower = self.removeStopWords(sentence.lower())

        sWiki = TextBlob(self.arrayToString(s))
        sVerbs = self.getVerbs(sWiki)

        #compare verbs for similarities and based on wordnet's similarity score
        #if they're exactly the same, they'll score 1
        for sverb in sVerbs:
            synv = wn.synset(sverb + '.v.01')
            for qverb in self.questionVerbs:
                synq = wn.synset(qverb + '.v.01')
                count += synv.path_similarity(synq)

        for word in self.qList:
             if word in s:
                 count += 1
             else:
                 if word.lower() in sLower:
                     count += 0.1
        return count

    def removeStopWords(self, sentence):

        s = set(sentence.split())

        r = (' '.join([i for i in s if i not in self.stopWords]))
        s = r.split()

        return s

    def arrayToString(self, sentenceArray):

        s = (' '.join([i for i in sentenceArray]))
        return s
