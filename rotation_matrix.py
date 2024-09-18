import cv2
import numpy as np
def rotate_image(image, angle):
(height, width) = image.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
return rotated_image
image_path =r"C:\Users\ravik\Downloads\lovepik-natural-woods-png-image_401110806_wh1200.png"
image = cv2.imread(image_path)
if image is None:
print(f"Error: Could not load image {image_path}")
else:
rotated_30 = rotate_image(image, 30)
rotated_45 = rotate_image(image, 45)
rotated_90 = rotate_image(image, 90)
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image (30 degrees)', rotated_30)
cv2.imshow('Rotated Image (45 degrees)', rotated_45)
cv2.imshow('Rotated Image (90 degrees)', rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
