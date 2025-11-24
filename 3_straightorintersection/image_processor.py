# 파일명: image_processor.py

import cv2
import torch
import numpy as np

# 훈련 시 사용했던 설정과 동일하게 유지
GRAYSCALE = False 
ROI_CROP_HEIGHT = 130
IMAGE_SIZE = (224, 224)

def preprocess_for_model(frame):
    """
    카메라 프레임 하나를 받아 AI 모델 입력용 텐서로 변환합니다.
    """
    # 1. 색상 변환 (BGR -> RGB or Grayscale)
    if GRAYSCALE:
        proc_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        proc_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 2. 관심 영역(ROI) 자르기
    height = proc_image.shape[0]
    roi = proc_image[height - ROI_CROP_HEIGHT:, :]
    
    # 3. 모델 입력 크기로 리사이즈
    resized_roi = cv2.resize(roi, IMAGE_SIZE)
    
    # 4. 텐서로 변환 및 정규화
    if GRAYSCALE:
        # (H, W) -> (1, 1, H, W)
        input_tensor = torch.from_numpy(resized_roi).float().unsqueeze(0).unsqueeze(0)
    else:
        # (H, W, C) -> (1, C, H, W)
        input_tensor = torch.from_numpy(resized_roi).float().permute(2, 0, 1).unsqueeze(0)
    
    input_tensor /= 255.0 # 0~1 사이로 정규화
    
    return input_tensor