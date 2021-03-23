# Measuring encyclopedic and grammatical content in silent gesture

Précis:
  - **Background:** 
  - **Q1:** (a) Can participants with no sign language experience detect whether silent gestures represent transitive (*I bounced a ball*) or intransitive (*The ball bounced*) events? (b) Do visual characteristics of the gestures guide non-signer's perception of transitivity?; See "/gesture-transitivity-project"
  - **Q2:** How accurate are non-signing participants at guessing the encyclopedic content of silent gestures? See "/gesture-meaning-project"
  - **Method:** 
    - Conducted (1) live action vignette and (2) silent-gesture labeling experiments on Amazon Mechanical Turker
    - Collected 20-30 sentences describing (a) 69 live action events and (b) gestures depicting those events (69 events * 6 gesturers = 414 gestures)
  - **Analysis:** 
    -  Q1: (a) Sentences were hand-annotated for transitivity. A gesture video was considered 'transitive' if it received >10 transitive labels, otherwise intransitive. 
  - **Results**:
    - transitivity is transparent: non-signers are 86% accurate at guessing the transitivity of silent gestures
    - non-signer transitivity judgments can be predicted by the visual characteristics of the silent gestures
    - the encyclopedic content of silent gesture is not as ambiguous as previously assumed
  
# Files
 - `preprocess_sentences.py`: Takes `data.csv` as input and (a) annonymizes MTurk WorkerIds, (b) removes errant responses/rejected work, (c) renames filenames to human-readable formats, (d) and automatically extracts the verb(s) from each response sentence.
 - `video_rename.py`: A file containing the key translating between obscurred and human-readable file names. File names were obscurred in experiment so Turkers could not use the file name (e.g., *balloon-deflate-np-IN.mp4*) to guess the meaning of the gesture.
 - `data.csv`: Input to `preprocess_sentences.py`. Raw data file containing the title of the gesture video, the inherent transitivity of the gesture video ('1' = transitive), the subject code for the gesturer, the subject code for the AMT respondent, a sentence describing the gesture, the main verb(s) of the sentence, and the transitivity of the sentence The main verb(s) of each response sentences were identified using `preprocess_data.py` with some manual cleanup. Transitivity was coded by hand. 
 - `data_processed.csv`: Summary data, including the item, its mean transitivity score, SDI/H-index, handshape characteristics, etc.
 
# To do
- [ ] Upload .py file that generates `data_processed.csv`
- [ ] Upload main analysis scripts
