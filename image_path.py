import cv2
def crop_image(image, x_start, y_start, x_end, y_end):
cropped_image = image[y_start:y_end, x_start:x_end]
return cropped_image
image_path =r"C:\Users\ravik\Downloads\lovepik-natural-woods-png-image_401110806_wh1200.png"
image = cv2.imread(image_path)
if image is None:
print(f"Error: Could not load image {image_path}")
else:
cropped_region_1 = crop_image(image, 0, 0, 200, 200)
height, width, _ = image.shape
cropped_region_2 = crop_image(image, width // 4, height // 4, 3 * width
// 4, 3 * height // 4)
cropped_region_3 = crop_image(image, width - 200, height - 200, width,
height)
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Region 1 (Top-left)', cropped_region_1)
cv2.imshow('Cropped Region 2 (Center)', cropped_region_2)
cv2.imshow('Cropped Region 3 (Bottom-right)', cropped_region_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
