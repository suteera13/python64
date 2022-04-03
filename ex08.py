import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
userId = input("Enter user id : ")
while True:
  ret, frame = cap.read()
  cv.imshow('Press S save', frame)
  key = cv.waitKey(1) 
  if key & 0xFF == ord('s'):
    image_path = 'input/'+userId+'.jpg'
    cv.imwrite(image_path, frame)
    cap.release()
    cv.destroyAllWindows()