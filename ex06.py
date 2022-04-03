import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('001.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()