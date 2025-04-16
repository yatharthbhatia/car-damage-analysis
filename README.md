# 🚗 Car Damage Analysis 🔍

## Overview

This project implements a car damage detection system using YOLOv5 and Flask. The system analyzes images of damaged cars and identifies various types of damage, making it useful for insurance companies 🏢, car dealerships 🤝, and vehicle inspection services.

## Features

-   Real-time car damage detection using YOLOv5 🚀
-   User-friendly web interface built with Flask 🌐
-   Support for multiple damage types detection ✅
-   Easy-to-use image upload and analysis system 📤
-   Detailed damage assessment reports 📊

## Technologies Used
 
<div style="display: flex; justify-content: space-evenly; flex-wrap: wrap; gap: 10px; width: 100%;">



</div>
<div align="center">
    <img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=yellow" alt="Python" height="30"/>
    <img src="https://img.shields.io/badge/YOLOv5-000000?style=for-the-badge&logo=pytorch&logoColor=green" alt="YOLOv5" height="30"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=red" alt="Flask" height="30"/>
    <img src="https://img.shields.io/badge/OpenCV-000000?style=for-the-badge&logo=opencv&logoColor=lightblue" alt="OpenCV" height="30"/>
    <img src="https://img.shields.io/badge/PyTorch-000000?style=for-the-badge&logo=pytorch&logoColor=orange" alt="PyTorch" height="30"/>
    <img src="https://img.shields.io/badge/HTML5-000000?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" height="30"/>
    <img src="https://img.shields.io/badge/CSS3-000000?style=for-the-badge&logo=css3&logoColor=pink" alt="CSS3" height="30"/>
</div>

## Setup Instructions

1.  Clone the repository:

    ```bash
    git clone https://github.com/yatharthbhatia/car-damage-analysis.git
    cd car-damage-analysis
    ```

2.  Install YOLOv5 dependencies:

    ```bash
    cd yolo
    pip install -r requirements.txt
    cd ..
    ```

3.  Download the pre-trained model weights (if not included in the repository).

4.  Run the application:

    ```bash
    python app.py
    ```

5.  Open your web browser and navigate to `http://localhost:5000` 💻

## Examples
## Application Interface

### Upload Page
![Upload Interface](docs/upload_interface.png)

### Detection Result
![Detection Result](docs/detection_result.png)

## Model Training

The damage detection model was trained on a custom dataset using YOLOv5. The training process included:

-   Data collection and annotation
-   Model configuration and hyperparameter tuning
-   Training on GPU infrastructure ⚡
-   Validation and testing
