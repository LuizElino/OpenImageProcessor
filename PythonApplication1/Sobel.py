import cv2 
import os
import sys
import mahotas
import numpy as np

#path = "C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/tiger.jpg"
#name = "tiger.jpg"
#mediana = 3

path = sys.argv[1]
name = sys.argv[2]
mediana = int(sys.argv[3])

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
suave = cv2.GaussianBlur(img, (mediana, mediana), 0)
T = mahotas.thresholding.otsu(suave)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
otsu = cv2.bitwise_not(temp)

sobelX = cv2.Sobel(otsu, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(otsu, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
bordas = cv2.bitwise_or(sobelX, sobelY)
newName = name.split(".")[0]+"Sobel."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), bordas)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))
