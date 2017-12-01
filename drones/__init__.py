import cv2

global cap
cap = cv2.VideoCapture(0)
w = 800
h = 448
cap.set(3,w);
cap.set(4,h);
