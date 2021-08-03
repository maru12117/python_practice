
import tkinter as tk

members={"hhp":['홍훈표',1234], "jeju":['제주시',1256], "seoul":['서울이',1278]} #회원명단

def join():
    members[user_id_entry.get()] = [user_name_entry.get(), user_pw_entry.get()]
    print("안녕하세요 %s님 회원가입이 완료되었습니다" % user_name_entry.get())
    print(members)

def search_password(user_id_search, user_name_search):
    if user_id_search in members and members[user_id_search][0] ==user_name_search:
        print("비밀번호는 %d 입니다" % members[user_id_search][1])

def management(): #모든 회원들을 출력함
    if user_id_entry.get()=="yaya" and int(user_pw_entry.get())==1598:
        show_frame(frame2)
        for x in members:
            print("Id : {0}, 이름: {1}, 비밀번호: {2}".format(x, members[x][0], members[x][1]))
    else:
        label_information.config(text="접근 금지")


def log_in(): #로그인
    print(user_id_entry.get())
    if user_id_entry.get() in members and int(user_pw_entry.get())==members[user_id_entry.get()][1]:
        print("로그인 성공")
        label_information.config(text="로그인 성공")
        
    else:
        label_information.config(text="비밀번호를 다시입력해주세요")

def show_frame(frame): #프레임을 씌우겠다.
    frame.tkraise()
    
root=tk.Tk()
root.state("zoomed")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frame1=tk.Frame(root) #로그인창
frame2=tk.Frame(root) #회원가입창
frame3=tk.Frame(root) #

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")
    
#===========Frame Code1====================
show_frame(frame1) #첫번째 창 frame1을 보여줌
label = tk.Label(frame1, text="코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
label.pack()
label.place(x=80, y=50)

label_id=tk.Label(frame1,text="ID")
label_id.pack()
label_id.place(x=100, y=100)


label_pw=tk.Label(frame1,text="pw")
label_pw.pack()
label_pw.place(x=100, y=150)

user_id_entry=tk.Entry(frame1, bg="light blue")
user_id_entry.insert(0,"아이디를 입력해주세요")
user_id_entry.pack()
user_id_entry.place(x=150, y=100, width=250, height=25)
user_pw_entry=tk.Entry(frame1)
user_pw_entry.pack()
user_pw_entry.place(x=150, y=150, width=250, height=25)

btn_join=tk.Button(frame1,text="회원가입", command=lambda:show_frame(frame2)) #누르면 frame2로 이동
btn_join.pack()
btn_join.place(x=70, y=200, width=80, height=25)

btn_login=tk.Button(frame1,text="로그인", command=log_in)
btn_login.pack()
btn_login.place(x=170, y=200, width=80, height=25)

btn_search=tk.Button(frame1,text="pw 찾기")
btn_search.pack()
btn_search.place(x=270, y=200, width=80, height=25)

btn_manager=tk.Button(frame1,text="관리자", command=management)
btn_manager.pack()
btn_manager.place(x=370, y=200, width=80, height=25)

label_information=tk.Label(frame1)
label_information.pack()
label_information.place(x=230, y=250)

#================Frame2===========================

label_title=tk.Label(frame2, text="[회원가입] 코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
label_title.pack()
label_title.place(x=80, y=50)

label_id=tk.Label(frame2,text="ID")
label_id.pack()
label_id.place(x=100, y=100)

label_name=tk.Label(frame2,text="이름")
label_name.pack()
label_name.place(x=100, y=150)

label_pw=tk.Label(frame2,text="pw")
label_pw.pack()
label_pw.place(x=100, y=200)

user_id_entry=tk.Entry(frame2)
user_id_entry.pack()
user_id_entry.place(x=150, y=100, width=250, height=25)
user_name_entry=tk.Entry(frame2)
user_name_entry.pack()
user_name_entry.place(x=150, y=150, width=250, height=25)
user_pw_entry=tk.Entry(frame2)
user_pw_entry.pack()
user_pw_entry.place(x=150, y=200, width=250, height=25)

btn_join=tk.Button(frame2,text="회원가입")
btn_join.pack()
btn_join.place(x=180, y=250, width=80, height=25)

btn_back=tk.Button(frame2,text="돌아가기", command=lambda:show_frame(frame1))
btn_back.pack()
btn_back.place(x=280, y=250, width=80, height=25)

root.mainloop()

    








