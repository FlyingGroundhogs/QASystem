import sys
import math
import string
import overlap
import NamedEntityRecognizer
import Classifier
def main():

    global textList
    textList = []

    global questionList
    questionList = []
    ner = NamedEntityRecognizer.NamedEntityRecognizer()
    textFile = open('textLonger.txt','r')
    textList = formatFileToList(textFile)
    textFile.close()

    questionFile = open('longerQuestions.txt','r')
    questionList = formatFileToList(questionFile)
    questionFile.close()

    for q in questionList:
        print ("\nQuestion: " + q)

        classifierResult = Classifier.Classifier(q)
        print("Response category: " +  classifierResult.responseCategory)
        print("Response subcategory: " + classifierResult.responseSubcategory)
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

main()
    
        


