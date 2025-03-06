import os
import cv2
import torch
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_boxes
from utils.torch_utils import select_device
from PIL import Image

app = Flask(__name__)

device = select_device('cpu')

MODEL_PATH = r"models/car_damage5/weights/best.pt"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}.")

model = attempt_load(MODEL_PATH)
model.eval()

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"})

    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No file selected"})

    if file and allowed_file(file.filename):
        image = Image.open(file).convert("RGB")
        img_np = np.array(image)
        img = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # Ensure static directory exists
        static_dir = os.path.join(app.root_path, "static")
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)

        # Save original image
        original_image_path = os.path.join(static_dir, "original.jpg")
        cv2.imwrite(original_image_path, img)
        print(f"Original image saved at {original_image_path}")

        # Resize for YOLO
        img_resized = cv2.resize(img, (640, 640))
        img_tensor = torch.from_numpy(img_resized).to(device).float().permute(2, 0, 1).unsqueeze(0) / 255.0

        # YOLO detection
        with torch.no_grad():
            pred = model(img_tensor)[0]
            pred = non_max_suppression(pred, conf_thres=0.3, iou_thres=0.5)

        detections = []
        for det in pred:
            if det is not None and len(det):
                det[:, :4] = scale_boxes(img_tensor.shape[2:], det[:, :4], img.shape).round()
                for *xyxy, conf, cls in det:
                    x1, y1, x2, y2 = map(int, xyxy)
                    label = f"{model.names[int(cls)]} {conf:.2f}"
                    confidence = float(conf)
                    
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    detections.append({
                        "label": model.names[int(cls)],
                        "confidence": confidence,
                        "bbox": [x1, y1, x2, y2]
                    })

        # Save processed image
        result_path = os.path.join(static_dir, "result.jpg")
        cv2.imwrite(result_path, img)
        print(f"Processed image saved at {result_path}")

        return redirect(url_for("result"))

    return jsonify({"error": "Invalid file format"})

@app.route("/result")
def result():
    return render_template("result.html", original_image="static/original.jpg", result_image="static/result.jpg")

if __name__ == "__main__":
    app.run(debug=True)
