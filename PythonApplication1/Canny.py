import cv2 
import os
import sys
import mahotas

#path = "C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/BABUINO.jpg"
#name = "BABUINO.jpg"
#mediana = 3
#canny1 = 100
#canny2 = 200

path = sys.argv[1]
name = sys.argv[2]
mediana = int(sys.argv[3])
canny1 = int(sys.argv[4])
canny2 = int(sys.argv[5])

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
suave = cv2.GaussianBlur(img, (mediana, mediana), 0)
T = mahotas.thresholding.otsu(suave)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
otsu = cv2.bitwise_not(temp)
bordas = cv2.Canny(otsu, canny1, canny2)
newName = name.split(".")[0]+"Canny."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), bordas)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))