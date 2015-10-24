import sys
import math
import string
import overlap

def main():
    
    global textList
    textList = []

    global questionList
    questionList = []

    textFile = open('text.txt','r')
    textList = formatFileToList(textFile)
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

main()
    
        


