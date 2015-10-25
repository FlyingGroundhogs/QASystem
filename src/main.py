import sys
import math
import string
import overlap
import HandCraftedNER

# use dictionary for holding names so we can index
_properNames = {}
def main():

    global textList
    textList = []

    global questionList
    questionList = []


    textFile = open('text.txt','r')
    textList = formatFileToList(textFile)
    textFile.close()

    textFile = open('text.txt','r')
    NERGraph = generateNamedEntitiesGraph(textFile)
    textFile.close()



    questionFile = open('questions.txt','r')
    questionList = formatFileToList(questionFile)
    questionFile.close()

    for q in questionList:
        print ("\nQuestion: " + q)
        print ("Best overlap sentence: " + overlap.bestOverlapCount(q, textList))

def formatFileToList(file):
    fileList = []
    for line in file:
        #change to lowercase and remove line breaks
        toLower = str.lower(line).rstrip('\r\n')

        #remove punctuation
        formattedLine = "".join(c for c in toLower if c not in string.punctuation)
        fileList.append(formattedLine)

    return fileList

def generateNamedEntitiesGraph( file):
    lineDict = {}
    #build the name dictionary
    nameFile = open('names.txt', 'r')
    for line in nameFile:
        tokens = line.split()
        _properNames[tokens[0].lower()] = 1

    for line in file:
        # remove line breaks
        cleaned = str(line).rstrip('\r\n')

        #remove punctuation
        formattedLine = "".join(c for c in cleaned if c not in string.punctuation)


        ner = HandCraftedNER.NER(formattedLine, _properNames)
        ner.printArrays()

        lowered = cleaned.lower()


    return lineDict

main()



