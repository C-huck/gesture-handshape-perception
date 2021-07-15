# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:23:26 2021

@author: Jack
"""

#IMPORT STATEMENTS
import numpy as np
from scipy import spatial
from itertools import combinations
from nltk.corpus import wordnet as wn

#DEFINITIONS
def load_relevant_verbs():
    """
    Function reads in and reformats list of hand-selected verbs and their 
    categories from VerbNet
    
    Returns
    -------
    List
        Reformatted list of VerbNet verbs.

    """
    f = open("relevant-framenet-classes-and-LUs.txt", "r")
    dictionary = []
    for line in f.readlines():
        dictionary+=[x[:-2] for x in line.split(',') if x[-2:]=='.v']
    f.close()
    dictionary = [x.strip() for x in dictionary]    
    return list(set(dictionary))

def load_embeddings(filename):
    """
    Loads GLoVe word embeddings from file

    Parameters
    ----------
    filename : .txt
        Txt file containing word:vector pairs.

    Returns
    -------
    embeddings_dict : Dict
        Dictionary of word:vectors

    """
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

def get_distance(w1,w2):
    """
    Returns euclidean distance between two vectors

    Parameters
    ----------
    w1 : array
        1st word-vector.
    w2 : array
        2nd word-vector.

    Returns
    -------
    float
        distance between two vectors or nan if either/both vectors not in embeddings_dict.

    """
    try:
        return spatial.distance.euclidean(w1, w2)
    except:
        return np.nan

def get_mean_distance(embedding_samples):
    """
    Iterates through pairs of words in a list and returns mean distance

    Parameters
    ----------
    embedding_samples : Dict
        word:vector dictionary.

    Returns
    -------
    Float
        mean distance between each word in list. Excludes nan values.

    """
    iters = list(combinations(range(len(embedding_samples)),2))
    return np.nanmean([get_distance(embedding_samples[x[0]],embedding_samples[x[1]]) for x in iters]

def generate_bootstrapped_baseline(dictionary,embeddings_dict,n=20,iterations=1000):
    """
    Generates baseline measure by pseudo-randomly drawing words from hand-selected 
    VerbNet verb list. Verbs are grouped into transitive and intransitive sets,
    and the mean distance betweem verbs within each set is returned.

    Parameters
    ----------
    dictionary : list
        list of VerbNet verbs.
    embeddings_dict : dict
        embeddings dictionary.
    n : int, optional
        number of verbs to generate. The default is 20.
    iterations : int, optional
        number of times to generate randomly selected verbs. The default is 1000.

    Returns
    -------
    array
        array of distances.
    list
        list of word lists

    """
    vector_array = []
    i = 0
    if iterations % 2 == 0:
        bool_vec = [True]*int(iterations/2) + [False]*int(iterations/2)
    elif n % 2 ==0:
        bool_vec = ([True]*int(n/2) + [False]*int(n/2)) * iterations
    else:
        print('iterations or n must be even')
        return -1
    word_list = []
    while i < iterations:
        temp_array = []
        set_list = []
        while len(temp_array) < n:
            sample = np.random.choice(dictionary,1)[0]
            if is_transitive(sample) == bool_vec[i]:
                try:
                    temp_array.append(embeddings_dict[sample])
                    set_list.append(str(sample))
                except:
                    continue
            else:
                continue
        mean_dist = get_mean_distance(temp_array)
        vector_array.append(mean_dist)
        word_list.append(set_list)
        i+=1
    return vector_array,word_list


def is_transitive(word):
    """
    Identifies whether verb is/can be transitive or not using WordNets 
    verb frame data

    Parameters
    ----------
    word : str
        input word.

    Returns
    -------
    Bool, -1
        Returns True is verb is/can be transitive or False if intransitive.
        Returns -1 if verb is not in dictionary

    """
    try:
        word = wn.synsets(word,pos='v')[0]
        frame_ids = word.frame_ids()
        if len(set(frame_ids) & set([8,9,10,11,14,15,16,17,18,19,20,21,24,25])) > 0:
            return True
        else:
            return False
    except:
        return -1
