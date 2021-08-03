#GUI

import tkinter as tk
'''root=tk.Tk()

lbl = tk.Label(root, text="EduCoding",underline=3)
lbl.pack()

txt = tk.Entry(root)
txt.pack()

btn = tk.Button(root, text="OK", activebackground ="red", width=5)
btn.pack()

root.mainloop()'''

'''root=tk.Tk() #Tk 객체 인스턴스 생성 루트 자체(윈도우)
label = tk.Label(root, text="Hello World") #라벨 생성(lebel 위젯 사용)

label.pack() #라벨 배치
#root.mainloop() #root 표시'''

#버튼을 눌렀을때의 처리
'''def func1(): 
    print('pushed') #메세지를 파이썬 셀에 출력

def func2(): 
    print('Hi')

button1 = tk.Button(root, text="Push!", command= func1) #버튼 생성
button2 = tk.Button(root, text="Hi", command= func2)
button1.pack() #버튼 배치
button2.pack()
root.mainloop() #root표시'''

#
root=tk.Tk() #Tk 객체 인스턴스 생성 루트 자체(윈도우)
label = tk.Label(root, text="Push Button") #라벨 생성(lebel 위젯 사용)
label.pack() #라벨 배치
#root.mainloop() #root 표시'''

#버튼을 눌렀을때의 처리
def func(): 
    label.config(text = "pushed") #label 표시변경(pushi button => pushed로 변경


button1 = tk.Button(root, text="Push!", command= func) #버튼 생성
button1.pack() #버튼 배치
root.mainloop() #root표시


