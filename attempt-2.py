import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from string import punctuation
from nltk.cluster.util import cosine_distance
import numpy as np
import math

text ="""skipOneand as you can clearly see thatelectric electric being started.And after every five seconds, we willhave this have this thing printed up.It's going to capture the captionsand that's going to be an and that's going to be an importantpart.I'm going to present the mate. So hello students today.We will be So hello students today.We will be learning how I coded formaking this Chrome extension.so I'll So I'll share my screen. nowlook at this particular functionstart button look at this particular functionstart button dot add event listener.So what this function does is that itbasically basically binds this click method onthe start button.So whenever you click on the startbutton, This particular script will run.now here what we do we Now here what we do we get the Now here what we do we get thehostname if the hostname is me dotgoogle.com then it is a Google meetand we can further start recordingstart fetching the meat. in that case what we do is we callthis get data method when in In that case what we do is we callthis get data method when in itextracts all the text of all thespans which are in that case what we do is we callthis get data method when in itextracts all the text of all thespans which are specificallygenerating this particular text andit returnsOkay. And when you submit the button, sothis is a subject.so So I'll take a snapshot.that matter now now here when we have this particularmethod that is all the now here when we have this particularmethod that is all the URL parametersare present subject name lecture nametranscript email images and easement. now here when we have this particularmethod that is all the URL parametersare present subject name lecture nametranscript email images and easement.These are the parameters of URLparams and the request is made whenthe request gets completed. Only if so, this is like when therequest is ready.and when the request is done and And when the request is done and thestatus is 200 then we add thatparticular. 
Okay.Now I'll take a snapshot again.
"""
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
   #print(sent1)
   #print(sent2)
    all_words = list(set(sent1 + sent2))
    
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
   
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        if w in punctuation:
        	continue
        vector1[all_words.index(w)] += 1
        
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        if w in punctuation:
        	continue
        vector2[all_words.index(w)] += 1
       
    
    #print(vector1)
    #print(vector2)
 
    return 1 - cosine_distance(vector1, vector2)
 

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix



stopWords = set(stopwords.words("english")) 
punctuation = punctuation + '\n'

article = sent_tokenize(text) 

sentences = []

for sentence in article:
    sentences.append(sentence.replace("[^a-zA-Z]", "[^0-9]").split(" "))

sentence_similarity_martix = build_similarity_matrix(sentences, stopWords)
sum_value=[np.sum(sen) for sen in sentence_similarity_martix]
   
sen_set=set()
for i in range(len(sum_value)):
    sen_set.add(i)
    

for i in range(len(sum_value)):
    for j in range(len(sum_value)):
        if sentence_similarity_martix[i][j]>0.8:
                if sum_value[i]>sum_value[j]:
                    sen_set.discard(j)
                else:
                    sen_set.discard(i)
n=len(sen_set)
n=math.ceil(math.sqrt(n))

final_text=[]
for idx in sen_set:
    final_text.append(sentences[idx])
#print(final_text)     #already word tokenized

#print(len(final_text))    #number of sentences making the cut
reduced_word=""
reduced_text=""
#joining word toekns to make sentence tokens


for w in final_text:
	reduced_word=" ".join(w)
	reduced_text+=' ' + reduced_word




words = word_tokenize(reduced_text) 

freqTable = dict() 
for word in words: 
    word = word.lower() 

    if word not in stopWords: 
      
    	if word not in punctuation:
    	
		    if word not in freqTable: 
		        freqTable[word] = 1
		    else: 
		        freqTable[word] += 1

sentenceValue = dict() 
lines = sent_tokenize(reduced_text) 

for sent in lines: 
    for word, freq in freqTable.items(): 
        if word in sent.lower(): 
            if sent in sentenceValue: 
                sentenceValue[sent] += freq 
            else: 
                sentenceValue[sent] = freq 


sumValues = 0
for sent in sentenceValue: 
    sumValues += sentenceValue[sent] 


# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue)) 

count=0
# Storing sentences into our summary. 
summary = " " 
for sent in lines: 
    if (sent in sentenceValue) and (sentenceValue[sent] > (1.2 * average) and count<=n): 
        summary += " " + sent
        count += 1 
        
print(summary) 