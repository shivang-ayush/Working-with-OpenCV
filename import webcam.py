

import cv2
webcam = cv2.VideoCapture(0)
webcam.set (3, 640)
webcam.set(4, 480)
webcam.set(10, 100)

while True:
    success, img = webcam.read()
    cv2.imshow("WebCAM", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
