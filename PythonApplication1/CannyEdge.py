import numpy as np
import cv2
import os
import sys

#path = "C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Input/fruits.jpg"
#name = "fruits.jpg"


path = sys.argv[1]
name = sys.argv[2]


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#thresholding 
_, thresh = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((2, 2), np.uint8)

#dilation
dilation = cv2.dilate(thresh, kernal, iterations=2)

#Countour shapes
contours, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#objects found
objects = str(len(contours))

#Print Number of objects
text = "Obj:"+str(objects)
cv2.putText(dilation, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
            0.4, (240, 0, 159), 1)

newName = name.split(".")[0]+"Canny."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), dilation)
print(os.path.join(newName))
print(objects)

