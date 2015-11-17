__author__ = 'Hayden'
__name__ = "QuestionType"

import string
from textblob import TextBlob
from nltk.corpus import wordnet as wn

# response categories
RESPONSE_CATEGORIES = ['NAMED ENTITY', 'OTHER']

# this is a dictionary
RESPONSE_SUBCATEGORIES = ['PERSON', 'GROUP', 'PERSONORGROUP', 'LOCATION', 'TIME', 'EXPLANATION', 'EVENT', 'QUANT',
                          'UNKNOWN']


def containsTimeReference(tokens):
    timePhrases = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'january', 'february', 'march', 'april',
                   'may', 'june', 'july', 'august', 'september',
                   'october', 'november', 'december', 'hour', 'day', 'week', 'month', 'year']
    for token in tokens:
        if token in timePhrases:
            return True
    return False


def containsGroupReference(tokens):
    groupReferences = ['co', 'corporation', 'llc', 'org', 'brothers', 'partners', 'sisters', 'association',
                       'organization',
                       'committee', 'assembly', 'consortium', 'google', 'congress', 'government', 'walmart', 'exxon',
                       'chevron', 'berkshire', 'apple', 'motors', 'foundation', 'center', 'group', 'school', 'board',
                       'directors', 'followers', 'church', 'ambassadors', 'research', 'centre', 'players', 'lions',
                       'bears', 'eagles', 'panthers', 'cowboys', 'wolves', 'bears', 'football', 'basketball', 'team',
                       'governments', 'committees', 'organizations', 'commission', 'oilers', 'yankees', 'sox',
                       'cardinals',
                       'bruins', 'trojans', 'canadians', 'wings', 'sabres', 'ducks', 'stars', 'panthers', 'devils',
                       'avalanche', 'flyers', 'leafs', 'jets', 'blues', 'capitals', 'senators', 'student', 'worker',
                       'workers', 'union', 'post', 'inquirer', 'herald', 'network', 'times', 'daily', 'journal',
                       'press',
                       'tribune', 'star', 'sun', 'gazette', 'review', 'weekly', 'agency', 'national', 'administration',
                       'americans',
                       'canadians', 'republicans', 'democrats', 'republican', 'democratic', 'order', 'federation']

    for token in tokens:
        if token in groupReferences:
            return True

    return False


class Classifier:
    # ************MEMBER VARIABLES *************************
    responseCategory = "OTHER"
    responseSubcategory = "UNKNOWN"

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



    def __init__(self, _sentence):
        self.sentence = _sentence
        lower = str.lower(_sentence).rstrip('\r\n')
        tokens = lower.split()
        wiki = TextBlob(_sentence)
        self.tags = wiki.tags
        keyWord = tokens[0]

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
        if self.containsNNP():
            x = 32

    def handle_where(self):
        x = 32

    def handle_when(self):
        x = 32

    def handle_why(self):
        x = 32

    def handle_what(self):
        x = 32

    def handle_how(self):
        x = 32

    # returns whether or not the question contains a proper noun phrase
    def containsNNP(self):
        for tag in self.tags:
            if tag[1] == "NNP":
                return True
