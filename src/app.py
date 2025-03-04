from flask import Flask, render_template, request, redirect, url_for
import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the YOLOv5 detector
from src.model.detector import DamageDetector

app = Flask(__name__)

# Initialize the damage detector
detector = DamageDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        upload_folder = os.path.join(app.static_folder, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        
        # Run detection
        results = detector.detect(file_path)
        
        # Prepare results for display
        result_image_path = os.path.join('uploads', f'result_{file.filename}')
        
        return render_template('result.html', 
                               original_image=os.path.join('uploads', file.filename),
                               result_image=result_image_path,
                               damages=results)

if __name__ == '__main__':
    app.run(debug=True)