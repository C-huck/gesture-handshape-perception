# Systematicity in gesture production, perception may support sign language emergence

- This project explores whether non-signers can extract grammatical information, like transitivity, from silent gesture.
- This project also identifies several visual features that explain how non-signers extract such information

# Contents

1. [Files](#files)
2. [Background](#background)
3. [Method](#method)
4. [Analysis](#analysis)
5. [Results](#results)
6. [Interpretation](#interpretation)
7. [References](#references)

# Background

When communicating in a new medium, like silent gesture, people must adopt novel strategies
to ensure successful communication. It has been argued that initial productions are inconsistent and unstructured, 
with systematicity emerging through interaction and transmission (Motamedi et al., 2019). In support, studies on 
sign language emergence have shown that homesigners, and signers of young and established sign languages 
systematically vary handshape to code transitivity in production, but gesturers do not (Brentari et al., 2017). 
However, perception studies show that non-signers can resolve abstract syntactic-semantic information, like 
distributivity, telicity, and phi-features (Marshall & Morgan, 2015; Strickland et al., 2015; Schlenker & Chemla, 2018) 
from gesture and sign on first exposure, suggesting that some aspects of the visual signal are immediately analyzable. 
Further, the recurrent emergence of handshape as a transitivity marker across unrelated sign languages suggests that 
this strategy is systematic. To reconcile these disparate findings, we conducted silent gesture production and 
perception experiments. We modeled handshape to uncover specific visual aspects of the signal that may undergird 
transitivity categorization.

# Method

1. video recorded 46 unique events involving the manipulation (transitive) or movement (intransitive) of a variety of objects
2. elicited silent gestures from 6 non-signing participants who depicted these events (6 x 46=276 gestures). 
    - Gestures representing transitive events were considered transitive, otherwise intransitive (inherent transitivity). 
3. collected 20 descriptions of the meanings of these gestures from 95 non-signers on Amazon Mechanical Turk (Turkers; 276 x 20=5,520 sentences; Fig. 1a). 
4. annotated gestures for 6 handshape features, each linked to transitivity marking in sign languages (Fig. 1b). 
5. labeled the sentences for transitivity (1=‘transitive’). 
    - A gesture was considered transitive if its proportion of transitive responses was greater than the median
proportion of all transitive responses, otherwise intransitive (perceived transitivity). 
6. ***Analysis 1:*** trained linear support vector classifiers to predict whether a given gesture is inherently in/transitive and 
7. ***Analysis 2:*** trained linear support vector classifiers to predictwhether it is perceived in/transitive. 
8. ***Classification***:
    - used 6-fold leave-one-out paradigm s.t. data were randomly split into 6 partitions, trained on 5 of the partitions and tested on the 6th, producing an accuracy score. 
    - repeated 6 times with each partition was the test set once.
    - computed mean accuracy and compared it against chance using the probability mass function of the binomial distribution. 
    - averaged the weights for each predictor across all 6 folds in each analysis to assess handshape parameter importance.
