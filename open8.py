import numpy as np
import cv2

blue, green, red = (255,0,0),(0,255, 0),(0,0,255)
image = np.zeros((400,600,3), np.uint8)
image[:]=(255,255,255)

pt1,pt2 = (50,50),(250,150)
pt3,pt4 = (400, 150), (500, 50)
roi=50,200,200,100

#직선 그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4
