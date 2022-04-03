import cv2
cap = cv2.VideoCapture(1)
while True:
  _, frame = cap.read()
  R = frame[:, :, 2]
  G = frame[:, :, 1]
  B = frame[:, :, 0]
  #print(frame.shape)
  cv2.imshow('frame' , frame)
  cv2.imshow('R', R)
  cv2.imshow('G', G)
  cv2.imshow('B', B)
  cv2.waitKey(1)