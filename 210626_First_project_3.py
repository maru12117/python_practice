
import tkinter as tk
import requests
import json

members={"hhp":['홍훈표','1234'], "jeju":['제주시','1256'], "seoul":['서울이','1278']} #회원명단

def join():
    members[user_id_entry2.get()] = [user_name_entry2.get(), user_pw_entry2.get()]
    print("안녕하세요 %s님 회원가입이 완료되었습니다" % user_name_entry2.get())
    print(members)
    user_id_entry2.delete(0, "end")
    user_name_entry2.delete(0, "end")
    user_pw_entry2.delete(0, "end")
    return show_frame(frame1) #로그인 창으로 이동

def search_password(): #비밀번호 찾기
    if user_id_research.get() in members and members[user_id_research.get()][0]==user_name_research.get():
        label_information3.config(text="비밀번호는 %s 입니다" % members[user_id_research.get()][1])
        user_id_research.delete(0, "end")
        user_name_research.delete(0, "end")
    else:
        label_information3.config(text="존재하지 않는 ID입니다")

def management(): #모든 회원들을 출력함
    if user_id_entry1.get()=="yaya" and user_pw_entry1.get()=="1598":
        user_id_entry1.delete(0, "end")
        user_pw_entry1.delete(0, "end")
        return show_frame(frame6)
    else:
        label_information1.config(text="접근 금지")

survey_id=""
def log_in(): #로그인
    if user_id_entry1.get() in members and user_pw_entry1.get()==members[user_id_entry1.get()][1]:
        print("로그인 성공")
        label_information1.config(text="로그인 성공")
        global survey_id
        survey_id=user_id_entry1.get() #해당 id를 설문조사할때 사용함
        user_id_entry1.delete(0, "end")
        user_pw_entry1.delete(0, "end")
        return show_frame(frame4)
    else:
        label_information1.config(text="비밀번호를 다시입력해주세요")

survey={'hhp':['리조트','일본','해외 여행 의향 있음', '감사합니다'], 'jkd':['리조트','미국','해외 여향 의향 없음',"안녕하세요"]} #예시 1
global_nation=""
def report(): #설문조사
    global survey_id
    survey[survey_id]=[vacation.get(),nation.get(),plan.get(),""]
    global global_nation
    global_nation=nation.get()
    print(global_nation)
    return show_frame(frame5)

def send_message(): #관리자에게 메세지
    global survey_id
    survey[survey_id][3]=write_subject.get("1.0","end").strip("\n") #텍스트 박스 처음부터 끝까지
    print(survey)
    return information_weather()

