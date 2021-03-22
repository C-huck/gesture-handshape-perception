import pandas as pd
from video_rename import ren_key

import re
from spellchecker import SpellChecker
from  nltk import word_tokenize,pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

import spacy
nlp = spacy.load("en_core_web_lg")

def spellCheck(sentence):
    sc_sentence = ""
    spell = SpellChecker()
    for word in sentence.split():
        new_word = spell.correction(word)
        sc_sentence+=new_word+" "
    return sc_sentence


def check_for_stop_verbs(inList):
    compList = ['need','want','should','can','signal','say','advise','watch',
                'show','point','instruct','pretend','try','attempt','plan',
                'begin','start','stop','continue','decide','fail','direct',
                'have','describe']
    for x in inList:
        if x in compList:
            inList.remove(x)
    return inList

def find_verb_WN(sentence):
    lemmatizer = WordNetLemmatizer() 
    verbs = []
    try:
        sentence = word_tokenize(sentence)
    except:
        print(sentence)
    tagged = pos_tag(sentence)
    for i,x in enumerate(tagged):
        if i == 0:
            continue
        elif len(wn.synsets(x[0],pos='v'))>1 and tagged[i-1][1] not in ['DT','IN','JJ']:
            verb = lemmatizer.lemmatize(x[0],pos='v')
            if verb != 'be':
                verbs.append(verb)
    return verbs

def find_verbs(sentence):
    out = []
    len_out = 0
    sc_sentence = spellCheck(sentence)
    sentences = re.split('and | that',sc_sentence)
    for sentence in sentences:
        sentence_nlp = nlp(sentence)
        for token in sentence_nlp:
            if token.dep_ == 'ROOT' and token.pos_ == 'VERB':
                out.append(token.lemma_)
            elif token.pos_ == 'VERB' and not token.dep_ in ['amod','advcl','acl','pcomp']:
                out.append(token.lemma_)
        if len(out) == len_out:
            out.append(find_verb_WN(sentence))
            len_out = len(out)
    out = check_for_stop_verbs(out)
    return out

def get_verb_from_sentence(df):
    verb_list = []
    for i,row in df.iterrows():
        result = find_verbs(row['sentence'])
        verb_list.append(result)
        if i % 100 == 0:
            print(i,len(df))
    return verb_list

def rename_item_names(df,key):
    """
    From ##-participant-TR/IN-s.mp4 to EVENT-PART-IN/TR.mp4

    """
    new_names = []
    participants = []
    for index,row in df.iterrows():
        for x in key:
            if str(x[1]) == row['Input.field_1'][:2]:
                new_name = x[0]
                new_names.append(new_name)
                participants.append(row['Input.field_1'][3:5])
            elif str(x[1])+'-' == row['Input.field_1'][:2]:
                new_name = x[0]
                new_names.append(new_name)
                participants.append(row['Input.field_1'][2:4])
    return new_names,participants

def generate_unique_subj_ID(df):
    a = set(df['WorkerId'])
    anon = []
    for i,row in df.iterrows():
        for x,y in zip(a,range(len(a))):
            if row['WorkerId'] == x:
                anon.append('subj'+str(y))
    return anon
                
##Read in csv
#NB: For privacy, uploaded CSV will not have column "WorkerId"
#NB: Sentence transitivity was marked by hand
columns = ["Input.field_1","Answer.sentence","RequesterFeedback","DELETE","WorkerId","transitivity"]
df = pd.read_csv("data_final.csv",header=0,usecols=columns)

##Remove rejected work, pre-screened non-compliant items
df = df[df['RequesterFeedback'].isna()].drop(columns=['RequesterFeedback'])
df = df[df['DELETE']!=1].drop(columns=['DELETE'])

##Rename items to be human readable
df['item'],df['participant'] = rename_item_names(df,ren_key)

##Generate anonymized subject IDs
df['subjID'] = generate_unique_subj_ID(df)

##Clean up DF
df = df.rename(columns={'Answer.sentence':'sentence'})
df.drop(columns=['WorkerId','Input.field_1'],inplace=True)

##Find target verb in each response sentence
df['verb'] = get_verb_from_sentence(df)
