__author__ = 'Hayden'
__name__ = "NamedEntityRecognizer"
import  nltk


class NamedEntityRecognizer:

    def __init__(self):
       x = 32

    def initialize(self, sentence):
       self.sentence = sentence

       self.tokens = nltk.word_tokenize(sentence)

       #do POS tagging on these tokens
       tagged = nltk.pos_tag(self.tokens)

       #get the named entities
       self.entities = nltk.chunk.ne_chunk(tagged, False)




    def printEntities(self):
         print self.entities




