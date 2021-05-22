import cv2
import numpy as np

# Reads Image from File
picture = cv2.imread('img1.png')
# Resizing Image
resize_pic = cv2.resize(picture, (400, 400), interpolation=cv2.INTER_AREA)

# Taking the Mean of the Matrix
mean = cv2.blur(resize_pic, (5, 5))
# Numpy Array
stack = np.hstack((resize_pic, mean))
cv2.imshow("Original (Left) and Mean Filtered (Right)", stack)

cv2.waitKey(0)

