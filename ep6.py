import cv2
cap = cv2.VideoCapture('rtsp://192.168.0.103:8080/h264_pcm.sdp')
while True:
  _, frame = cap.read()
  cv2.imshow('frame' , frame)
  cv2.waitKey(1)