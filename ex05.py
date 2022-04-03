import cv2
img_bgr = cv2.imread('001.png', 1)
img_bgr = cv2.resize(img_bgr, None, fx=0.5, fy=0.5)
print(img_bgr.shape)
cv2.imshow("image_bgr", img_bgr)
cv2.waitKey(-1)

img_gray = cv2.imread(r'.\input\001.png', 0)
img_gray = cv2.resize(img_bgr, None, fx=0.5, fy=0.5)
print(img_bgr.shape)
cv2.imshow("img_gray", img_gray)
cv2.waitKey(-1)