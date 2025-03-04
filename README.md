# Car Damage Detection System

## Overview

This project implements a car damage detection system using YOLOv5 and Flask. The system can analyze images of damaged cars and identify various types of damage, making it useful for insurance companies, car dealerships, and vehicle inspection services.

## Features

- Real-time car damage detection using YOLOv5
- User-friendly web interface built with Flask
- Support for multiple damage types detection
- Easy-to-use image upload and analysis system
- Detailed damage assessment reports

## Technologies Used

- Python
- YOLOv5
- Flask
- OpenCV
- PyTorch
- HTML/CSS

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yatharthbhatia/car-damage-analysis.git
   cd car-damage-analysis
   ```

2. Install YOLOv5 dependencies:
   ```bash
   cd yolov5
   pip install -r requirements.txt
   cd ..
   ```

3. Download the pre-trained model weights (if not included in the repository)

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Access the web interface through your browser
2. Upload an image of a damaged car
3. Click on the "Detect Damage" button
4. View the results showing detected damage areas and classifications

## Model Training

The damage detection model was trained on a custom dataset using YOLOv5. The training process included:
- Data collection and annotation
- Model configuration and hyperparameter tuning
- Training on GPU infrastructure
- Validation and testing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- YOLOv5 team for the object detection framework
- Flask team for the web framework
- Contributors and maintainers of all dependencies

---
