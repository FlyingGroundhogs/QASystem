__author__ = 'Hayden'
__name__ = "QuestionType"

import string

# response categories
RESPONSE_CATEGORIES = ['NAMED ENTITY',  'THING', 'LIST', 'EXPLANATION']

# this is a dictionary
RESPONSE_SUBCATEGORIES = {'NAMED ENTITY': ['PERSON', 'GROUP', 'PERSONORGROUP', 'LOCATION', 'TIME', 'EVENT'],  'THING':['QUANTIFIER', 'QUANTITY'], 'LIST': [], 'EXPLANATION': []}


def containsTimeReference(tokens):

    timePhrases = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'hour', 'day', 'week', 'month', 'year']
    for token in tokens:
        if token in timePhrases:
            return True

    return False

def containsGroupReference(tokens):
        groupReferences = ['co', 'corporation', 'llc', 'org', 'brothers', 'partners', 'sisters', 'association', 'organization',
                       'committee', 'assembly', 'consortium', 'google', 'congress', 'government', 'walmart', 'exxon',
                       'chevron', 'berkshire', 'apple', 'motors', 'foundation', 'center', 'group', 'school', 'board',
                       'directors', 'followers', 'church', 'ambassadors', 'research', 'centre', 'players', 'lions',
                       'bears', 'eagles', 'panthers', 'cowboys', 'wolves', 'bears', 'football', 'basketball', 'team',
                       'governments', 'committees', 'organizations', 'commission', 'oilers', 'yankees', 'sox', 'cardinals',
                       'bruins', 'trojans', 'canadians', 'wings', 'sabres', 'ducks', 'stars', 'panthers', 'devils',
                       'avalanche', 'flyers', 'leafs', 'jets', 'blues', 'capitals', 'senators', 'student', 'worker',
                       'workers', 'union', 'post', 'inquirer', 'herald', 'network', 'times', 'daily', 'journal', 'press',
                       'tribune', 'star', 'sun', 'gazette', 'review', 'weekly', 'agency', 'national', 'administration', 'americans',
                       'canadians', 'republicans', 'democrats', 'republican', 'democratic', 'order', 'federation']


        for token in tokens:
            if token in groupReferences:
                return True

        return False



class Classifier:

    responseCategory = "NONE"
    responseSubcategory = "NONE"


    def __init__(self, sentence):
       lower = str.lower(sentence).rstrip('\r\n')
       tokens = lower.split()

       self.responseSubcategory = "NONE"
       if tokens.__contains__("whose"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = "PERSONORGROUP"

       if tokens.__contains__("who"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           if tokens.__contains__("were") or tokens.__contains__("are" or containsGroupReference(tokens)):
               self.responseSubcategory = 'GROUP'
           if (tokens.__contains__("was") or tokens.__contains__("is")):
               self.responseSubcategory = 'PERSON'
           else:
               self.responseSubcategory = 'PERSONORGROUP'

       elif tokens.__contains__("happened") or tokens.__contains__("caused") or tokens.__contains__("event"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = 'EVENT'

       elif tokens.__contains__("where"):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = 'LOCATION'


       elif ((tokens.__contains__("when") and tokens.__contains__("what") is False) or containsTimeReference(tokens) is True):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory = 'TIME'

       elif ((tokens.__contains__("when") and tokens.__contains__("what") is True) or containsTimeReference(tokens) is True):
           self.responseCategory = RESPONSE_CATEGORIES[3]


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
           elif(tokens.__contains__("how") and tokens.__contains__("big")):
               self.responseSubcategory = "QUANTITY"

       elif (tokens.__contains__("cost")):
           self.responseCategory = RESPONSE_CATEGORIES[3]
           self.responseSubcategory = "QUANTITY"

       elif(tokens.__contains__("what") and containsGroupReference(tokens) and (tokens.__contains__("type") is False and tokens.__contains__("kind") is False )):
           self.responseCategory = RESPONSE_CATEGORIES[0]
           self.responseSubcategory= "GROUP"
       elif (tokens.__contains__("what")):
           self.responseCategory = RESPONSE_CATEGORIES[1]





