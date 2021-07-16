# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:23:26 2021

@author: Jack
"""

#IMPORT STATEMENTS
import numpy as np
from nltk.corpus import wordnet as wn
import common_functions as cf

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
    corpus = []
    for line in f.readlines():
        corpus+=[x[:-2] for x in line.split(',') if x[-2:]=='.v']
    f.close()
    corpus = [x.strip() for x in corpus]    
    return list(set(corpus))

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
        mean_dist = cf.get_mean_distance(temp_array)
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
    
#distances,word_list = generate_bootstrapped_baseline(dictionary,embeddings_dict,n=20,iterations=414)


#rand_out = generate_bootstrapped_baseline(dictionary,embeddings_dict,n=20,iterations=413)

