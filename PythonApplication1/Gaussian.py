import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
gaussian = int(sys.argv[3])

img = cv2.imread(path)
gaussianImg = cv2.GaussianBlur(img, (gaussian, gaussian), 0)
newName = name.split(".")[0]+"Gaussian."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), gaussianImg)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/", newName))
print(os.path.join(newName))