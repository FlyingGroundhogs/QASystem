__author__ = 'Hayden'
__name__ = "QuestionType"

import string

# response categories
RESPONSE_CATEGORIES = ['NAMED ENTITY',  'THING', 'LIST', 'EXPLANATION']

# this is a dictionary
RESPONSE_SUBCATEGORIES = {'NAMED ENTITY': ['PERSON', 'GROUP', 'PERSONORGROUP' 'LOCATION', 'TIME'],  'THING':['QUANTIFIER', 'QUANTITY'], 'LIST': [], 'EXPLANATION': []}


def containsTimeReference(tokens):

    timePhrases = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'hour', 'day', 'week', 'month', 'year']
    for token in tokens:
        if token in timePhrases:
            return True

    return False



class Classifier:

    responseCategory = "NONE"
    responseSubcategory = "NONE"


    def __init__(self, sentence):
       lower = str.lower(sentence).rstrip('\r\n')
       tokens = lower.split()

       if tokens.__contains__("who"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           if tokens.__contains__("were") or tokens.__contains__("are"):
               self.responseSubcategory = 'GROUP'
           if (tokens.__contains__("was") or tokens.__contains__("is")):
               self.responseSubcategory = 'PERSON'
           else:
               self.responseSubcategory = 'PERSONORGROUP'



       elif tokens.__contains__("where"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = 'LOCATION'

       elif (tokens.__contains__("when") or containsTimeReference(tokens) is True):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = 'TIME'

       elif tokens.__contains__("list"):
            self.responseCategory = RESPONSE_CATEGORIES[2]

       elif (tokens.__contains__("why") or tokens.__contains__("how") or tokens.__contains__("reason") or tokens.__contains__("explain")):
           self.responseCategory = RESPONSE_CATEGORIES[3]
           if(tokens.__contains__("how") and tokens.__contains__("much")):
               self.responseSubcategory = "QUANTIFIER"
           elif(tokens.__contains__("how") and tokens.__contains__("many")):
               self.responseSubcategory = "QUANTITY"
           elif(tokens.__contains__("how") and tokens.__contains__("long")):
               self.responseSubcategory = "QUANTITY"
       elif (tokens.__contains__("what")):
           self.responseCategory = RESPONSE_CATEGORIES[1]




