import os
import sys
import torch
import cv2
import numpy as np

# Add YOLOv5 to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'yolov5'))

class DamageDetector:
    """Class for detecting car damage using YOLOv5"""
    
    def __init__(self, model_path=None):
        """
        Initialize the damage detector with a pre-trained YOLOv5 model
        
        Args:
            model_path (str, optional): Path to the model weights. If None, uses the default model.
        """
        if model_path is None:
            # Default to the project's trained model
            model_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                'models', 'best.pt'
            )
        
        # Load the YOLOv5 model
        self.model = torch.hub.load(
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'yolov5'),
            'custom', 
            path=model_path, 
            source='local'
        )
        
        # Set model parameters
        self.model.conf = 0.25  # Confidence threshold
        self.model.iou = 0.45   # IoU threshold
        self.model.classes = None  # All classes
        
    def detect(self, image_path):
        """
        Detect car damage in an image
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            list: List of detected damages with their details
        """
        # Run inference
        results = self.model(image_path)
        
        # Save the results image
        results.save(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            'src', 'static', 'uploads', f'result_{os.path.basename(image_path)}'
        ))
        
        # Process results
        damages = []
        for pred in results.xyxy[0]:
            x1, y1, x2, y2, conf, cls = pred.tolist()
            damage_type = results.names[int(cls)]
            
            damages.append({
                'type': damage_type,
                'confidence': round(conf * 100, 2),
                'bbox': [int(x1), int(y1), int(x2), int(y2)]
            })
        
        return damages
    
    def get_damage_types(self):
        """
        Get the list of damage types the model can detect
        
        Returns:
            list: List of damage type names
        """
        return list(self.model.names.values())