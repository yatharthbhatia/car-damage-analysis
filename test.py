import cv2
import numpy as np

# Create a blank test image
test_img = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.imwrite("C:/Users/Manan/Desktop/CarDamageAnalysisSepm/static/test.jpg", test_img)

print("Test image saved!")
