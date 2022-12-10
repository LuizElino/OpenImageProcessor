import cv2
import numpy as np
import os
import sys

path = sys.argv[1]
name = sys.argv[2]

image1 = cv2.imread(path)
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 

cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/" , name), img)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/" , name))


