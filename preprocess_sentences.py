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


def check_for_stop_verbs(inList):
    compList = ['need','want','should','can','signal','say','advise','watch',
                'show','point','instruct','pretend','try','attempt','plan',
                'begin','start','stop','continue','decide','fail','direct',
                'have']
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
        #if len(out) == len_out:
        #    out.append(find_verb_WN(sentence)[0])
        #    len_out = len(out)
    out = check_for_stop_verbs(out)
    return out


