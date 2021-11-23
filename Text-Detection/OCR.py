import pytesseract as pt
import cv2

# Using Tesseract as pt for ease of use and Importing Tesseract to the code
# You must include the entire file location where tesseract is found, which is usually in program files.
pt.pytesseract.tesseract_cmd = "tesseract.exe"

# Be sure to put the entire location of the image into imread function or put the image in the same directory and just type the image name along with its format
image = cv2.imread('img.jpg')

# Setting height and Width of the Characters
height, width, _ = image.shape

# Setting the border for bounding box
border = pt.image_to_boxes(image)

# Loop to read the characters
for i in border.splitlines():
    i = i.split(' ')
    x = int(i[1])
    y = int(i[2])
    a = int(i[3])
    b = int(i[4])
    print(i)

    # Applying rectangle fuction to the characters to create bounding boxes
    cv2.rectangle(image, (x, height-y), (a, height-b), (0, 128, 0), 1)

    # Using putText to display the characters as text on the Image
    cv2.putText(image, i[0], (x, height-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 0), 2)

cv2.imshow('Image to Text', image)

# Kill Process
cv2.waitKey(0)
