# Description of Variables in the CSV File

## Overview
This document provides detailed descriptions of the variables in the dataset, explaining their meanings and how they were derived. The dataset contains various metrics related to subjective recognition, verbal accuracy, semantic distance, and entropy across different exposure conditions.

## Exposure Conditions
- **Pre-disambiguation:** First presentation of the Mooney image before the participant has seen the corresponding greyscale version.
- **Greyscale:** The disambiguation image (clear version of the Mooney image).
- **Post-disambiguation:** Second presentation of the Mooney image after the participant has seen the corresponding greyscale version.

## Variables
### Identification Variables
- **image:** The name or identifier of the image used in the experiment.

### Subjective Recognition (mean_subj_recog)
- Mean percentage of subjectively recognized images across participants separately for all exposure conditions.

### Verbal Accuracy (mean_verb_acc)
- Proportion of correct verbal labels provided by participants separately for all exposure conditions.
- A provided label is considered correct if it matches the target label or one of its pre-defined synonyms (semantic distance = 0).

### Semantic Distance (mean_sem_dist)
- Average semantic distance of participant-provided labels from the correct label separately for all exposure conditions.
- Semantic distance is defined as the distance in semantic space. For this, we used [openly available semantic embeddings](https://osf.io/jum2f/) derived from large text corpora.
- Low semantic distance means that participant-provided labels were close in semantic space to the target label (including synonyms), i.e. donkey and horse.

### Semantic Entropy (semantic_entropy)
- Average semantic entropy of participant-provided labels separately for all exposure conditions.
- Entropy is defined as the variability in the set of labels used, considering the amount and frequencies of different guesses.
- Low entropy means participants used a small and consistent set of labels to descirbe an image.

### Difference Variables (Post - Pre)
- **diff_mean_subj_recog:** Difference in subjective recognition between post- to pre-disambiguation.
- **diff_mean_verb_acc:** Difference in verbal accuracy between post- to pre-disambiguation.
- **diff_mean_sem_dist:** Difference in semantic distance between post- to pre-disambiguation.

### Information Gain (Pre - Post)
- **info_gain_entropy:** Change in semantic entropy from pre- to post-disambiguation.
- **info_gain_sem_dist:** Change in semantic distance from pre- to post-disambiguation (inverse diff_mean_sem_dist).
- **info_gain_sem_dist_gray:** Change in semantic distance from pre- to greyscale.
- **info_gain_entropy_gray:** Change in semantic entropy from pre- to greyscale.
