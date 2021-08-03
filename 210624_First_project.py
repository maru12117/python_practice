#간단한 회원가입을 시작함
'''user_id : 사용자 아이디
user_name : 사용자 이름
user_pw : 비밀번호'''

import tkinter as tk

members={"hhp":['홍훈표',1234], "jeju":['제주시',1256], "seoul":['서울이',1278]} #회원명단

def join_1():
    label_title=tk.Label(root, text="[회원가입] 코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
    label_title.pack()
    label_title.place(x=80, y=50)

    label_id1=tk.Label(root,text="ID")
    label_id1.pack()
    label_id1.place(x=100, y=100)

    label_name1=tk.Label(root,text="이름")
    label_name1.pack()
    label_name1.place(x=100, y=150)

    label_pw1=tk.Label(root,text="pw")
    label_pw1.pack()
    label_pw1.place(x=100, y=200)

    user_id_entry1=tk.Entry(root)
    user_id_entry1.pack()
    user_id_entry1.place(x=150, y=100, width=250, height=25)
    user_name_entry1=tk.Entry(root)
    user_name_entry1.pack()
    user_name_entry1.place(x=150, y=150, width=250, height=25)
    user_pw_entry1=tk.Entry(root)
    user_pw_entry1.pack()
    user_pw_entry1.place(x=150, y=200, width=250, height=25)

    btn_join1=tk.Button(root,text="회원가입", command=join)
    btn_join1.pack()
    btn_join1.place(x=250, y=250, width=80, height=25)

    print(user_id_entry1.get())
    print(user_name_entry1.get())
    print(user_pw_entry1.get())

    btn_join.destroy()
    btn_login.destroy()
    btn_manager.destroy()
    label_information.destroy()
    user_id_entry.destroy()
    user_pw_entry.destroy()
    
def join():
    members[user_id_entry1.get()] = [user_name_entry1.get(), user_pw_entry1.get()]
    print("안녕하세요 %s님 회원가입이 완료되었습니다" % user_name_entry1.get())
    print(members)

def management(): #모든 회원들을 출력함
    if user_id_entry.get()=="yaya" and int(user_pw_entry.get())==1598:
        print("관리자 프로그램입니다")
        label_information.config(text="관리자 프로그램 실행")
        for x in members:
            print("Id : {0}, 이름: {1}, 비밀번호: {2}".format(x, members[x][0], members[x][1]))
    else:
        label_information.config(text="접근 금지")


def log_in(): #로그인
    if user_id_entry.get() in members and int(user_pw_entry.get())==members[user_id_entry.get()][1]:
        print("로그인 성공")
        label_information.config(text="로그인 성공")
        btn_out=tk.Button(root,text="완료")
        btn_out.pack()
        btn_out.place(x=230, y=200, width=80, height=25)
        
        
    else:
        print("로그인 실패")
        label_information.config(text="비밀번호를 다시입력해주세요")

root=tk.Tk()
root.geometry("500x400+100+100")
root.resizable(False,False)
root.title("[온라인 설문조사]")
label_title=tk.Label(root, text="코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
label_title.pack()
label_title.place(x=80, y=50)

label_id=tk.Label(root,text="ID")
label_id.pack()
label_id.place(x=100, y=100)

label_pw=tk.Label(root,text="pw")
label_pw.pack()
label_pw.place(x=100, y=150)

user_id_entry=tk.Entry(root)
user_id_entry.pack()
user_id_entry.place(x=150, y=100, width=250, height=25)
user_pw_entry=tk.Entry(root)
user_pw_entry.pack()
user_pw_entry.place(x=150, y=150, width=250, height=25)

btn_join=tk.Button(root,text="회원가입", command= join_1)
btn_join.pack()
btn_join.place(x=130, y=200, width=80, height=25)

btn_login=tk.Button(root,text="로그인", command=log_in)
btn_login.pack()
btn_login.place(x=230, y=200, width=80, height=25)

btn_manager=tk.Button(root,text="관리자" ,command =management)
btn_manager.pack()
btn_manager.place(x=330, y=200, width=80, height=25)



label_information=tk.Label(root)
label_information.pack()
label_information.place(x=230, y=250)

root.mainloop()

    








