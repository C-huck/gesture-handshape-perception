# Measuring encyclopedic and grammatical content in silent gesture

This project investigates different types of information that are available in silent gesutre (or not) and contributes to our understanding of how meaning is negotiated in novel communication settings (e.g., newly deafened or language-impaired individuals, emerging sign languages).

Tools used:
- SpaCy
- GloVe
- NLTK/WordNet
- Scikit-learn

**Background:**
- People unfamiliar with a sign language, aka non-signers, are good at resolving grammatical information about signs, like whether the events they denote have natural semantic endpoints:
  -  This phenomenon in language is called *telicity*. e.g., *The flower wilted* has an endpoint/is telic (*The flower is completely wilted*), but *The flower grew* does not/is atelic (*?The flower completely grew*). 
-  But, non-signers are bad at guessing the encyclopedic content (=meaning) of signs
  -  e.g., Non-signers usually can't guess that the sign DECIDE (Fig 1, left) means *to decide* or THINK (Fig 1, right) mean *to think*, but they know that the former has a natural semantic endpoint while the latter does not
- This project focuses on how meaning and *argument structure* are conveyed in silent gesture, and how they are perceived 
  - *argument structure* refers to how many nouns a verb takes. If a verb takes only one noun, it's intransitive (*The ball bounced*). If it takes two, it's transitive (*I bounced a ball*) 
- Previous work on argument structure in silent gesture has demonstrated that non-signers manipulate the shape of their hands to distinguish between transitive and intransitive verbs
  - These studies do not generalize, as they looked at only a few verbs 
- Previous work has shown that non-signers are better at guessing the meaning of gestures that other non-signers produce
  - These studies adopt a strict definition of accuracy, however, such that if the gesture means *to hammer* and a non-signer thinks it means *to pound*, the guess was marked as incorrect.
- **Q1:** (a) Can participants with no sign language experience detect whether silent gestures represent transitive or intransitive events? (b) Do visual characteristics of the gestures guide non-signer's perception of transitivity?; See `/gesture-transitivity-project`
- **Q2:** How accurate are non-signing participants at guessing the encyclopedic content of silent gestures? See `/gesture-meaning-project`

![Figure from https://doi.org/10.1073/pnas.1423080112](https://c-huck.github.io/images/F2large.jpg)
**Figure 1:** (Left) Verb DECIDE in American Sign Language; (right) Verb THINK-OVER in American Sign Language. Non-signers are not able to guess the meaning of the signs, but they can tell that DECIDE has a natural semantic endpoint, but THINK-OVER does not. Figure obtained from https://doi.org/10.1073/pnas.1423080112.

**Method:** 
- Collected 414 silent gestures from 6 non-signers depicting 69 events; Annotated these gestures for visual and manual (phonetic) characteristics
- Collected 20-30 sentences describing (a) 69 live action events and (b) the intended meaning of the gestures 

**Analysis:** 
-  Q1:
  -  Sentences were hand-annotated for transitivity. A gesture video was considered 'transitive' if it received >12 transitive labels, otherwise 'intransitive'. 
  -  Use a linear support vector machine to predict 'transitive' or 'intransitive' class of gestures based on its visual/manual/phonetic features (6-fold l-o-o paradigm)
- Q2:
  -  For each event, we computed the mean pair-wise semantic distance (SD) between verbs elicited from action videos (action-verbs), verbs elicited from gesture videos (gesture-verbs), and randomly generate verbs (random-verbs). 
  -  Semantic distance was defined as the Euclidean distance between two words' 300d word-representation vectors, obtained from GloVe.
  -  We predicted SD(action-verbs,gesture-verbs) >> SD(action-verbs,random-verbs)
 
 **Results**:
- Q1: transitivity is transparent: non-signers are 86% accurate at guessing the transitivity of silent gestures
- Q1: non-signer transitivity judgments can be predicted by the visual characteristics of the silent gestures
- Q2: verbs generated from action videos are significantly more related to verbs generated from gesture videos than to random verbs; the encyclopedic content of silent gesture is not as ambiguous as previously assumed

# Files
 - `generate_summary_data.py`: Outputs summary data for live action videos and gesture videos.  For each gesture or action vignette, computes the proportion of transitive sentences used to describe it, and three measures of semantic similarity: the diversity of verbs used (via Shannon's Diversity Index/H-Index), the Euclidean Distance of each verb's 300d representation vectors, and the mean cosine similarity of the sentences used, etc. 
 - `preprocess_sentences.py`: Takes `data.csv` as input and (a) annonymizes MTurk WorkerIds, (b) removes errant responses/rejected work, (c) renames filenames to human-readable formats, (d) and automatically extracts the verb(s) from each response sentence.
 - `video_rename.py`: A file containing the key translating between obscurred and human-readable file names. File names were obscurred in experiment so Turkers could not use the file name (e.g., *balloon-deflate-np-IN.mp4*) to guess the meaning of the gesture.
 - `data.csv`: Input to `preprocess_sentences.py`. Raw data file containing the title of the gesture video, the inherent transitivity of the gesture video ('1' = transitive), the subject code for the gesturer, the subject code for the AMT respondent, a sentence describing the gesture, the main verb(s) of the sentence, and the transitivity of the sentence The main verb(s) of each response sentences were identified using `preprocess_data.py` with some manual cleanup. Transitivity was coded by hand. 
 - `gesture_summary_data.csv` and `action_summary_data.csv`: Output of `generate_summary_data.py`. Summary data for sentences elicited from gesture videos and live action videos. Includes: the item, its mean transitivity score, SDI/H-index, etc. Gesture summary also contains phonetic characteristics of gestures.

# Output
For Q1, see [abstract 1](https://c-huck.github.io/pdfs/CUNY2021.pdf) - [abstract 2](https://c-huck.github.io/pdfs/AMLaP_silent_gesture_transitivity.pdf)

For Q2, see [abstract](https://c-huck.github.io/pdfs/AMLaP_silent_gesture_meaning.pdf)
