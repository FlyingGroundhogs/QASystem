global stopWords

stopWords = ['a','an','the','are','as','at','be','by','far','from'
            'has','he','in','is','it','its','of','on','that','the',
            'to','was','were','will','with' 'a','an','the','are','as','at','be','by','far','from'
            'has','he','in','is','it','its','on','that','the',
            'to','was','were','will','with', 'when', 'may', 'some', 'more', 'residents', 'students',
            'faculty', 'scientists', 'researchers', 'proceeds']


def bestOverlapCount(question, sentences):
    bestCount = 0
    bestSentence = ''
    
    for sentence in sentences:
        currentCount = overlapCount(question, sentence)
        if currentCount > bestCount:
            bestCount = currentCount
            bestSentence = sentence

    #print ("Best overlap count: %d" % bestCount)
    return bestSentence
        

def overlapCount(question,sentence):
    count = 0
    
    #remove stop words from question and sentence
    q = removeStopWords(question)
    s = removeStopWords(sentence)

    for word in q:
        if word in s:
            count += 1

    return count


def removeStopWords(sentence):

    #remove dups by making a set  
    s = set(sentence.split())

    r = (' '.join([i for i in s if i not in stopWords]))
    s = r.split()
          
    return s




