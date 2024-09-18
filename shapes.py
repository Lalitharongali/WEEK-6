import cv2
import numpy as np
image = np.zeros((500, 500, 3), dtype='uint8')
start_point = (50, 50)
end_point = (450, 50)
color = (255, 0, 0)
thickness = 5
cv2.line(image, start_point, end_point, color, thickness)
top_left_corner = (100, 100)
bottom_right_corner = (400, 300)
color = (0, 255, 0)
thickness = 3
cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness)
top_left_corner_filled = (150, 150)
bottom_right_corner_filled = (350, 250)
color_filled = (0, 0, 255)
cv2.rectangle(image, top_left_corner_filled, bottom_right_corner_filled,
color_filled, -1)
center = (250, 400)
radius = 50
color = (255, 255, 0)
thickness = -1
cv2.circle(image, center, radius, color, thickness)
center = (250, 200)
axes_length = (100, 50)
angle = 45
start_angle = 0
end_angle = 360
color = (0, 255, 255)
thickness = 2
cv2.ellipse(image, center, axes_length, angle, start_angle, end_angle,
color, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
text_position = (100, 450)
font_scale = 1
font_color = (255, 255, 255)
thickness = 2
cv2.putText(image, 'OpenCV Shapes', text_position, font, font_scale,
font_color, thickness)
cv2.imshow('Shapes on Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
