__author__ = 'Hayden'
__name__ = "NamedEntityRecognizer"
import  nltk


class NamedEntityRecognizer:



    def __init__(self, sentence):
       self.sentence = sentence

       self.tokens = nltk.word_tokenize(self.sentence)

       #do POS tagging on these tokens
       tagged = nltk.pos_tag(self.tokens)

       #get the named entities
       self.entities = nltk.chunk.ne_chunk(tagged, True)
       x = 32



    def printEntities(self):
         print self.entities




