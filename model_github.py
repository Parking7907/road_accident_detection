import torch
import torch.nn as nn
import torch.nn.functional as F
import pdb
from efficientnet_pytorch import EfficientNet
from model_utils.attention_modules import Spatial_Attention
from model_utils.attention_modules import Temporal_Attention


class MYNET(nn.Module):
    def __init__(self, sequence_size):
        super().__init__()
        self.sequence_size = sequence_size
        self.motion_features = Spatial_Attention(sequence_size, True)
        self.backbone = EfficientNet.from_pretrained('efficientnet-b0', in_channels=3)
        self.TA = Temporal_Attention(n_segment=sequence_size//3, feature_dim=1000, num_class=2)
        
    def forward(self, rgb):
        B = rgb.shape[0]
        PA = self.motion_features(rgb)
        #rgb Shape = 16 31 3 224 224
        #encoded features = rgb[:, 1:, ...] => 16, 30, 3, 224, 224
        encoded_features = rgb[:,1:,...]*PA
        
        backbone_out = self.backbone(encoded_features.mean(2).reshape(-1, 3, 224, 224))
        temporal_vec = (backbone_out).reshape(B, self.sequence_size//3, -1)
        return self.TA(temporal_vec)