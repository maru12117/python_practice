#연습문제 (button을 누를떄마다 'apple'
'''import tkinter as tk

root=tk.Tk() #Tk 객체 인스턴스 생성 루트 자체(윈도우)

#버튼을 눌렀을때의 처리
def func():
        label.config(text = "Pushed!!!") #클릭!

def func_event1(ev): #이벤트처리가 되면, 해당 함수(
    #print(ev) ev의 좌표가 출력
    label.config(text='Leave!!!')

def func_event2(ev): #이벤트 처리
    label.config(text='Enter!!!')

label = tk.Label(root, text="Push Button") #라벨 생성(lebel 위젯 사용)
label.pack() #라벨 배치
button = tk.Button(root, text="Push!", command= func) #버튼 생성
button.pack() #버튼 배치

#마우스 커서가 버튼을 벗어났을 때의 이벤트 추가
button.bind('<Leave>',func_event1) #어떤 이벤트를 발생했을때 조작함
button.bind('<Enter>',func_event2)

root.mainloop() #root표시'''


#버튼만들기 Event Object
'''import tkinter as tk

root=tk.Tk() 

def func():
        label.config(text = "Pushed!!!") #클릭!

def func_event_click(ev): #ev 동작
    disp = str(ev.x)+'/'+str(ev.y) #마우스 위치 x,y좌표값 출력
    label.config(text=disp)

label = tk.Label(root, text="Push Button") #라벨 생성(lebel 위젯 사용)
label.pack() #라벨 배치
button = tk.Button(root, text="Push!", command= func) #버튼 생성
button.pack() #버튼 배치

#마우스 커서가 버튼을 벗어났을 때의 이벤트 추가
button.bind('<Button-1>',func_event_click) #어떤 이벤트를 발생했을때 조작함
#Button-1 왼쪽 마우스를 눌렀을떄

root.mainloop() #root표시'''

#라디오 버튼만들기
'''import tkinter as tk 

def Action1():
        label.config(text = "Button1") #클릭!
def Action2():
        label.config(text = "Button2") #클릭!

root=tk.Tk()

sel=tk.IntVar() #라디오 버튼값을 저장하는 정수형 variable 객체 생성
sel.set(1) #sel에 1할당(라디오 버튼에서 첫번쨰꺼) : 초기 지정

label = tk.Label(root, text="Select Button") #라벨 생성(lebel 위젯 사용) underline은 줄 3개
label.pack() #라벨 배치

rb1=tk.Radiobutton(root, text="Option1", variable=sel, value=1, indicatoron=1, command= Action1)
rb1.pack() #버튼 배치, variable=rbvar같은 그룹 라디오동작, indicatoron=0 버튼모양 바꾸기

rb2=tk.Radiobutton(root, text="Option2", variable=sel, value=2, indicatoron=1, command= Action2)
rb2.pack()

root.mainloop() #root표시'''

#라디오 버튼만들기
'''import tkinter as tk

def Action1():
        label.config(text = "Radio button1")
def Action2():
        label.config(text = "Radio button2") 
def Action3():
        label.config(text = "Radio button3")
def Action4():
        print(sel.get())

root=tk.Tk()

sel=tk.IntVar(root, 0) #라디오 버튼값을 저장하는 정수형 variable 객체 생성 #tk.StringVal() 문자형 객체 Control variable
sel.set(1) #sel에 1할당(라디오 버튼에서 첫번쨰꺼) : 초기 지정

label = tk.Label(root, text="Encoding", underline=5) #라벨 생성(lebel 위젯 사용) underline은 줄 3개
label.pack() #라벨 배치

rb1=tk.Radiobutton(root, text="Choice1", variable=sel, value=1, indicatoron=1, command= Action1) #각각의 묶음 variable
rb1.pack() #버튼 배치, variable=rbvar같은 그룹 라디오동작, indicatoron=0 버튼모양 바꾸기

rb2=tk.Radiobutton(root, text="Choice2", variable=sel, value=2, indicatoron=1, command= Action2)
rb2.pack()

rb3=tk.Radiobutton(root, text="Choice3", variable=sel, value=3, indicatoron=1, command= Action3)
rb3.pack()

button=tk.Button(root, text="Print choice", command=Action4)
button.pack()

root.mainloop() #root표시'''

