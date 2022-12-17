
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import sys
import os

path = sys.argv[1]
name = sys.argv[2]
image1 = cv2.imread(path)
hist,bin = np.histogram(image1.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')
newName = name.split(".")[0]+"Histogram."+name.split(".")[1]
plt.savefig("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/"+newName)
print(os.path.join("C:/OpenImageProcessor/ImageConvert/wwwroot/Imgs/Actual/", newName))
print(os.path.join(newName))
