# Codebook for Project Data

## Variables

- **image**: Name of the image stimulus

- **mean_subj_recog_pre**: Mean subjective recognition pre-disambiguation (range: 0-1)
- **mean_subj_recog_post**: Mean subjective recognition post-disambiguation (range: 0-1)
- **mean_subj_recog_grey**: Mean subjective recognition for greyscale images (range: 0-1)

- **mean_verb_acc_pre**: Mean verbal accuracy pre-disambiguation (range: 0-1)
- **mean_verb_acc_post**: Mean verbal accuracy post-disambiguation (range: 0-1)
- **mean_verb_acc_grey**: Mean verbal accuracy for greyscale images (range: 0-1)

- **mean_sem_dist_pre**: Mean semantic distance pre-disambiguation (range: 0-1)
- **mean_sem_dist_post**: Mean semantic distance post-disambiguation (range: 0-1)
- **mean_sem_dist_grey**: Mean semantic distance for greyscale images (range: 0-1)

- **diff_mean_subj_recog**: Difference in mean subjective recognition (post - pre)
- **diff_mean_verb_acc**: Difference in mean verbal accuracy (post - pre)
- **diff_mean_sem_dist**: Difference in mean semantic distance (post - pre)

- **gray_semantic_entropy**: Semantic entropy for greyscale images
- **post_semantic_entropy**: Semantic entropy post-disambiguation
- **pre_semantic_entropy**: Semantic entropy pre-disambiguation

- **info_gain_entropy**: Information gain in entropy from pre- to post-disambiguation
- **info_gain_sem_dist**: Information gain in semantic distance from pre- to post-disambiguation
- **info_gain_sem_dist_gray**: Information gain in semantic distance from pre-disambiguation to greyscale
- **info_gain_entropy_gray**: Information gain based in entropy from pre-disambiguation to greyscale

---

## Definitions

- **Semantic distance**: A measure of how distant two concepts are in a given semantic space, using [openly available semantic embeddings](https://osf.io/jum2f/) derived from large text corpora. Low semantic distance means that participant-provided labels were close in semantic space to the target label, i.e. donkey and horse.
- **Entropy**: A measure of variability in the set of labels used to describe an image, considering the amount and frequencies of different guesses. Low entropy means participants used a small and consistent set of labels to descirbe an image.
- **Information gain**: The reduction in semantic distance or uncertainty (entropy) after exposure to a stimulus, i.e. the greyscale image.