# Model Weights Directory

This directory contains the trained YOLOv5 model weights for car damage detection.

## Model Files

- `best.pt`: The best performing model weights from training

## Usage

These model weights are automatically loaded by the `DamageDetector` class in `src/model/detector.py`.

To use a different model, you can pass the path to the model weights when initializing the detector:

```python
from src.model.detector import DamageDetector

# Use custom model weights
detector = DamageDetector(model_path='path/to/custom/weights.pt')
```