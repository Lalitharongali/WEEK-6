import cv2
image_path = r"C:\Users\ravik\Downloads\lovepik-natural-woods-png-image_401110806_wh1200.png"
image = cv2.imread(image_path)
if image is None:
print(f"Error: Could not load image {image_path}")
else:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('LAB Image', lab_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
