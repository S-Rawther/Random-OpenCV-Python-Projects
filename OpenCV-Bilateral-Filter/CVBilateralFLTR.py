# This code explains about the Bi-Lateral Filter Function
import cv2
import numpy as np

# Read Image and pointing the destination of the image
# Be sure to put the entire location of the image into imread function or put the image in the same directory and just type the image name with it format
# Declaring a variable for the cv2 function to read the image and another variable for resizing the image
image = cv2.imread('image1.png')
# We are giving the parameters for the resizing function with numbers being the size that we want to resize the image to
image_resize = cv2.resize(image, (500, 500))

# Applying Bilateral Filter with Diameter as 15, Sigmacolor and Sigmaspace 75
bilatfltr = cv2.bilateralFilter(image_resize, 15, 75, 75)

# Here, we use Numpy to display the before and after image side by side by using hstack
image_display = np.hstack((image_resize, bilatfltr))
# Using imshow function to display the before and after image
cv2.imshow("Original (Left) and Bilateral Filtered (Right)", image_display)

# Using waitkey function 0 so that the image will be displayed until any key is pressed
cv2.waitKey(0)
