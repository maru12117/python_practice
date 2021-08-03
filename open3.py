#키 이벤트 발생

import numpy as np
import cv2

switch_case = {
    ord('a'):"a키 입력", #ord 함수 -문자를 아스키코드로 변환
    ord('b'):"b키 입력",
    0x41:"A키 입력",
    int('0x42', 16):"B키 입력",
    2424832 :"왼쪽 화살표키 입력",
    2490368 : "윗쪽 화살표키 입력",
    2555904 : "오른쪽 화살표 키 입력",
    2621440: "아래쪽 화살표 키 입력"
    }

image = np.ones((200,300), np.uint8) #화소값이 1인 행렬 생성
cv2.namedWindow("Keyboard Event")
cv2.imshow("Keyboard Event", image)

while True: #무한반복
    key = cv2.waitKeyEx(100) #100ms 동안 키 이벤트 대기
    if key == 27:
        break #ESC 누르면 종료
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows() #열린 모든 윈도우 제거
