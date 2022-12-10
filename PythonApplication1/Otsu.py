import cv2 
import os
import sys
import mahotas

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
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Otsu/" , name), otsu)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Otsu/" , name))




