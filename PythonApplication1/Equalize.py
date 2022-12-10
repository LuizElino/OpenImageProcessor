import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
img = cv2.imread(path,0)
h_eq = cv2.equalizeHist(img)
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Equalized/" , name), h_eq)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Equalized/" , name))