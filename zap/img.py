import cv2
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(base_dir, "img")
os.chdir(diretorio)


video = cv2.VideoCapture(0)
imgsalva = 'imgsalva.jpg'



while True:
     ret, frame = video.read()
     if not ret:
          break
     cv2.imshow('Frame', frame)

     print("Salvando imagem...")
     cv2.imwrite(imgsalva,frame)
     imgsalva.join(diretorio)
     print("Imagem salva!")

     cv2.imshow('salva',imgsalva)

     cv2.waitKey(30)
