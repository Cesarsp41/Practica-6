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
