import sys
import math
import string
import overlap
import os.path
import SClassifier
import Classifier
import VOverlap
import QAMatcher
from textblob import TextBlob

_properNames = {}
_locations = {}

def main():

    readInProperNames()
    readInLocations()

    #inputFileName = sys.argv[1]
    inputFileName = "inputfile.txt"

    #list of IDs
    fileIDArray = []

    #collection to append .story and .questions to IDs in fileIDArray
    questionStoryArray = []

    inputFile = open(inputFileName, 'r')
    for line in inputFile:
		#if there are lines at the end of the text, ignore them
        if line.strip():
            fileIDArray.append(line)
    inputFile.close()

    #file path to developset
    dSetPath = fileIDArray[0]
    developSetPath = os.path.normpath(dSetPath).rstrip()

    for i in range(1,len(fileIDArray)):
        story = fileIDArray[i].rstrip() + '.story'
        questionFile = fileIDArray[i].rstrip() + '.questions'
        questionStoryArray.append(story + ' ' + questionFile)

    for questStory in questionStoryArray:

        qs = questStory.split()
        storyPath = os.path.join(developSetPath, qs[0])
        storyFile = open(storyPath, 'r')

        #get all possible categories for each sentence and keep them for reference
        #before we even look at the question
        masterSentenceCategories = {}
        sentenceArray = formatFileToList(storyFile)
        for sentence in sentenceArray:
            sCat = SClassifier.SClassifier(sentence, _properNames, _locations)
            masterSentenceCategories[sentence] = sCat.categories

        quest = qs[1]
        questionPath = os.path.join(developSetPath, quest)
        qFile = open(questionPath, 'r')
        qArray = []
        for line in qFile:
            l = line.rstrip()
            if l:
                qArray.append(l)

        for q in range(0, len(qArray), 3):
            qID = qArray[q]
            question = qArray[q+1]
            #removes "Question:" from the line, removes punctuation and capitals
            question = formatQuestion(question)

            print(qID)
            print (question)
            #get the question category, find the best sentence per our
            #master sentence categories list
            matcher = QAMatcher.QAMatcher(question, masterSentenceCategories, _properNames)

        storyFile.close()
        qFile.close()

def formatFileToList(file):
    formattedList = []
    #add misc punctuation to this array as we find it
    miscPunctList = ['--','-']

    #skip the header info
    for i in range (1,7):
        file.readline()
    data = file.read()

    #this is an easy way to separate sentences so that initials like D.H. or
    #titles like Dr. are not mistaken for a separate sentence
    zen = TextBlob(data)
    sentenceList = zen.sentences

    for line in sentenceList:
        #remove line breaks, strip trailing whitespace
        line = (line).replace('\n',' ').strip()

        #remove punctuation
        #formattedLine = "".join(c for c in line if c not in string.punctuation)
        formattedLine = "".join(c for c in line if c not in miscPunctList)
        #only add to main list if string is non-empty
        if formattedLine:
            formattedList.append(formattedLine)

    return formattedList

def formatQuestion(line):

    #change to lowercase, remove line breaks, strip trailing whitespace
    toLower = str(line).lower().replace('\n','').replace(',','').strip()

    #remove the first word 'question'
    toLower = toLower.split(' ',1)[1]

    #remove punctuation
    formattedLine = "".join(c for c in toLower if c not in string.punctuation)

    return formattedLine


def readInProperNames():

    #build the name dictionary
    nameFile = open('names.txt', 'r')
    for line in nameFile:
        tokens = line.split()
        _properNames[tokens[0].lower()] = 1

def readInLocations():

    locFile = open('CAlocations.txt', 'r')
    for line in locFile:
        line = str(line).lower().replace('\n','')
        tokens = line.split(':')
        cityCountry = tokens[1].split(',')

        city = cityCountry[0].strip()
        country = cityCountry[1].strip()
        _locations[city] = 1
        _locations[country] = 1
    locFile.close()

    countryFile = open('countries.txt', 'r')
    for line in countryFile:
        line = str(line).lower().replace('\n','')
        _locations[line] = 1
    countryFile.close()

    USCitiesFile = open('UScities.txt', 'r')
    for line in USCitiesFile:
        line = str(line).lower().replace('\n','')
        _locations[line] = 1
    USCitiesFile.close()

    USStatesFile = open('states.txt', 'r')
    for line in USStatesFile:
        line = str(line).lower().replace('\n','')
        _locations[line] = 1
    USStatesFile.close()

    worldCitiesFile = open('worldCities.txt', 'r')
    for line in worldCitiesFile:
        city = line.split()[1].strip()
        _locations[city] = 1

    worldCitiesFile.close()

main()











