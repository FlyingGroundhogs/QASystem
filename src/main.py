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
    textList = formatFileToList(textFile, '.')
    textFile.close()

    questionFile = open('questions.txt','r')
    questionList = formatFileToList(questionFile, '?')
    questionFile.close()

    for q in questionList:
        print ("\nQuestion: " + q)
        print ("Best overlap sentence: " + overlap.bestOverlapCount(q, textList))
        
def formatFileToList(file, delimiter):

    formattedList = []
    data = file.read()
    sentenceList = data.split(delimiter)
    
    for line in sentenceList:
        #change to lowercase, remove line breaks, strip trailing whitespace
        toLower = str.lower(line).replace('\n','').strip()
        
        #remove punctuation
        formattedLine = "".join(c for c in toLower if c not in string.punctuation)
        #only add to main list if string is non-empty
        if formattedLine:
            formattedList.append(formattedLine)

    return formattedList

main()
    
        