#lambda 사용
'''import tkinter as tk

def Action1():
        label.config(text = "Radio button1")
def Action2():
        label.config(text = "Radio button2") 
def Action3():
        label.config(text = "Radio button3")

root=tk.Tk()

sel=tk.IntVar(root, 0) #라디오 버튼값을 저장하는 정수형 variable 객체 생성 #tk.StringVal() 문자형 객체 Control variable
sel.set(1) #sel에 1할당(라디오 버튼에서 첫번쨰꺼) : 초기 지정

label = tk.Label(root, text="Encoding", underline=5) #라벨 생성(lebel 위젯 사용) underline은 줄 3개
label.pack() #라벨 배치

rb1=tk.Radiobutton(root, text="Choice1", variable=sel, value=1, indicatoron=1, command= Action1) #각각의 묶음 variable
rb1.pack() #버튼 배치, variable=rbvar같은 그룹 라디오동작, indicatoron=0 버튼모양 바꾸기

rb2=tk.Radiobutton(root, text="Choice2", variable=sel, value=2, indicatoron=1, command= Action2)
rb2.pack()

rb3=tk.Radiobutton(root, text="Choice3", variable=sel, value=3, indicatoron=1, command= Action3)
rb3.pack()

button=tk.Button(root, text="Print choice", command=lambda:print(sel.get()))
button.pack()

root.mainloop() #root표시'''

#슬라이더 만들기

'''import tkinter as tk

def func(scl):
        label.config(text = "value = %d" % int(scl))


root=tk.Tk()

sel=tk.IntVar()
sel.set(0) #0으로 설정

label = tk.Label(root, text="Value =%d" % sel.get()) 
label.pack()

s = tk.Scale(root, label='Scale', orient='h', from_=0,to=100, showvalue=False, variable=sel, command=func)
s.pack()

root.mainloop()'''

#텍스트 박스 만들기

'''import tkinter as tk

def func(ev): #엔터키를 눌렀을때의 동작
        label.config(text = e.get())


root=tk.Tk()

label = tk.Label(root, text="Input Text") 
label.pack()

e=tk.Entry(root) #텍스트 박스 생성
e.pack()

e.bind('<Return>',func) #ev 생성

root.mainloop()'''

#문제
'''import tkinter as tk

def func(ev): #엔터키를 눌렀을때의 동작
        label.config(text = e.get())


root=tk.Tk()

label = tk.Label(root, text="Input Text") 
label.pack()

e=tk.Entry(root) #텍스트 박스 생성
e.pack()

#e.bind('<>',func)
btn=tk.Button(root, text="Print")
btn.bind('<Button-1>',func) #내가 한것.
btn.pack()

root.mainloop()'''

#김씨가 한거
'''import tkinter as tk

def func(): #ev(이벤트가 빠짐
        label.config(text = e.get())


root=tk.Tk()

label = tk.Label(root, text="Input Text") 
label.pack()

e=tk.Entry(root) #텍스트 박스 생성
e.pack()

#e.bind('<>',func)
btn=tk.Button(root, text="Print", command=func)
btn.pack()

root.mainloop()'''

#계산기 만들기

'''import tkinter as tk

def func(): #ev(이벤트가 빠짐
    if sel.get()==1:
        result=int(e1.get())+int(e2.get())
    elif sel.get()==2:
        result=int(e1.get())-int(e2.get())
    elif sel.get()==3:
        result=int(e1.get())*int(e2.get())
    elif sel.get()==4:
        if int(e2.get())==0:
            label.config(text = "0으로 나눌 수 없습니다")
            return
        else:
            result=int(e1.get())/int(e2.get())
    f_result = "%.2f" % result
    label.config(text = f_result)

    if sel.get()==3 and int(e2.get())==0:
        label.config(text = "0으로 나눌 수 없습니다")
    else:
        result=eval(e1.get()+operator[i]+e2.get())
        f_result = "%.2f" % result
        label.config(text = f_result)
        

root=tk.Tk()
root.geometry('300x200') #윈도우 창 크기 변경

e1=tk.Entry(root) #텍스트 박스 생성
e1.pack()

e2=tk.Entry(root) #텍스트 박스 생성
e2.pack()

sel=tk.IntVar()
sel.set(1)
#sel이 한 세트임. 그래서 sel.get()하면 value값이 나옴
rt1=tk.Radiobutton(root, text="Button +", indicatoron=1, value=1, variable=sel)
rt1.pack()

rt2=tk.Radiobutton(root, text="Button -", indicatoron=1, value=2, variable=sel)
rt2.pack()

rt3=tk.Radiobutton(root, text="Button *", indicatoron=1, value=3, variable=sel)
rt3.pack()

rt4=tk.Radiobutton(root, text="Button /", indicatoron=1, value=4, variable=sel)
rt4.pack()

#for문을 돌려서 라인 줄이기가 가능함
radios=[]
operator=["+","-","*","/"]
for i in range(4):
    radio_=tk.Radiobutton(root, text="Button %s" % operator[i], variable= sel, value=i+1)
    radios.append(radio_)
    radios[i].pack()

btn=tk.Button(root, text="Result", command=func)
btn.pack()

label = tk.Label(root, text="결과 표시창")
label.pack()

root.mainloop()'''

