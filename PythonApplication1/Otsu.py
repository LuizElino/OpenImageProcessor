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
newName = name.split(".")[0]+"Otsu."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), otsu)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))




