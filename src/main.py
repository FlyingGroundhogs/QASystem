import sys
import math
import string
import overlap
import os.path
import HandCraftedNER
import Classifier
_properNames = {}

def main():

    #this is only for our testing with a relative filepath; to be removed when handing in
    currentPath = os.getcwd()
    parentDir = (os.path.abspath(os.path.join(currentPath, os.pardir)))
    inputFilePath = os.path.join(parentDir, "inputfile.txt")

    #list of IDs
    fileIDArray = []

    #collection to append .story and .questions to IDs in fileIDArray
    questionStoryArray = []

    inputFile = open(inputFilePath, 'r')
    for line in inputFile:
        fileIDArray.append(line)
    inputFile.close()

    #file path to developset
    developSetPath = os.path.join(parentDir, fileIDArray[0]).rstrip()

    for i in range(1,len(fileIDArray)):
        story = fileIDArray[i].rstrip() + '.story'
        questionFile = fileIDArray[i].rstrip() + '.questions'
        questionStoryArray.append(story + ' ' + questionFile)

    for questStory in questionStoryArray:
        qs = questStory.split()
        storyPath = os.path.join(developSetPath, qs[0])
        storyFile = open(storyPath, 'r')
        sentenceArray = formatFileToList(storyFile, '.')

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
            question = formatQuestion(qArray[q+1])
            print (qID)
            print (question)

            #print ("CLASSIFIER: TYPE OF RESPONSE: ")
            cl = Classifier.Classifier(question)

            clSubcat = ''
            #print (cl.responseCategory)
            if(cl.responseCategory is not None):
                #print (cl.responseSubcategory)
                clSubcat = cl.responseSubcategory

            bestOverlap = overlap.bestOverlapCount(question, sentenceArray)
            #print ("Best overlap sentence: " + bestOverlap)
            #send names into memory for efficiency
            readInProperNames()
            ner = HandCraftedNER.NER(bestOverlap, _properNames)
            #ner.printArrays()

            if clSubcat is "PERSON" and ner.personArray:
                print ("Answer: " + ner.personArray[0])
            elif clSubcat is "GROUP" and ner.groupArray:
                print ("Answer: " + ner.groupArray[0])
            elif clSubcat is "PERSONORGROUP" and ner.personOrGroupArray:
                print ("Answer: " + ner.personOrGroupArray[0])
            elif clSubcat is "LOCATION" and ner.locationArray:
                print ("Answer: " + ner.locationArray[0])
            elif clSubcat is "TIME" and ner.timeArray:
                print ("Answer: " + ner.timeArray[0])
            elif clSubcat is "EVENT" and ner.eventArray:
                print ("Answer: " + ner.eventArray[0])
            else:
                print ("Answer: " + bestOverlap)


        storyFile.close()
        qFile.close()

def formatFileToList(file, delimiter):
    formattedList = []
    #add misc punctuation to this array as we find it
    miscPunctList = ['--','-']

    #skip the header info
    for i in range (1,7):
        file.readline()
    data = file.read()

    sentenceList = data.split(delimiter)

    for line in sentenceList:

        #change to lowercase, remove line breaks, strip trailing whitespace
        toLower = (line).replace('\n',' ').strip()

        #remove punctuation
        formattedLine = "".join(c for c in toLower if c not in string.punctuation)
        formattedLine = "".join(c for c in toLower if c not in miscPunctList)
        #only add to main list if string is non-empty
        if formattedLine:
            formattedList.append(formattedLine)

    return formattedList

def formatQuestion(line):

    #change to lowercase, remove line breaks, strip trailing whitespace
    toLower = str.lower(line).replace('\n','').strip()

    #remove the first word 'question'
    toLower = toLower.split(' ',1)[1]

    #remove punctuation
    formattedLine = "".join(c for c in toLower if c not in string.punctuation)

    return formattedLine


def readInProperNames( ):

    #build the name dictionary
    nameFile = open('names.txt', 'r')
    for line in nameFile:
        tokens = line.split()
        _properNames[tokens[0].lower()] = 1

main()











