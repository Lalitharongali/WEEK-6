import cv2
def display_image(file_path):
image = cv2.imread(file_path)
if image is None:
print(f"Error: Could not load image {file_path}")
return
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_paths = [
https://w0.peakpx.com/wallpaper/162/65/HD-wallpaper-barbie-birtay-face-barbie.jpg
]
for path in image_paths:
display_image(path)
