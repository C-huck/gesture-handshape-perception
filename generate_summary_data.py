import pandas as pd
from collections import Counter
import numpy as np
from itertools import combinations
from nltk.corpus import wordnet as wn
from  nltk import word_tokenize,stem
from scipy import spatial

from sklearn.feature_extraction.text import TfidfVectorizer
import string

stemmer = stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(word_tokenize(text.lower().translate(remove_punctuation_map)))

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def get_mean_cosine_sim(sentence_list,iters):
    return np.nanmean([cosine_sim(sentence_list[x[0]],sentence_list[x[1]]) for x in iters])

def load_embeddings(fileIn="glove.840B.300d.txt"):
    """
    Loads word embeddings from file
    Parameters
    ----------
    fileIn : str, optional
        Source of pre-trained vector file. 
        The default is "glove.840B.300d.txt", retrieved from (https://nlp.stanford.edu/projects/glove/)

    Returns
    -------
    embeddings_dict : dictionary
        keys are words, values are 1x300-dimensional vectors.

    """
    embeddings_dict = {}
    with open(fileIn, 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            try:
                vector = np.asarray(values[1:], "float32")
            except:
                vector = np.asarray(values[1:])
            embeddings_dict[word] = vector
    return embeddings_dict

def get_distance(embeddings_dict,w1,w2):
    try:
        return spatial.distance.euclidean(embeddings_dict[w1], embeddings_dict[w2])
    except:
        return np.nan

def get_mean_distance(embeddings_dict,word_list):
    """
    Computes mean pair-wise (Euclidean) dictance between words in a set; calls get_distance().
    Parameters
    ----------
    embeddings_dict : dict
        embeddings dictionary created by load_embeddings().
    word_list : list
        list of words to analyze

    Returns
    -------
    mean_embed_dist: float
        mean pairwise 

    """
    word_combinations = list(combinations(range(len(word_list)),2))
    mean_embed_dist = np.nanmean([get_distance(embeddings_dict,word_list[x[0]],word_list[x[1]]) for x in word_combinations])
    return mean_embed_dist

def sdi(data):
    """
    Parameters
    ----------
    data : Dictionary; keys: words, values: word frequencies
        Computes Shannon Diversity Index (SDI)

    Returns
    -------
    sdi: float 
        Shannon Diversity Index.

    """
    
    from math import log as ln
    
    def p(n, N):
        """ Relative abundance """
        if n ==  0:
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
            
    N = sum(data.values())
    sdi = -sum(p(n, N) for n in data.values() if n != 0)
    return sdi

def get_penalized_distance_scores(w1,w2):
    a = [(y.path_similarity(x),i,j) for (i,x) in enumerate(w1) for (j,y) in enumerate(w2) if len(y.lowest_common_hypernyms(x)) > 0]
    if len(a) > 0:
        b = max([x[0]-(((x[1]+x[2])/10)*x[0]) for x in a])
    else:
        b = 0
    return max(b,0)

def get_mean_wn_path_simularity(synsets):
    iters = list(combinations(range(len(synsets)),2))
    return np.mean([get_penalized_distance_scores(synsets[x[0]],synsets[x[1]]) for x in iters])

def get_all_scores(df):    
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    res = []
    for x in set(df['item']):
        temp = df[df['item']==x]
        
        ##For SDI computation
        word_list = [x.split(',') for x in list(temp['verb'])]
        word_list = list(flatten(word_list))
        word_frequencies = Counter(word_list) #for SDI

        ##For cosine similarity computation
        sentence_list = list(temp['sentence'])
        iters_sen = list(combinations(range(len(sentence_list)),2))
        
        ##Compute average sentence transitivity
        avg_transitivity = np.mean(temp['transitivity']) #for transitivity score
        
        ##For wordnet path similarity computation
        synsets = [] 
        for y in temp['verb']:
            synsets.append(wn.synsets(y,pos='v'))
        res.append([x,round(avg_transitivity,4),
                    sdi(word_frequencies),
                    get_mean_wn_path_simularity(synsets),
                    get_mean_distance(embeddings_dict,word_list),
                    get_mean_cosine_sim(sentence_list,iters_sen)])
    return res

#Load embeddings
embeddings_dict = load_embeddings("C:/Users/Jack/ud120-projects/GloVe-master/glove.6B/glove.6B.50d.txt")

#Load sentences generated from action videos
df_action = pd.read_csv("../action_label.csv",header=0,converters={'verb': eval}).dropna()
df_action['verb'] = [','.join(x) for x in df_action['verb']]

#Get per-item mean transitivity, H-index (sdi), path similarity, embedding distance, and cosine similarity scores
df_scores_action = pd.DataFrame(data=get_all_scores(df_action),columns=["item","transitivity",'sdi','ps_score','embedding_score','cosine_sim_score'])

#Load sentences generated from gesture videos
columns = ["Input.field_1","Answer.sentence","verb","transitivity","RequesterFeedback","DELETE","WorkerId"]
df_gesture = pd.read_csv("data_final.csv",header=0,usecols=columns)
df_gesture = df_gesture[df_gesture['RequesterFeedback'].isna()].drop(columns=['RequesterFeedback'])
df_gesture = df_gesture[df_gesture['DELETE']!=1].drop(columns=['DELETE'])
df_gesture = df_gesture.rename(columns={'Input.field_1':'item','Answer.sentence':'sentence'}).dropna()

#Get per-item mean transitivity, H-index (sdi), path similarity, embedding distance, and cosine similarity scores
df_scores_gesture = pd.DataFrame(data=get_all_scores(df_gesture),columns=["item","transitivity",'sdi','ps_score','embedding_score','cosine_sim_score'])
