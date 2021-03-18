# Transparency of encyclopedic content of silent gesture

Project explores what range(s) of interpretations silent gestures are perceived to have. 

![Experimental design](images/experimental_design_meaning.png)

# Method

1. Produced vignettes of 69 unique events (e.g., *break, walk, hammer*).
2. Elicited silent gestures of these vignettes from 6 non-signing participants (6 * 69 = 413 silent gestures, with one gesture discarded). 
3. For each action vignette, elicited 30 one-sentence descriptions of the action on Amazon Mechanical Turk
4. For each silent gesture, we elicited 20 one-sentence descriptions of what the gesture intended to convey on AMT 
5. Extracted the verbs from the sentences (`get-verb.py`) and scored them according to their Semantic Distance (SD). 
6. Semantic Distance was calculated as the average pairwise euclidean distance between each verb’s 300-dimensional word-representation vector within a set of verbs (e.g., the set of verbs elicited from a particular action vignette)

# Analysis

## Internal consistency 

1. Compute mean pair-wise SD for (a) every set of action-verbs and (b) every set of gesture-verbs
2. 

## Consistency between action-verbs and gesture-verbs

1. Compute mean pair-wise SD for action-verbs with gesture-verbs
