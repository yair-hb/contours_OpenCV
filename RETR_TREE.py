import cv2
import numpy as np

imagen = cv2.imread('figcontorno.png')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gris,100,255, cv2.THRESH_BINARY)

contornos, hierachy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print ('hierachy= ', hierachy)

for i in range (len(contornos)):
    cv2.drawContours(imagen,contornos, i,(0,255,0), 3)
    cv2.imshow('imagen', imagen)
    cv2.waitKey(0)

cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()