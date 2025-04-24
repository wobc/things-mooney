# Codebook for THINGS-MOONEY

## Variables

- **image**: Name of the image stimulus

- **subj_ident_pre**: Mean subjective identification pre-disambiguation (range: 0-1)
- **subj_ident_gray**: Mean subjective identification for grayscale images (range: 0-1)
- **subj_ident_post**: Mean subjective identification post-disambiguation (range: 0-1)

- **verbal_acc_pre**: Mean verbal accuracy pre-disambiguation (range: 0-1)
- **verbal_acc_gray**: Mean verbal accuracy for grayscale images (range: 0-1)
- **verbal_acc_post**: Mean verbal accuracy post-disambiguation (range: 0-1)

- **sem_dist_pre**: Mean semantic distance pre-disambiguation (range: 0-1)
- **sem_dist_gray**: Mean semantic distance for grayscale images (range: 0-1)
- **sem_dist_post**: Mean semantic distance post-disambiguation (range: 0-1)

- **sem_entropy_pre**: Semantic entropy pre-disambiguation
- **sem_entropy_gray**: Semantic entropy for grayscale images
- **sem_entropy_post**: Semantic entropy post-disambiguation

- **diff_mean_subj_ident**: Difference in mean subjective identification (post - pre)
- **diff_mean_verbal_acc**: Difference in mean verbal accuracy (post - pre)
- **diff_mean_sem_dist**: Difference in mean semantic distance (post - pre)
- **diff_mean_sem_entropy**: Difference in semantic entropy (post - pre)

- **info_gain_sem_dist**: Information gain in semantic distance from pre- to post-disambiguation (inverted diff_mean_sem_dist)
- **info_gain_entropy**: Information gain in entropy from pre- to post-disambiguation (inverted diff_mean_sem_entropy)
- **info_gain_sem_dist_gray**: Information gain in semantic distance from pre-disambiguation to grayscale (pre - gray)
- **info_gain_entropy_gray**: Information gain in entropy from pre-disambiguation to grayscale (pre - gray)

---

## Definitions

- **Semantic distance**: A measure of how distant two concepts are in a given semantic space, using [openly available semantic embeddings](https://osf.io/jum2f/) derived from large text corpora. Low semantic distance means that participant-provided labels were close in semantic space to the target label, i.e. donkey and horse. Synonyms count as correct answers (semantic distance = 0).
- **Entropy**: A measure of variability in the set of labels used to describe an image, considering the amount and frequencies of different guesses. Low entropy means participants used a small and consistent set of labels to descirbe an image.
- **Information gain**: The reduction in semantic distance or uncertainty (entropy) after exposure to a stimulus, i.e. the greyscale image.