import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
gaussian = int(sys.argv[3])

img = cv2.imread(path)
gaussianImg = cv2.GaussianBlur(img, (gaussian, gaussian), 0)
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Gaussian/" , name), gaussianImg)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Gaussian/" , name))