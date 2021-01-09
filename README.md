# Measuring encyclopedic and grammatical content in silent gesture

Precis:
  - Do participants with no sign language experience can detect whether silent gestures represent transitive or intransitive events?
  - How accurate as non-signing participants at guessing the encyclopedic content of silent gestures?
  - Conducted a silent-gesture labeling experiment; 20 sentences for each of 413 videos of transitive/intransitive event denoting silent gestures
  - Initial analysis suggests:
    - transitivity is transparent: non-signers are accurate at guessing the transitivity of silent gestures
    - non-signer transitivity judgments can be predicted by the visual characteristics of the silent gestures
    - the encyclopedic content of silent gesture is not as ambiguous, even as 

Method:
  - Generated 413 verbal silent gestures from 6 participants, describing 69 unique in/transitive events
  - Annotated the videos for handshape features
  - Collected 20 sentences for each of 413 videos on Amazon Mechanical Turk
  - Annotated sentences for transitivity
  - Extracted the main verb
  - Calculated:
    - Mean transitivity of sentences elicited from a gesture (*perceived transitivity score*; 0--1)
    - Shannon Diversity Index/H-index of verbs elicited from a gesture, following Sehyr & Emmorey, DATE, *Journal*.
    - Mean path similarity score of verbs elicited from a gesture
    - Mean semantic distance of verbs elicited from a gesture
  
  
# Files
 - `data.csv`: Raw data file containing the title of the gesture video, the inherent transitivity of the gesture video ('1' = transitive), the subject code for the gesturer, the subject code for the AMT respondent, a sentence describing the gesture, the main verb of the sentence, and the transitivity of the sentence
 - `data_processed.csv`: Summary data, including the item, its mean transitivity score, SDI/H-index, handshape characteristics, etc.
 
# To do
- [ ] Uplouad .py file that generates `data_processed.csv`
- [ ] Upload main analysis script