city="Seoul"
def information_weather():
    global global_nation
    print(global_nation)
    global city
    if global_nation=="제주도":
        city = "Seoul"
    elif global_nation=="미국":
        city = "Washington"
    elif global_nation=="일본":
        city = "Tokyo"
    elif global_nation=="태국":
        city = "Bangkok"
    elif global_nation=="대만":
        city = "Taipei"
    print(city)
    apikey = "31e60ed232c94ed4631da50ad6ce08ed"  #api 활용
    lang = "kr"
    api = f"""http://api.openweathermap.org/data/2.5/\
    weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
    result = requests.get(api)
    data = json.loads(result.text)
    weather1= tk.Label(frame7, text="%s의 현재 날씨는 %s, %s" % (global_nation,data["weather"][0]["main"],data["weather"][0]["description"]))
    weather1.pack()
    weather1.place(x=120, y=140)

    weather2= tk.Label(frame7, text="%s의 현재 온도는 %d도이며 최저기온 %d도, 최고기온 %d도입니다" % (global_nation,data["main"]["temp"], data["main"]["temp_min"],data["main"]["temp_max"]))
    weather2.pack()
    weather2.place(x=120, y=180)

    weather3=tk.Label(frame7, text="%s의 현재 기압은 %d이며 강풍은 %.2fm/s로 불고 있습니다 " % (global_nation,data["main"]["pressure"], data["wind"]["speed"]))
    weather3.pack()
    weather3.place(x=120, y=220)
    
    return show_frame(frame7)

def result_show():
    list_manage=[]
    i=0
    z=0
    for x,y in survey.items():
        manage_=tk.Label(frame6,text="{0}님의 설문조사 결과는 {1} 여행을 가고싶어하며, {2}으로 여행지를 선택하였습니다. 현재 {3} 관리자에게 {4} 라며 메세지를 전달함".format(x, y[0],y[1],y[2],y[3]))
        list_manage.append(manage_)
        list_manage[i].pack()
        list_manage[i].place(x=100, y=150+z)
        i+=1
        z+=40

def show_frame(frame): #프레임을 씌우겠다.
    global city
    global global_nation
    print(city)
    frame.tkraise()
    
root=tk.Tk()
root.title("[온라인 설문조사]")
root.state("zoomed")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frame1=tk.Frame(root) #로그인창
frame2=tk.Frame(root) #회원가입창
frame3=tk.Frame(root) #비밀번호 찾기 창
frame4=tk.Frame(root) #설문조사 창
frame5=tk.Frame(root) #관리자에게 건의사항 메일 보내기
frame6=tk.Frame(root) #관리자 프로그램
frame7=tk.Frame(root) #마지막 국가정보 제공

for frame in (frame1, frame2, frame3, frame4, frame5,frame6, frame7):
    frame.grid(row=0, column=0, sticky="nsew")
    
#===========Frame Code1====================
show_frame(frame1) #첫번째 창 frame1을 보여줌
label = tk.Label(frame1, text="[로그인] 코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
label.pack()
label.place(x=80, y=50)

label_id=tk.Label(frame1,text="ID")
label_id.pack()
label_id.place(x=100, y=100)


label_pw=tk.Label(frame1,text="pw")
label_pw.pack()
label_pw.place(x=100, y=150)

user_id_entry1=tk.Entry(frame1, bg="light blue")
user_id_entry1.pack()
user_id_entry1.place(x=150, y=100, width=250, height=25)
user_pw_entry1=tk.Entry(frame1, bg="light blue")
user_pw_entry1.pack()
user_pw_entry1.place(x=150, y=150, width=250, height=25)

btn_join=tk.Button(frame1,text="회원가입", command=lambda:show_frame(frame2)) #누르면 frame2로 이동
btn_join.pack()
btn_join.place(x=70, y=200, width=80, height=25)

btn_login=tk.Button(frame1,text="로그인", command=log_in)
btn_login.pack()
btn_login.place(x=170, y=200, width=80, height=25)

btn_search=tk.Button(frame1,text="pw 찾기", command=lambda:show_frame(frame3))
btn_search.pack()
btn_search.place(x=270, y=200, width=80, height=25)

btn_manager=tk.Button(frame1,text="관리자", command=management)
btn_manager.pack()
btn_manager.place(x=370, y=200, width=80, height=25)

label_information1=tk.Label(frame1)
label_information1.pack()
label_information1.place(x=230, y=250)

#================Frame2=========================== 회원 가입창

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

user_id_entry2=tk.Entry(frame2)
user_id_entry2.pack()
user_id_entry2.place(x=150, y=100, width=250, height=25)
user_name_entry2=tk.Entry(frame2)
user_name_entry2.pack()
user_name_entry2.place(x=150, y=150, width=250, height=25)
user_pw_entry2=tk.Entry(frame2)
user_pw_entry2.pack()
user_pw_entry2.place(x=150, y=200, width=250, height=25)

btn_join=tk.Button(frame2,text="회원가입", command=join)
btn_join.pack()
btn_join.place(x=180, y=250, width=80, height=25)

btn_back=tk.Button(frame2,text="돌아가기", command=lambda:show_frame(frame1))
btn_back.pack()
btn_back.place(x=280, y=250, width=80, height=25)

#================Frame3=================================== pw찾기

label = tk.Label(frame3, text="[비밀번호 찾기] 아이디와 이름을 입력해주세요")
label.pack()
label.place(x=80, y=50)

label_id_research=tk.Label(frame3,text="ID")
label_id_research.pack()
label_id_research.place(x=100, y=100)

label_name_research=tk.Label(frame3,text="이름")
label_name_research.pack()
label_name_research.place(x=100, y=150)

user_id_research=tk.Entry(frame3, bg="light blue")
user_id_research.pack()
user_id_research.place(x=150, y=100, width=250, height=25)

user_name_research=tk.Entry(frame3, bg="light blue")
user_name_research.pack()
user_name_research.place(x=150, y=150, width=250, height=25)


btn_pw1=tk.Button(frame3,text="pw찾기", command=search_password) #비밀번호 찾기
btn_pw1.pack()
btn_pw1.place(x=170, y=200, width=80, height=25)

btn_return=tk.Button(frame3,text="돌아가기", command=lambda:show_frame(frame1))
btn_return.pack()
btn_return.place(x=270, y=200, width=80, height=25)

label_information3=tk.Label(frame3)
label_information3.pack()
label_information3.place(x=230, y=250)

#================Frame4=================================== 설문조사 실시    
label = tk.Label(frame4, text="[설문조사] 코로나 백신 여권 소유시, 가장 가고싶은 여행지 조사")
label.pack()
label.place(x=80, y=50)

vacation=tk.StringVar()
nation=tk.StringVar()
plan=tk.StringVar()
vacation.set(0)
nation.set(0)
plan.set(0)

label_place=tk.Label(frame4,text="이번 휴가때 가장 가고싶은 곳은 어디입니까?")
label_place.pack()
label_place.place(x=100, y=100)

rb_vac1=tk.Radiobutton(frame4, text="도심 휴양지", variable=vacation, value="도심 휴양지", indicatoron=1)
rb_vac1.pack()
rb_vac1.place(x=120, y=130)

rb_vac2=tk.Radiobutton(frame4, text="바닷가", variable=vacation, value="바닷가", indicatoron=1)
rb_vac2.pack()
rb_vac2.place(x=120, y=160)

rb_vac3=tk.Radiobutton(frame4, text="산과 계곡", variable=vacation, value="산과 계곡", indicatoron=1)
rb_vac3.pack()
rb_vac3.place(x=120, y=190)

rb_vac4=tk.Radiobutton(frame4, text="리조트", variable=vacation, value="리조트", indicatoron=1)
rb_vac4.pack()
rb_vac4.place(x=120, y=220)


label_nation=tk.Label(frame4,text="코로나 백신 여권을 소유하신다면 여행하고 싶은 국가는 어디입니까?")
label_nation.pack()
label_nation.place(x=100, y=300)

rb_nation1=tk.Radiobutton(frame4, text="미국", variable=nation, value="미국", indicatoron=1)
rb_nation1.pack()
rb_nation1.place(x=120, y=330)

rb_nation2=tk.Radiobutton(frame4, text="일본", variable=nation, value="일본", indicatoron=1)
rb_nation2.pack()
rb_nation2.place(x=120, y=360)

rb_nation3=tk.Radiobutton(frame4, text="대만", variable=nation, value="대만", indicatoron=1)
rb_nation3.pack()
rb_nation3.place(x=120, y=390)

rb_nation4=tk.Radiobutton(frame4, text="태국", variable=nation, value="태국", indicatoron=1)
rb_nation4.pack()
rb_nation4.place(x=120, y=420)

rb_nation5=tk.Radiobutton(frame4, text="제주도(해외여행 의향 없음)", variable=nation, value="제주도", indicatoron=1)
rb_nation5.pack()
rb_nation5.place(x=120, y=450)

label_plan=tk.Label(frame4,text="2021년에 해외여행을 갈 계획이 있으십니까?")
label_plan.pack()
label_plan.place(x=100, y=530)

rb_plan1=tk.Radiobutton(frame4, text="해외여행 의향 있음", variable=plan, value="해외여행 의향 있음", indicatoron=1)
rb_plan1.pack()
rb_plan1.place(x=120, y=560)

rb_plan2=tk.Radiobutton(frame4, text="해외여행 의향 없음", variable=plan, value="해외여행 의향 없음", indicatoron=1)
rb_plan2.pack()
rb_plan2.place(x=120, y=590)

label_mention1=tk.Label(frame4,text="설문에 응해주셔서 감사합니다")
label_mention1.pack()
label_mention1.place(x=200, y=670)

btn_report=tk.Button(frame4,text="제출" ,command=report)
btn_report.pack()
btn_report.place(x=250, y=720, width=80, height=25)

#================Frame5=================================== 관리자에게 전하고 싶은 메세지

label = tk.Label(frame5, text="[요구사항] 본 설문에 대한 애로사항 및 요구사항을 관리자에게 전달해주세요")
label.pack()
label.place(x=80, y=50)

write_subject=tk.Text(frame5) #텍스트 박스
write_subject.pack()
write_subject.place(x=80, y=100, width=450, height=350)

btn_send=tk.Button(frame5,text="보내기" ,command=send_message)
btn_send.pack()
btn_send.place(x=250, y=470, width=80, height=25)

#================Frame6=================================== 관리자 통계파일

label = tk.Label(frame6, text="[관리자 프로그램] 설문조사에 응답한 결과")
label.pack()
label.place(x=80, y=50)

btn_return1=tk.Button(frame6,text="돌아가기" ,command=lambda:show_frame(frame1))
btn_return1.pack()
btn_return1.place(x=350, y=50, width=80, height=25)

btn_result1=tk.Button(frame6,text="설문결과" , command=result_show) #결과 보기 클릭
btn_result1.pack()
btn_result1.place(x=450, y=50, width=80, height=25)

#================Frame7=================================== 마지막 정보제공 단계

btn_return2=tk.Button(frame7,text="감사합니다" ,command=lambda:show_frame(frame1))
btn_return2.pack()
btn_return2.place(x=250, y=470, width=80, height=25)
    

label = tk.Label(frame7, text="[국가 정보 제공] 여행지 정보를 제공합니다")
label.pack()
label.place(x=80, y=50)

information_nation1=tk.Label(frame7,text="※ 날씨 정보 확인하기")
information_nation1.pack()
information_nation1.place(x=100, y=100)

btn_weather=tk.Button(frame7,text="날씨 정보")
btn_weather.pack()
btn_weather.place(x=350, y=100, width=80, height=25)




root.mainloop()

    








