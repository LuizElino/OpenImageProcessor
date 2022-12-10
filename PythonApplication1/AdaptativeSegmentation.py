import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
mediana = int(sys.argv[3])

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
suave = cv2.medianBlur(img, mediana)
adaptative = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/AdaptativeSegmentation/" , name), adaptative)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/AdaptativeSegmentation/" , name))
