import cv2
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(base_dir, "img")

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    cv2.imshow('Frame', frame)
    
    img = cv2.imwrite('img/video.jpg',frame)
    

    cv2.waitKey(30)
