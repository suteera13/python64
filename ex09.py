import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('001.png',1)
print("Original image configuration :",img.shape)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
# resizing of an image is done
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
resize_img = cv2.resize(img1,(300, 200))
print("Resize image configuration :",resize_img.shape)
  # show the image
cv2.imshow("window2",resize_img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize_img2 = cv2.resize(img,(150, 100))
print("Resize image configuration :",resize_img2.shape)
  # show the image
cv2.imshow("window3",resize_img2)
cv2.waitKey(-1)