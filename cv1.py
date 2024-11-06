import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = 'C:/Users/sai vidya/OneDrive/Pictures/Screenshots/Screenshot 2023-10-20 103211.png'
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
