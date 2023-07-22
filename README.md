# Temporal Action Proposal Generation with Background Constraint (AAAI 2022)
![](./bcnet.png )

This repository contains the source code of the [BCNet](https://arxiv.org/abs/2112.07984) (Background Constraint Network).
## TODOs
- [x] add Inference code
- [x] add Training code

## Overview

Temporal action proposal generation (TAPG) is a challenging task that aims to locate action instances in untrimmed videos with temporal boundaries.
To evaluate the confidence of proposals, the existing works typically predict action score of proposals that are supervised by the temporal Intersection-over-Union (tIoU) between proposal and the ground-truth.
In this paper, we innovatively propose a general auxiliary Background Constraint idea to further suppress low-quality proposals, by utilizing the background prediction score to restrict the confidence of proposals. In this way, the Background Constraint concept can be easily plug-and-played into existing TAPG methods (e.g., BMN, GTAD). 
From this perspective, we propose the Background Constraint Network (BCNet) to further take advantage of the rich information of action and background. Specifically, we introduce an Action-Background Interaction module for reliable confidence evaluation, which models the inconsistency between action and background by attention mechanisms at the frame and clip levels.
Extensive experiments are conducted on two popular benchmarks,i.e., ActivityNet-1.3 and THUMOS14. The results demonstrate that our method outperforms state-of-the-art methods. Equipped with the existing action classifier, our method also achieves remarkable performance on the temporal action localization task.






