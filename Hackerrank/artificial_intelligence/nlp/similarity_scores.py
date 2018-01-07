# -*-coding:Latin-1 -*
"""The Python3 code solving the Hackerrank problem entitled 'Similarity scores'"""

import re
import math

#===========================
# the 'Document' class
#===========================

class Document:
    """A class representing the contents of a document:

    - .text        = the processed contents of the document: lowercase, no punctuation
    - .nwords      = the total number of words in the processed document
    - .occurrences = the dictionnary representing the number of occurrences
                     of each unique word in the document
       
    """

    def __init__(self, text):
        """Initialise the contents of the document"""
        
        self.text = re.sub(r"[.,;:?!]+", r" ", text.strip().lower())

        words = self.text.split()
        self.nwords = len(words)
        
        self.occurrences = {}       
        for word in words:
            if word not in self.occurrences:
                self.occurrences[word] = 1
            else:
                self.occurrences[word] += 1


    def computeTF(self, word):
        """Compute the term frequency of 'word' in the document"""
        
        if self.nwords != 0 and word in self.occurrences:
            return self.occurrences[word] / self.nwords
        return 0

    def __repr__(self):
        return str(self.occurrences)


#=================================================================================
# main program
#=================================================================================

docs = []
docs.append(Document("I'd like an apple."))
docs.append(Document("An apple a day keeps the doctor away."))
docs.append(Document("Never compare an apple to an orange."))
docs.append(Document("I prefer scikit-learn to orange."))

querry = docs[0]    # use the first document as querry 


#=================================================================================
# compute the inverse document frequency (IDF) scores
# indicating the importance of a term in a corpus (over all documents)
# [ idf(t, D) = log(|D| / |{d: t in d}| ]
#
#=================================================================================

IDF = {}
for qword in querry.occurrences:                # for each querry word
    matched_docs = 0                            
    for doc in docs:                            # for each document        
        if qword in doc.occurrences:            # if querry word present in document
            matched_docs += 1    
    IDF[qword]= math.log(len(docs)/matched_docs)

    
#=================================================================================
# compute the term frequency (TF) scores
# of each querry word in each document
# [ tf(t,d)= freq(t,d)/|{t':t' in d}|]
#
# compute the TF-IDF scores as
# [ tf-idf(t,d,D) = tf(t,d) x idf(t,D) ]
#=================================================================================

TFIDF = []
for i, doc in enumerate(docs):                  # for each document
    TFIDF.append({})                                
    for qword in querry.occurrences:            # for each querry word
        TFIDF[i][qword] = IDF[qword] * doc.computeTF(qword)
        

#=================================================================================
# get the most similar document to the first document
#=================================================================================

max_id = 0
max_sum = 0
for i in range(1, len(docs)):
    dsum = sum(TFIDF[i].values())               # sum of the tf-idf scores of querry words in doc 'i'
    if dsum >= max_sum:
        max_sum = dsum
        max_id = i+1

    print("The similarity score between Doc-1 and Doc-{} = {}".format(i+1,dsum))

print("\nThe document most similar to the first document is Doc-{}".format(max_id))
    
    
