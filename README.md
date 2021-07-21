# Measuring encyclopedic and grammatical content in silent gesture

This project investigates different types of information that are available in silent gesutre (or not) and contributes to our understanding of how meaning is negotiated in novel communication settings (e.g., newly deafened or language-impaired individuals, emerging sign languages).

Tools used:
- SpaCy
- GloVe
- NLTK/WordNet
- Scikit-learn

## Contents

1. [To-do](#to-do)
2. [Files](#files)
3. [Background](#background)
4. [Method](#general-methods)
5. [Analysis](#general-analyses)
6. [Results](#results)
7. [Output](#output)

## To-do:

- [ ] Gesture meaning project
  - [ ] Clean up `common_functions.py` : Eliminate redundancies in `comp_all_X` functions 
- [ ] Transitivity project
  - [ ] Create README
  - [ ] Write abstract, post plots
  - [ ] Upload analysis scripts

## Files:
 - `generate_summary_data.py`: Outputs summary data for live action videos and gesture videos.  For each gesture or action vignette, computes the proportion of transitive sentences used to describe it, and three measures of semantic similarity: the diversity of verbs used (via Shannon's Diversity Index/H-Index), the Euclidean Distance of each verb's 300d representation vectors, and the mean cosine similarity of the sentences used, etc. 
 - `preprocess_sentences.py`: Takes `data.csv` as input and (a) annonymizes MTurk WorkerIds, (b) removes errant responses/rejected work, (c) renames filenames to human-readable formats, (d) and automatically extracts the verb(s) from each response sentence.
 - `video_rename.py`: A file containing the key translating between obscurred and human-readable file names. File names were obscurred in experiment so Turkers could not use the file name (e.g., *balloon-deflate-np-IN.mp4*) to guess the meaning of the gesture.
 - `data.csv`: Input to `preprocess_sentences.py`. Raw data file containing the title of the gesture video, the inherent transitivity of the gesture video ('1' = transitive), the subject code for the gesturer, the subject code for the AMT respondent, a sentence describing the gesture, the main verb(s) of the sentence, and the transitivity of the sentence The main verb(s) of each response sentences were identified using `preprocess_data.py` with some manual cleanup. Transitivity was coded by hand. 
 - `gesture_summary_data.csv` and `action_summary_data.csv`: Output of `generate_summary_data.py`. Summary data for sentences elicited from gesture videos and live action videos. Includes: the item, its mean transitivity score, SDI/H-index, etc. Gesture summary also contains phonetic characteristics of gestures.

## Background:

### Information sources in language
- Speech contains a wealth of information, each conveyed in different channels: 
  - sequences of sounds identify words
  - accents and pitch identify speaker identity (e.g., female, Irish speakers of English)
  - intonation conveys force (question, statement, command, etc.) and emotional state
- Research on sign languages have similarly identified different channels where distinct information can be found:
  - Hands convey signs/words (signs are differentiated by handshape, location, orientation of palms, etc.)
  - Facial expressions convey force (questions, statements, etc.), sentence boundaries (e.g., like periods in written English), etc. 
- Gesture also contains a wealth of information, but researchers are only just beginning to identify sources of information and provide them a linguistic description

### Information sources in gesture, perception
- Previous research has shown that people unfamiliar with a sign language, aka non-signers, are good at resolving grammatical information about signs and gestures
- But, non-signers are bad at guessing the "dictionary" meaning of signs
- For example, non-signers can guess whether the events verb signs denote have natural semantic endpoints, irrespective of their ability to guess what the sign means:
   - FYI: This phenomenon in language is called *telicity*. e.g., *The flower wilted* has an endpoint/is telic (*The flower is completely wilted*), but *The flower grew* does not/is atelic (*?The flower completely grew*). 
  -  For example, non-signers usually can't guess that the sign DECIDE (Fig 1, left) means *to decide* or THINK (Fig 1, right) mean *to think*, but they know that the former has a natural semantic endpoint while the latter does not
- One interesting finding from this study was that non-signers associated gestural boundaries (e.g., the hands' sharp deceleration towards a point in space) with the existence of a natural semantic boundary  
- The current project instead focuses on how "dictionary" meaning and *argument structure* are conveyed in silent gesture, and how they are perceived 
  - *argument structure* refers to how many nouns a verb takes. If a verb takes only one noun, it's intransitive (*The ball bounced*). If it takes two, it's transitive (*I bounced a ball*) 

![Figure from https://doi.org/10.1073/pnas.1423080112](https://c-huck.github.io/images/F2large.jpg)
**Figure 1:** (Left) Verb DECIDE in American Sign Language; (right) Verb THINK-OVER in American Sign Language. Non-signers are not able to guess the meaning of the signs, but they can tell that DECIDE has a natural semantic endpoint, but THINK-OVER does not. Figure obtained from https://doi.org/10.1073/pnas.1423080112.

### Research Questions
- **Q1:** (a) Can participants with no sign language experience detect whether silent gestures represent transitive or intransitive events? (b) Do visual characteristics of the gestures guide non-signer's perception of transitivity?; See `/gesture-transitivity-project`
- **Q2:** How accurate are non-signing participants at guessing the encyclopedic content of silent gestures? See `/gesture-meaning-project`


## General methods:
- Collected 414 silent gestures from 6 non-signers depicting 69 events; Annotated these gestures for visual and manual (phonetic) characteristics
- Collected 20-30 sentences describing (a) 69 live action events and (b) the intended meaning of the gestures
  - From these sentences, both a gesture's meaning and perceived transitivity can be deduced: E.g., *The person ate an apple* denotes an event of *eating* with two arguments, *the person* and *an apple* (i.e., the event is transitive).

## General analyses:
***Q1:***
-  Sentences were hand-annotated for transitivity. A gesture video was considered 'transitive' if it received >12 transitive labels, otherwise 'intransitive'. 
-  Use a linear support vector machine to predict 'transitive' or 'intransitive' class of gestures based on its visual/manual/phonetic features (6-fold l-o-o paradigm)

***Q2:***
-  For each event, we computed the mean pair-wise semantic distance (SD) between verbs elicited from action videos (action-verbs), verbs elicited from gesture videos (gesture-verbs), and randomly generate verbs (random-verbs). 
-  Semantic distance was defined as the Euclidean distance between two words' 300d word-representation vectors, obtained from GloVe.
-  We predicted SD(action-verbs,gesture-verbs) >> SD(action-verbs,random-verbs)
 
 ## Results:
- Q1: transitivity is transparent: non-signers are 86% accurate at guessing the transitivity of silent gestures
- Q1: non-signer transitivity judgments can be predicted by the visual characteristics of the silent gestures
- Q2: verbs generated from action videos are significantly more related to verbs generated from gesture videos than to random verbs; the encyclopedic content of silent gesture is not as ambiguous as previously assumed

## Output
For Q1, see [abstract 1](https://c-huck.github.io/pdfs/CUNY2021.pdf) - [abstract 2](https://c-huck.github.io/pdfs/AMLaP_silent_gesture_transitivity.pdf)

For Q2, see [abstract](https://c-huck.github.io/pdfs/AMLaP_silent_gesture_meaning.pdf)
