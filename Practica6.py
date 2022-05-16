import numpy as np
import cv2

cam = cv2.VideoCapture(1)

#Colores (tonos)
amarilloBajo = np.array([22,109,20],np.uint8)
amarilloAlto = np.array([32,255,255],np.uint8)
