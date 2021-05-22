import cv2
import numpy as np

# Reads Image
image = cv2.imread('img1.png')
image_resize = cv2.resize(image, (500, 500))

# Applying Gaussian Function
# Creating Gaussian Kernel on a 5 x 5 Matrix
g_blur = cv2.GaussianBlur(image_resize,(7, 7), 15)
# Stacking Original and De-Noised image on a Window
display_array = np.hstack((image_resize, g_blur))
cv2.imshow("Original (Left) and Gaussian Filtered (Right)", display_array)

cv2.waitKey(0)