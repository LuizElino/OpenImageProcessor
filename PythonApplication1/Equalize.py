import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
img = cv2.imread(path,0)
h_eq = cv2.equalizeHist(img)
newName = name.split(".")[0]+"Equalized."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/", newName), h_eq)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))