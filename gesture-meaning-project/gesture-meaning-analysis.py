##Import statements
import pandas as pd

##Definitions
def get_distance(dictionary,w1,w2):
    from scipy import spatial
    try:
        return spatial.distance.euclidean(dictionary[w1], dictionary[w2])
    except:
        return np.nan#, (w1,w2)

def get_mean_distance(dictionary,word_list):
    iters = list(combinations(range(len(word_list)),2))
    return np.nanmean([get_distance(dictionary,word_list[x[0]],word_list[x[1]]) for x in iters])

def generate_random_verb_list(dictionary,size=20): 
    out_list = []
    import random
    from nltk.corpus import wordnet as wn
    i = 0
    while i < size:
        draw = random.choice(list(dictionary.keys())) #randomly draw entry from GloVe word-embedding dictionary
        if len(wn.synsets(draw,pos='v'))>0 and draw not in out_list: #only add entry if it is a verb in wordnet corpus and not already in list
            out_list.append(draw)
            i+=1
        else:
            continue
    return out_list

def load_embeddings(filename):
        embeddings_dict = {}
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                values = line.split()
                word = values[0]
                try:
                    vector = np.asarray(values[1:], "float32")
                except:
                    vector = np.asarray(values[1:])
                embeddings_dict[word] = vector
        return embeddings_dict

embeddings_dict = load_embeddings("C:/Users/Jack/ud120-projects/GloVe-master/glove.6B/glove.6B.300d.txt")

##Import data

#Import preprocessed data from liva action videos (=action-verbs)
df_action = pd.read_csv('../data_actions.csv')

#Import preprocessed data from gesture videos (=gesture-verbs)
df_action = pd.read_csv('../data_gestures.csv')

#Generate lists of random verbs
random_verbs = []
for i in range(69):
    temp = generate_random_verb_list(embeddings_dict)
    random_verbs.append(temp)
  
##ANALYSIS 1: Are action-verbs more semantically related to gesture 
