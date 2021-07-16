# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:11:31 2021

@author: Jack
"""

#IMPORT STATEMENTS
import pandas as pd
import common_functions as cf
import generate_random_verbs as grv
from video_rename import ren_key
from scipy.stats import ttest_ind
import numpy as np

#LOAD EMBEDDINGS DICTIONARY, FRAMENET WORD LIST
cf.init()

#LOAD ACTION PERCEPTION DATA
df_action = pd.read_csv("action_label.csv",header=0,converters={'verb': eval}).dropna()
df_action['verb'] = [','.join(x) for x in df_action['verb']]

#LOAD GESTURE PERCEPTION DATA
columns = ["Input.field_1","Answer.sentence","verb","transitivity","RequesterFeedback","DELETE","WorkerId"]
df_csv = pd.read_csv("C:/Users/Jack/ud120-projects/transparency-project-cc-pn/CLS/data_final.csv",header=0,usecols=columns)
df_csv = df_csv[df_csv['RequesterFeedback'].isna()].drop(columns=['RequesterFeedback'])
df_csv = df_csv[df_csv['DELETE']!=1].drop(columns=['DELETE'])
df_csv = df_csv.rename(columns={'Input.field_1':'item','Answer.sentence':'sentence'}).dropna()
df_csv['event'],df_csv['participant'] = cf.rename_item_names(df_csv,ren_key)



#PROCESS ACTION PERCEPTION DATA, COMPUTE INTER-SIMILARITY
df_scores_action = pd.DataFrame(data=cf.get_all_scores(df_action),columns=["item","transitivity",'sdi','embedding_score'])
df_scores_action['participant'] = 'la'

#PROCESS GESTUREE PERCEPTION DATA, COMPUTE INTER-SIMILARITY
df_scores_gesture = pd.DataFrame(data=cf.get_all_scores(df_csv),columns=["item","transitivity",'sdi','embedding_score'])

#COMPUTE INTER(SELF)-SIMILARITY, RANDOM VERBS

#TO-DO

#COMPARE INTRA-SIMILARITY, ACTION-GESTURE VERBS
action_gesture = np.array(cf.comp_all_action_gesture(df_action,df_csv))

#COMPARE INTRA-SIMILARITY, ACTION-RANDOM VERBS
action_random = np.array(cf.comp_all_action_random(df_action))

###STATISTICAL ANALYSIS

#COMPARE ACTION INTER-SIMILARITY WITH GESTURE INTER-SIMILARITY
ttest_ind(df_scores_action['embedding_score'],df_scores_gesture['embedding_score'],equal_var=False,nan_policy='omit')

#COMPARE GESTURE INTER-SIMILARITY WITH RANDOM INTER-SIMILARITY
ttest_ind(df_scores_gesture['embedding_score'],df_scores_gesture['embedding_score'],equal_var=False,nan_policy='omit')

#COMPARE ACTION-GESTURE SIMILARITY WITH ACTION-RANDOM SIMILARITY

#TO-DO

###PLOTTING

#TO-DO