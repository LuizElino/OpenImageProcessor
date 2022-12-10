
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import sys

path = sys.argv[1]
name = sys.argv[2]
image1 = cv2.imread(path)
hist,bin = np.histogram(image1.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')

plt.savefig("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/"+name)
print("C:/Users/elino/source/repos/PythonApplication1/ImageConvert/wwwroot/Imgs/Output/"+name)

