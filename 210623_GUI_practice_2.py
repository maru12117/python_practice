#연습문제 (button을 누를떄마다 'apple'
import tkinter as tk

root=tk.Tk() #Tk 객체 인스턴스 생성 루트 자체(윈도우)
#root.mainloop() #root 표시'''

#버튼을 눌렀을때의 처리
def func():
    global x
    if x:
        label.config(text = "apple!")
        x = False
    else:
        label.config(text = "orange!!")
        x = True

x = False #전역변수
label = tk.Label(root, text="apple!") #라벨 생성(lebel 위젯 사용)
label.pack() #라벨 배치
button = tk.Button(root, text="Push!", command= func) #버튼 생성
button.pack() #버튼 배치
root.mainloop() #root표시
