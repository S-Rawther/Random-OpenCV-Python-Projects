import cv2
import numpy as np

# Read Image
image = cv2.imread('pic_1.png')
image_resize = cv2.resize(image, (500, 500))
# Applying Median Filter
median_fltr = cv2.medianBlur(image_resize, 5)
display = np.hstack((image_resize, median_fltr))
cv2.imshow("Original (Left) and Median Filtered (Right)", display)

cv2.waitKey(0)