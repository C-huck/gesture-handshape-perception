# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:30:16 2021

@author: Chuck
"""
#IMPORT STATEMENTS
import generate_random_verbs as grv
from itertools import product,combinations
from spellchecker import SpellChecker 
from collections import Counter
import numpy as np
from scipy import spatial

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

def sdi(data):
    """ Given a hash { 'species': count } , returns the SDI
    
    >>> sdi({'a': 10, 'b': 20, 'c': 30,})
    1.0114042647073518"""
    
    from math import log as ln
    
    def p(n, N):
        """ Relative abundance """
        if n ==  0:
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
            
    N = sum(data.values())
    
    return -sum(p(n, N) for n in data.values() if n != 0)

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
    return np.nanmean([get_distance(embedding_samples[x[0]],embedding_samples[x[1]]) for x in iters])

def get_all_scores(df):   
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    res = []
    spell = SpellChecker()
    for x in set(df['item']):
        temp = df[df['item']==x]
        word_list = [x.split(',') for x in list(temp['verb'])]
        word_list = list(flatten(word_list))
        count_temp = Counter(word_list) #for SDI
        avg = np.mean(temp['transitivity']) #for transitivity score
        word_list = [spell.correction(word) for word in word_list]
        word_list = [embeddings_dict[word] for word in word_list if word in embeddings_dict.keys()]
        res.append([x,round(avg,4),sdi(count_temp),get_mean_distance(word_list)])
    return res

def comp_all_action_random(df):
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    final_mean = []
    for z in set(df['item']):
        temp = df[df['item']==z]
        word_list = [x.split(',') for x in list(temp['verb'])]
        word_list = list(flatten(word_list))
        spell = SpellChecker()
        word_list = [spell.correction(word) for word in word_list]
        comp_list = comp_action_random(word_list)
        item_mean = []
        for x in comp_list:
            mean = []
            for y in x[1]:
                tempo = get_distance(embeddings_dict[x[0]],embeddings_dict[y])
                mean.append(tempo)
            item_mean.append(np.mean(mean))
        final_mean.append([z,np.mean(item_mean)])
    return final_mean
    

def comp_action_random(list1):
    list2 = grv.generate_bootstrapped_baseline(dictionary,embeddings_dict,n=20,iterations=1)[1]
    return list(product(list1,list2))

def rename_item_names(df,key):
    """
    From ##-participant-TR/IN-s.mp4 to EVENT-PART-IN/TR.mp4

    """
    new_names = []
    participants = []
    for index,row in df.iterrows():
        for x in key:
            if str(x[1]) == row['item'][:2]:
                new_name = x[0]
                new_names.append(new_name)
                participants.append(row['item'][3:5])
            elif str(x[1])+'-' == row['item'][:2]:
                new_name = x[0]
                new_names.append(new_name)
                participants.append(row['item'][2:4])
    return new_names,participants

def comp_all_action_gesture(df1,df2):
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    spell = SpellChecker()
    mean_distance_subj = []
    for x in set(df1['item']):
        temp1 = df1[df1['item']==x]
        word_list1 =  [a.split(',') for a in list(temp1['verb'])]
        word_list1 = list(flatten(word_list1))
        word_list1 = [spell.correction(word) for word in word_list1]
        temp2 = df2[df2['event']==x]
        for y in ['cm','cm','ho','ip','np','rv']:
            temp2_2 = temp2[temp2['participant']==y]
            word_list2 =  [z.split(',') for z in list(temp2_2['verb'])]
            word_list2 = list(flatten(word_list2))
            word_list2 = [spell.correction(word) for word in word_list2]
            final_list = list(product(word_list1,word_list2))
            distances = []
            for b in final_list:
                try:
                    distance = get_distance(embeddings_dict[b[0]],embeddings_dict[b[1]])
                    distances.append(distance)
                except:
                    print(b[0],b[1])
                    continue
            mean_distance_subj.append([x+'-'+y,np.nanmean(distances)])
    return mean_distance_subj

def init():
    global embeddings_dict
    global dictionary
    embeddings_dict = load_embeddings("C:/Users/Jack/ud120-projects/GloVe-master/glove.6B/glove.6B.300d.txt")
    dictionary = grv.load_relevant_verbs()
    return embeddings_dict,dictionary


