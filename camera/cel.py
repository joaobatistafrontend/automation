import cv2

video = cv2.VideoCapture()
ip = 'https://192.168.40.146:8080/video'
video.open(ip)
while True:
    _, img = video.read()
    cv2.imshow('test0',img)
    cv2.waitKey(1)