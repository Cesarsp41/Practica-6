import numpy as np
import cv2

cam = cv2.VideoCapture(1)

#Colores (tonos)
amarilloBajo = np.array([22,109,20],np.uint8)
amarilloAlto = np.array([32,255,255],np.uint8)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

verdeBajo = np.array([38,80,20],np.uint8)
verdeAlto = np.array([90,255,255],np.uint8)

rojoBajo1 = np.array([0,100,60],np.uint8)
rojoAlto1 = np.array([3,255,255],np.uint8)

print('Presiona "espacio" para cerrar el video.')

while(cam.isOpened()):
  ready,imgVolteada = cam.read()
    img = cv2.flip(imgVolteada,1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    maskAmarillo = cv2.inRange(hsv,amarilloBajo,amarilloAlto)
    maskAzul = cv2.inRange(hsv,azulBajo,azulAlto)
    maskVerde = cv2.inRange(hsv,verdeBajo,verdeAlto)
    maskRojo1 = cv2.inRange(hsv,rojoBajo1,rojoAlto1)
    maskRojo2 = cv2.inRange(hsv,rojoBajo2,rojoAlto2)
    maskRojo = cv2.add(maskRojo1,maskRojo2)
    
    imgAmarillo = cv2.bitwise_and(img,img,mask=maskAmarillo)
    imgAzul = cv2.bitwise_and(img,img,mask=maskAzul)
    imgVerde = cv2.bitwise_and(img,img,mask=maskVerde)
    imgRojo = cv2.bitwise_and(img,img,mask=maskRojo)

    img = cv2.subtract(img,imgAmarillo)
    img = cv2.subtract(img,imgAzul)
    img = cv2.subtract(img,imgVerde)
    img = cv2.subtract(img,imgRojo)
    
    if ready == True:
        cv2.imshow('Video',img)
        cv2.imshow('Mask amarillo',imgAmarillo)
        cv2.imshow('Mask azul',imgAzul)
        cv2.imshow('Mask verde',imgVerde)
        cv2.imshow('Mask rojo',imgRojo)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.destroyAllWindows()
            break
