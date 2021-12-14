import cv2
import numpy as np

imagen = cv2.imread('figcontorno.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gris, 100,255, cv2.THRESH_BINARY)

contornos1,hierachy1 = cv2.findContours(th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contornos2,hierachy2 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos1, -1, (0,255,0),3)
print ('len(contornos1[2])=', len(contornos1[2]))
print ('len(contornos1[2])=', len(contornos2[2]))

cv2.imshow('imagen de prueba',imagen)
cv2.imshow('TH', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
