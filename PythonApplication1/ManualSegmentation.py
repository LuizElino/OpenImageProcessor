import cv2 
import os
import sys

path = sys.argv[1]
name = sys.argv[2]
mediana = int(sys.argv[3])
thresh1 = int(sys.argv[4])
thresh2 = int(sys.argv[5])

img = cv2.imread(path)
suave = cv2.medianBlur(img, mediana)
ret, img_bin = cv2.threshold(suave, thresh1, thresh2, cv2.THRESH_BINARY)
cv2.imwrite(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/ManualSegmentation/" , name), img_bin)
print(os.path.join("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/ManualSegmentation/" , name))
