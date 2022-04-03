import cv2, os, numpy as np
cap = cv2.VideoCapture(0)
path = './image/'
h = s = p = e = 0
while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF