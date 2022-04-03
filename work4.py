import cv2, os, numpy as np
cap = cv2.VideoCapture(0)
path = './work/'
h = s = p = e = 0
while True:
  _, frame = cap.read()

  key = cv2.waitKey(1) & 0xFF
  if key == ord('l') : h += 1; cv2.imwrite(path + 'LightStick_' + str(h) + '.png', frame)
  if key == ord('p') : s += 1; cv2.imwrite(path + 'Pen_' + str(s) + '.png', frame)
  if key == ord('k') : p += 1; cv2.imwrite(path + 'Key_' + str(p) + '.png', frame)
  if key == ord('e') : e += 1; cv2.imwrite(path + 'else_' + str(e) + '.png', frame)
  y = []; D = []
  for fname in os.listdir(path):
    if '.png' in fname:
        x = cv2.imread(path + fname)
        y.append(fname.split('_')[0])
        D.append(np.sum ((x-frame)**2))
  if len(D) > 0:
    ans = y[D.index(min(D))]
    if ans != 'else': cv2.putText(frame, ans, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0)) 
    # print(ans)
  cv2.imshow('frame', frame)