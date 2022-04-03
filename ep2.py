import cv2
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    R = frame[:, :, 2]
    G = frame[:, :, 1]
    B = frame[:, :, 0]
    cv2.imshow('frame' , frame)
    cv2.imshow('R', R)
    cv2.imshow('R', G)
    cv2.imshow('R', B)
    cv2.waitKey(1)