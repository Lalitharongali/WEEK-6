import cv2
import numpy as np
def resize_image(image, scale_percent, interpolation):
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dimensions = (width, height)
resized = cv2.resize(image, dimensions, interpolation=interpolation)
return resized
image_path =[
r"C:\Users\ravik\Downloads\lovepik-natural-woods-png-image_401110806_wh1200.png"]
image = cv2.imread(image_path)
if image is None:
print(f"Error: Could not load image {image_path}")
else:
scale_percent = 50
resized_nearest = resize_image(image, scale_percent, cv2.INTER_NEAREST)
resized_linear = resize_image(image, scale_percent, cv2.INTER_LINEAR)
resized_cubic = resize_image(image, scale_percent, cv2.INTER_CUBIC)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image (INTER_NEAREST)', resized_nearest)
cv2.imshow('Resized Image (INTER_LINEAR)', resized_linear)
cv2.imshow('Resized Image (INTER_CUBIC)', resized_cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()
