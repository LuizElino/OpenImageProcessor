import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
mediana = int(sys.argv[3])

img = cv2.imread(path)
medianaImg = cv2.medianBlur(img, mediana)
newName = name.split(".")[0]+"Mediana."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), medianaImg)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))