#배치해보기

'''import tkinter as tk
window = tk.Tk()
window.title("Educoding&IT")
window.geometry("320x400+100+100") #창 크기
window.resizable(False,False) #창 고정

b1=tk.Button(window, text="(50,50)") #가로 세로 위치
b2=tk.Button(window, text="(50,100)")
b3=tk.Button(window, text="(100,150)")
b4=tk.Button(window, text="(0,200)")
b5=tk.Button(window, text="(0,300)")
b6=tk.Button(window, text="(0,300)")

b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50) #폭 과 높이
b3.place(x=100, y=150, bordermode="inside") #bordermode 안에....
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx = 0.5) #x좌표의 배치 비율 (0~1)
b6.place(x=0, y=300, relx =0.5, anchor="s") #anchor 위젯의 기준위치

window.mainloop()'''

#계산기 만들기

'''import tkinter as tk

window = tk.Tk()
window.title("계산기")
window.geometry("400x210") #창 크기
window.resizable(False,False) #창 고정

def monter(tm):
    global stri
    stri=stri+tm
    label.config(text = stri)

def zero():
    global stri
    label.config(text = "0")
    stri=""

def calc():
    global stri
    result=eval(stri)
    label.config(text = result)
    stri=""

label = tk.Label(window, text="")
label.pack()
sel=tk.StringVar()
stri=" "
    
b1=tk.Button(window, text="1", command=lambda:monter('1')) #람다를 이용해서 button값 가져오
b2=tk.Button(window, text="2", command=lambda:monter('2'))
b3=tk.Button(window, text="3", command=lambda:monter('3'))
b4=tk.Button(window, text="4", command=lambda:monter('4'))
b5=tk.Button(window, text="5", command=lambda:monter('5'))
b6=tk.Button(window, text="6", command=lambda:monter('6'))
b7=tk.Button(window, text="7", command=lambda:monter('7'))
b8=tk.Button(window, text="8", command=lambda:monter('8'))
b9=tk.Button(window, text="9", command=lambda:monter('9'))
bc=tk.Button(window, text="c", command=zero)
b0=tk.Button(window, text="0", command=lambda:monter('0'))
bm=tk.Button(window, text="=" ,command=calc)
p1=tk.Button(window, text="+", command=lambda:monter('+'))
p2=tk.Button(window, text="-", command=lambda:monter('-'))
p3=tk.Button(window, text="*", command=lambda:monter('*'))
p4=tk.Button(window, text="/", command=lambda:monter('/'))


b1.place(x=50, y=50,width=50, height=25)
b2.place(x=130, y=50, width=50, height=25) 
b3.place(x=210, y=50, width=50, height=25) 
b4.place(x=50, y=90, width=50, height=25)
b5.place(x=130, y=90, width=50, height=25)
b6.place(x=210, y=90, width=50, height=25)
b7.place(x=50, y=130, width=50, height=25)
b8.place(x=130, y=130, width=50, height=25)
b9.place(x=210, y=130, width=50, height=25)
bc.place(x=50, y=170, width=50, height=25)
b0.place(x=130, y=170, width=50, height=25)
bm.place(x=210, y=170, width=50, height=25)
p1.place(x=290, y=50, width=50, height=25)
p2.place(x=290, y=90, width=50, height=25)
p3.place(x=290, y=130, width=50, height=25)
p4.place(x=290, y=170, width=50, height=25)

window.mainloop()'''


import requests
import json

city = "Seoul"
apikey = "31e60ed232c94ed4631da50ad6ce08ed"
lang = "kr"
# units - metric
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

# 지역 : name
print(data["name"],"의 날씨입니다.")










