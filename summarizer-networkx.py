import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
 
def read_article(file_name):
    #file = open(file_name, "r")
    #filedata = file.readlines()
    #print(filedata)
    text="""Berkshire Hathaway (BRKB) bought new shares in pharmaceutical companies AbbVie (ABBV), Bristol-Myers Squibb (BMY), Merck (MRK) and Pfizer (PFE) during the third quarter. Pfizer has a promising coronavirus vaccine in the works, but the company's stock fell Monday after Moderna (MRNA) announced progress for its own vaccine. The company disclosed its latest holdings in a filing with the Securities and Exchange Commission after the closing bell Monday.  The investments in the big drug stocks are also noteworthy considering that Buffett and Berkshire, along with Amazon and banking giant JPMorgan Chase (JPM), are partners in a health care effort known as Haven. Berkshire Hathaway  (BRKA)also acquired a new stake in wireless telecom leader T-Mobil (TMUS) and sold off its position in retail giant Costco (COST). It's been an interesting (and busy) couple of months for the Oracle of Omaha and Berkshire, marked by several uncharacteristic moves for the long-time value investor. In August, Berkshire Hatahaway disclosed that it had bought a stake in mining company Barrick Gold (GOLD). Buffett has in the past bashed the yellow metal as an investment.  He once wrote in one of his annual shareholder letters that owning gold was like having a giant cube that sat there and never produced anything because the commodity doesn't generate profits or pay dividends. Berkshire also recently shocked Wall Street by investing in buzzy cloud software firm Snowflake ahead of its initial public offering.  Apple (AAPL) is currently Berkshire's largest holding, although the investment firm trimmed its stake in the stock by a small margin in the third quarter. But Buffett historically has been slow to embrace tech stocks — and when he does, they tend to be more mature companies such as Apple — not recent IPOs.  After all, Berkshire didn't invest in Amazon (AMZN) until the first quarter of 2019 — 22 years after the e-tailer's Wall Street debut. The company has also increased its investments in retail and health care lately. Within the past year, Berkshire has invested in grocery king Kroger (KR), high-end furnishings chain RH (RH) and drug company Biogen (BIIB). Berkshire announced in August that it had taken big stakes in several Japanese trading conglomerates. Earlier this summer, Berkshire also acquired natural gas assets from Dominion Energy (D) for nearly $10 billion. But Buffett has also been quick to unload stocks that haven't done so well recently. Berkshire Hathaway has slashed its position in Goldman Sachs (GS), which it had bought a big stake in during the middle of the Great Recession.  Berkshire has also been selling shares of Wells Fargo (WFC), the scandal-ridden bank that continues to struggle, and sold more of its holdings in the third quarter. And Berkshire liquidated its entire stake in four major airlines — American (AAL), Delta (DAL), Southwest (LUV) and United (UAL) — earlier this year as they have been hit hard by the Covid-19 pandemic."""
    filedata=[]
    filedata.append(text)

    article = filedata[0].split(". ")
    print(article)
    sentences = []

    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    #sentences.pop() 
    print("hello darling")
    print(sentences)
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
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
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    print(stop_words)
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences =  read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    ans=". ".join(summarize_text)
    print(ans)
    return ans
    #print("Summarize Text: \n", ". ".join(summarize_text))

# let's begin
attempt=generate_summary( "initial.txt", 6)
#final_ans2=generate_summary( "initial.txt", 4)
count=0
ideal="""Yoga can be a very healthy way of taking your mind off hectic schedules and focus on your spiritual transcendence.
One must consume meals at regular intervals and not skip meals, which leads to indigestion and weight gain.
Being healthy facilitates our productivity and ensures that we lead fulfilling lives.
Starting each day with some free-hand exercise like jogging or running ensures proper blood circulation in the body.
"""
from nltk.tokenize import sent_tokenize
i_attempt = sent_tokenize(attempt)
print("\nSentence-tokenized copy in a list:")
print(i_attempt)

i_ideal = sent_tokenize(ideal)
print("\nSentence-tokenized copy in a list:")
print(i_ideal)

for x in i_ideal:
  if x in i_attempt:
   count+=1

print(count) 
ans=(count/len(i_ideal))*100
print(ans)