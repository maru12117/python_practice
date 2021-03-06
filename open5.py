#트랙바

import numpy as np
import cv2

def onChange(value): #트랙바 콜백 함수
    global image
    print("value 값:", value)
    image = np.zeros((300,500), np.uint8) #영상 data초기화
    image = image+value #행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8) #영상 생성

title = "Trackbat Event"
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange) #현재값, 최대값, 콜백함수
cv2.waitKey(0)
cv2.destroyAllWindows()
