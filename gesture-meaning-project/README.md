# Transparency of encyclopedic content of silent gesture

Project explores what range(s) of interpretations silent gestures are perceived to have. 

# Contents

1. [Files](#files)
2. [Background](#background)
3. [Method](#method)
4. [Analysis](#analysis)
5. [Results](#results)
6. [Interpretation](#interpretation)
7. [References](#references)

# Files

- `action_label.csv` : Cleaned data from live action labeling experiment
- `common_functions.py` : functions used to 
- `gesture_label.csv` : Cleaned data from gesture labeling experiment
- `generate_random_verbs.py` : functions to generate random baseline for analysis
- `main_analysis.py` : statistical analysis + plotting
- `relevant-fram...LUs.txt ` : semi-structure list of action concepts from FrameNet. Used in generation of random baseline.

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
3. For each action vignette, elicited 30 one-sentence descriptions of the action on Amazon Mechanical Turk (Fig. 1, left)
4. For each silent gesture, we elicited 20 one-sentence descriptions of what the gesture intended to convey on AMT (Fig. 1, right)
5. Extracted and spell-checked the verbs from the sentences (`get-verb.py`)
6. Computed Semantic Distance between verbs
    - e.g., the verbs in the set {eat, dine, drink} are more similar to each other than {eat, think, drip}, which can be represented numerically (i.e., SD(eat, dine, drink) < SD(eat, think, drip)).
7. Specifically, we obtained 300-dimensional word-representation vectors from GloVe (Pennington et al., 2014)
    - vectors characterize words based on their co-occurrence with other words (within Common Crawl dataset).
8. Semantic Distance was calculated as the average pairwise euclidean distance between each verb's vector
9. Calculate semantically-matched baseline (chance): 
    - compiled a list of 1,015 verbs from FrameNet whose superordinate categories entailed movement (e.g., self motion) or manipulation (e.g., cause impact)
    - randomly drew 20 verbs from this list (with replacement)
    - computed the mean semantic distance, repeating this process 413 times

 ![Experimental design](images/experimental_design_meaning.png) 

**Figure 1:** Experimental design: Turkers annotated live action videos (left) or videos of silent gestures
(right). For each video, verbs were compared for similarity (semantic distance)

# Analysis

***A1: Inter-set (self) similarity:*** 
1. Compute mean pair-wise SD for action verbs, SD(action verbs); 
2. Compute mean pair-wise SD for gesture verbs, SD(gesture verbs); and
3. *Baseline*: Compute mean pair-wise SD for randomly generated verbs, SD(random verbs)

***A2: Intra-set similarity:***
1. Compute SD between action verbs and gesture verbs, SD(action verbs, gesture verbs)
2. *Baseline*: Compute SD between action verbs and random verbs, SD(action verbs, random verbs)

# Results

1. Action verbs were significantly more consistent with each other than gesture verbs (t(481) = -10.27, p<0.001; Fig. 2a).
2. Gesture verbs were more internally consistent than random verbs (t(412) = -39.44, p<0.001; Fig. 2a). 
3. Action verbs were significantly more consistent with gesture verbs than with random verbs (t(488) = -29.97, p<0.001; Fig. 2b).

| ![](https://c-huck.github.io/images/inter_consistency.png) | ![](https://c-huck.github.io/images/intra_consistency.png) |
|:---:|:---:|
| (a) Inter consistency | (b) Intra consistency |

**Figure 2**: Results: **(a)** Verbs produced in response to gesture videos were less similar to each other
than those produced in response to action videos (SD(action verbs) < SD(gesture verbs); M<sub>SD(act)</sub> =
3.96, M<sub>SD(gest)</sub> = 6.25). However, both sets of verbs were more internally consistent than randomly
selected verbs of manipulation or movement (SD(action verbs), SD(gesture verbs) << SD(random verbs);
M<sub>SD(rand)</sub> = 8.65). The red line represents the mean of SD(random verbs), with the min-max range
shaded in pink; **(b)** Verbs produced in response to action videos were more similar to verbs produced
in response to gesture videos than to randomly selected verbs (SD(action videos,gesture verbs)) <<
(SD(action verbs,random verbs); (M<sub>SD(act,gest)</sub> = 5.94, M<sub>SD(act,rand)</sub> = 8.33). The red line represents the
mean of SD(action verbs,random verbs), with the min-max range shaded in pink

# Interpretation

Despite the reported low interpretation accuracy of silent gesture, the present, more nuanced analysis
suggests that non-signers consider only a certain range of interpretations for silent gestures,
and that these interpretations are semantically similar to the actions the gestures represent.
This approach strengthens the hypothesis that gestures are constructed and perceived by way
of shared underlying event representations (van Nispen et al., ibid.) and that there are shared
means of en/decoding these representations (Emmorey, 2014; Taub, 2001).

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
