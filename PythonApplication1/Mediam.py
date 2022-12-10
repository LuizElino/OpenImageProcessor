import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
mediam = int(sys.argv[3])

img = cv2.imread(path)
mediam =  cv2.blur(img, ( mediam, mediam))
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Mediam/" , name), mediam)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/Mediam/" , name))



