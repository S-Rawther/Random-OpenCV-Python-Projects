import cv2
import numpy as np

# Read the Image
image = cv2.imread('image_1.png')
# Resizing image for Optimal Viewing
resize = cv2.resize(image, (500, 500))

# Creating a Sharpening Kernel Filter for Sharpening Function
# Changing the array value will change the sharpening intensity
# The Kernel value must be equal to 1
sharp_kernel = np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])
# Using the Filter to Perform Sharpening Function on Image
image_sharpen = cv2.filter2D(resize, -1, sharp_kernel)
# Displaying Image Side by Side
display = np.hstack((resize, image_sharpen))
cv2.imshow("Original (Left) and Sharpened (Right)", display)

cv2.waitKey(0)
