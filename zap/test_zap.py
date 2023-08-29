import cv2
import requests



video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
_, buffer = cv2.imencode('.jpg', frame)
cv2.imshow('.jpg', buffer)