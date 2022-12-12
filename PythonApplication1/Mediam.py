import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
mediam = int(sys.argv[3])

img = cv2.imread(path)
mediam =  cv2.blur(img, ( mediam, mediam))
newName = name.split(".")[0]+"Mediam."+name.split(".")[1]
cv2.imwrite(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName), mediam)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/" , newName))
print(os.path.join(newName))



