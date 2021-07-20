# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:11:31 2021

@author: Chuck
"""

#IMPORT STATEMENTS
import pandas as pd
import common_functions as cf
import generate_random_verbs as grv
from video_rename import ren_key
from scipy.stats import ttest_ind
import numpy as np

#LOAD EMBEDDINGS DICTIONARY, FRAMENET WORD LIST
embeddings_dict,dictionary = cf.init()

#LOAD ACTION PERCEPTION DATA
df_action = pd.read_csv("action_label.csv",header=0,converters={'verb': eval}).dropna()
df_action['verb'] = [','.join(x) for x in df_action['verb']]

#LOAD GESTURE PERCEPTION DATA
columns = ["Input.field_1","Answer.sentence","verb","RequesterFeedback","DELETE",'transitivity']
df_gesture = pd.read_csv("C:/Users/Jack/ud120-projects/transparency-project-cc-pn/CLS/data_final.csv",header=0,usecols=columns)
df_gesture = df_gesture[df_gesture['RequesterFeedback'].isna()].drop(columns=['RequesterFeedback'])
df_gesture = df_gesture[df_gesture['DELETE']!=1].drop(columns=['DELETE'])
df_gesture = df_gesture.rename(columns={'Input.field_1':'item','Answer.sentence':'sentence'}).dropna()
df_gesture['event'],df_gesture['participant'] = cf.rename_item_names(df_gesture,ren_key)

#GENERATE RANDOM WORD LISTS, COMPUTE INTER(SELF)-SIMILARITY
random_vec,random_words,bool_vec=grv.generate_bootstrapped_baseline(dictionary,embeddings_dict,n=20,iterations=413,seed=1)

df_random = pd.DataFrame(data=random_vec,columns=['embedding_score'])
df_random['participant'] = 'rand'

#PROCESS ACTION PERCEPTION DATA, COMPUTE INTER-SIMILARITY
df_scores_action = pd.DataFrame(data=cf.get_all_scores(df_action),columns=["item","transitivity",'sdi','embedding_score'])
df_scores_action['participant'] = 'la'
df_scores_action['inherent_transitivity'] = [1 if 'TR' in x else 0 for x in df_scores_action['item']] #for subsequent analysis

#PROCESS GESTUREE PERCEPTION DATA, COMPUTE INTER-SIMILARITY
df_scores_gesture = pd.DataFrame(data=cf.get_all_scores(df_gesture),columns=["item","transitivity",'sdi','embedding_score'])
df_scores_gesture['inherent_transitivity'] = [1 if 'TR' in x else 0 for x in df_scores_gesture['item']]
df_scores_gesture['participant'] = 'gesture'
df_scores_gesture['inherent_transitivity'].sum()/len(df_scores_gesture['inherent_transitivity']) #for subsequent analysis

#COMPARE INTRA-SIMILARITY, ACTION-GESTURE VERBS
action_gesture = np.array(cf.comp_all_action_gesture(df_action,df_gesture))

#COMPARE INTRA-SIMILARITY, ACTION-RANDOM VERBS
action_random = np.array(cf.comp_all_action_random(df_action))

###STATISTICAL ANALYSIS

#COMPARE ACTION INTER-SIMILARITY WITH GESTURE INTER-SIMILARITY
ttest_ind(df_scores_action['embedding_score'],df_scores_gesture['embedding_score'],equal_var=False,nan_policy='omit')

#COMPARE GESTURE INTER-SIMILARITY WITH RANDOM INTER-SIMILARITY
ttest_ind(df_scores_gesture['embedding_score'],random_vec,equal_var=False,nan_policy='omit')

#COMPARE ACTION-GESTURE SIMILARITY WITH ACTION-RANDOM SIMILARITY
ttest_ind(action_random[:,1].astype(float),action_gesture[:,1].astype(float),equal_var=False,nan_policy='omit')

###PLOTTING

import seaborn as sns
import matplotlib.pyplot as plt

###INTER(SELF)-SIMILARITY PLOT
df_plotting = pd.concat([df_scores_action[['embedding_score','participant']],df_scores_gesture[['embedding_score','participant']]])
rand_max,rand_min,rand_mean = max(random_vec),min(random_vec),np.mean(random_vec)
sns.catplot(x='participant',y='embedding_score',data=df_plotting,kind='box')
plt.axhline(y=rand_mean,linewidth=2, color='r')
plt.axhspan(rand_max, rand_min, facecolor='r', alpha=0.25)
plt.ylim(0,10)
plt.ylabel('Semantic Distance')
plt.xticks([0,1],['Live action','Gesture'])
plt.xlabel('')
plt.show()

###INTRA-SIMILARITY PLOT
df_plotting = pd.DataFrame(data=action_gesture[:,1].astype(float),columns=['embedding_score'])
sns.catplot(y='embedding_score',data=df_plotting,kind='box')
rand_max,rand_min,rand_mean = max(action_random[:,1].astype(float)),min(action_random[:,1].astype(float)),np.mean(action_random[:,1].astype(float))
sns.catplot(y='embedding_score',data=df_plotting,kind='box')
plt.axhline(y=rand_mean,linewidth=2, color='r')
plt.axhspan(rand_max, rand_min, facecolor='r', alpha=0.25)
plt.ylim(0,10)
plt.ylabel('Semantic Distance')
plt.xticks([0],['Action-Gesture Similarity'])
plt.xlabel('')
plt.show()
