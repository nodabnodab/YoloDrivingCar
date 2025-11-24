# 파일명: model.py

import torch
import torch.nn as nn
from torchvision import models

class DrivingModel(nn.Module):
    def __init__(self, grayscale=False):
        super(DrivingModel, self).__init__()
        
        # [최종 수정] Jetson의 torchvision v0.8.0 환경에 맞춰 pretrained=True 사용
        self.backbone = models.mobilenet_v2(pretrained=True)
        
        if grayscale:
            original_weights = self.backbone.features[0][0].weight.data
            new_weights = original_weights.mean(dim=1, keepdim=True)
            self.backbone.features[0][0] = nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1, bias=False)
            self.backbone.features[0][0].weight.data = new_weights
            
        num_features = self.backbone.classifier[1].in_features
        self.backbone.classifier = nn.Identity()
        
        self.steering_head = nn.Sequential(
            nn.Linear(num_features, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 1)
        )
        
        self.intersection_head = nn.Sequential(
            nn.Linear(num_features, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 5)
        )
        
    def forward(self, x):
        features = self.backbone(x)
        steering = self.steering_head(features)
        intersection = self.intersection_head(features)
        return steering, intersection