__author__ = 'Hayden'
__name__ = "NamedEntityRecognizer"
import  nltk


class NamedEntityRecognizer:
    def __init__(self, sentence):
       self.sentence = sentence

       tokens = nltk.word_tokenize(self.sentence)

       #do POS tagging on these tokens
       tagged = nltk.pos_tag(tokens)

       #get the named entities

       entities = nltk.chunk.ne_chunk(tagged)
       x = 32