# Transparency of encyclopedic content of silent gesture

Project explores what range(s) of interpretations silent gestures are perceived to have. 

![Experimental design](images/experimental_design_meaning.png)

# Background

Gesture contains a wealth of imagistic, yet vague information. Studies show that
non-signers are poor at determining the encyclopedic content of gestures (van Nispen et al.,
2017) and signs from natural sign languages (Sehyr & Emmorey, 2019). This calls into question
how shared interpretations are established in novel communicative settings (e.g., an emerging
sign system). However, these studies adopted a strict definition of ‘accuracy,’ where a guess
and the gloss of the sign/gesture must be string identical (e.g., ‘brush’ and ‘comb’ are not a
match). We argue that this underestimates the information contained within the signal by not
taking into consideration the similarity between guess and gloss. To this end, we conducted
action- and silent gesturing-labeling experiments, and compared the similarity of labels using a
computational approach to semantic similarity, focusing on verb usage specifically. We show
that (a) non-signing participants converge on a certain range of interpretations when assigning
meaning to gestures, and (b) these interpretations are semantically similar to the actions the
gestures represent.

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

# References

Emmorey, K. (2014). Iconicity as structure mapping. Philosophical Transactions of the Royal Society B,
369(1651), 20130301.

Ortega, G., & Özyürek, A. (2020). Types of iconicity and combinatorial strategies distinguish semantic
categories in silent gesture across cultures. Language and Cognition, 12(1), 84–113.

Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global vectors for word representation. In
Empirical methods in natural language processing (emnlp) (pp. 1532–1543).

Sehyr, Z. S., & Emmorey, K. (2019). The perceived mapping between form and meaning in ASL depends
on linguistic knowledge and task. Language and Cognition, 11(2), 208–234.

Taub, S. F. (2001). Language from the body: Iconicity and metaphor in American Sign Language.
Cambridge: Cambridge University Press.

van Nispen, K., van de Sandt-Koenderman, W. M. E., & Krahmer, E. (2017). Production and comprehension of pantomimes used to depict objects. Frontiers in Psychology, 8, 1095
