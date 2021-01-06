from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
 
def read_article(file_name):
    file = open(file_name, "r")
    #filedata = file.read()
    filedata=["I am Yash Yash",
"I am Sarakshi",
"I am Palak Palak Palak",
"I am Saif",
"I am Sarakshi",
"I am harvey",
"I am Saif and Harvey and Yash",
"I am Sarakshi",
"I am Palak Palak Palak",
"I am Yash Palak Sarakshi"]
    print(filedata)
    article=filedata
    #article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))  #include numbers
    #sentences.pop() 
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    print(sent1)
    print(sent2)
    all_words = list(set(sent1 + sent2))
    
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
        
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
       
    
    print(vector1)
    print(vector2)
 
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


def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences =  read_article(file_name)
    print(sentences)
    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    print(sentence_similarity_martix)

    sum_value=[np.sum(sen) for sen in sentence_similarity_martix]
    print("===========================================================")
    sen_set=set()
    for i in range(len(sum_value)):
        sen_set.add(i)
    print("===========================================================")
    print(sen_set)
    print(sum_value)
    for i in range(len(sum_value)):
        for j in range(len(sum_value)):
            if sentence_similarity_martix[i][j]>0.8:
                if sum_value[i]>sum_value[j]:
                    sen_set.discard(j)
                else:
                    sen_set.discard(i)
    print("========================================================hellooooooooooooo===")
    
    print(sen_set)
    final_text=[]
    for idx in sen_set:
        final_text.append(sentences[idx])
    print(final_text)
    
    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    #print("===========================================================")
    #print(sentence_similarity_graph)
    scores = nx.pagerank(sentence_similarity_graph)
    print(scores)
    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    print("Summarize Text: \n", ". ".join(summarize_text))

# let's begin
generate_summary( "raatko.txt",2 )