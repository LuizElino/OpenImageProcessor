import cv2
import numpy as np
import os
import sys

path = sys.argv[1]
name = sys.argv[2]

#path = "C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Input/BABUINO.jpg"
#name = "BABUINO.jpg"

image1 = cv2.imread(path)
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 

newName = name.split(".")[0]+"Gray."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), img)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))


