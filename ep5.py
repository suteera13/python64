import cv2
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    R = frame[:, :, 2]
    G = frame[:, :, 1]
    B = frame[:, :, 0]
    mask = (R < 90) & (G < 30) & (B < 30)
    mask1 = (R < 50) & (G < 90) & (B < 20)
    mask2 = (R < 30) & (G < 20) & (B < 80)
    cv2.imshow('frame' , frame)
    cv2.imshow('mask', mask*1.0)
    cv2.imshow('mask1', mask1*1.0)
    cv2.imshow('mask2', mask2*1.0)
    cv2.waitKey(1)