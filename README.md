TODOs
 add Inference code
 add Training code
Overview
With the rapid growth of video data, video understanding, such as action recognition and action detection, is becoming critical for intelligent video surveillance, human-computer interaction, machine vision, autonomous driving, action extraction, action analysis and other fields. Due to the need for efficient temporal modeling in untrimmed videos, it is still challenging for Temporal Action Detection (TAD) tasks to identify the boundaries of actions so as to generate high-quality action proposals. Most of the existing Temporal Action Proposal Generation (TAPG) methods employ two-stream (i.e., RGB and optical flow) feature representation that covers short-term motion information based solely on the feature changes between adjacent frames, which lacks long-term motion information. 

RGB and optical flow features to capture the appearance and motion information of action instances. 
Temporal Action Proposal Generation (TAPG) is the process of identifying the boundaries of actions in untrimmed videos. 

Installation
Create conda environment

conda create -n bcnet python=3.7 -y
source activate bcnet
Requirements

git clone https://github.com/happy-lifi/BCNet.git
cd BCNet
pip install -r requirements.txt
Data setup
We use the features provided by G-TAD. To reproduce the results in THUMOS14 without further changes:

Download the data from GooogleDrive[https://drive.google.com/drive/folders/1-19PgCRTTNfy2RWGErvUUlT0_3J-qEb8]

Place it into a folder named TSN_pretrain_avepool_allfrms_hdf5 inside data/thumos_feature.

You could also pass the folder containing the HDF5 files if the script admits the following argument --feature_path.

Training
sh ./run/bcn_train.sh
Testing
sh ./run/bcn_infer.sh
THUMOS Results
(1) 特征残差
Method	Feature	mAP@0.3	mAP@0.4	mAP@0.5	mAP@0.6	mAP@0.7	checkpoint
BCNet	TSN	67.4	61.0	52.5	42.4	29.9	[链接: https://pan.baidu.com/s/1ACmcPTNuTlUrOFaSLSc2Nw?pwd=1234 提取码: 1234 ]
Acknowledgement
We especially thank the contributors of BMN and G-TAD for providing helpful code.

Citing
@article{yang2021temporal,
  title={Temporal Action Proposal Generation with Background Constraint},
  author={Yang, Haosen and Wu, Wenhao and Wang, Lining and Jin, Sheng and Xia, Boyang and Yao, Hongxun and Huang, Hujie},
  journal={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2022}
}
Contact
For any question, please file an issue or contact

Haosen Yang: haosen.yang.6@gmail.com
Wenhao Wu: whwu.ucas@gmail.com
