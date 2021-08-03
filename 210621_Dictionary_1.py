#학생 인적사항 관리

def register_Student():
    student_num=int(input("학번을 입력하세요 : "))
    student_name=input("이름을 입력하세요 : ")
    student_score=input("학점을 입력하세요 : ")
    student_register[student_num]=[student_name,student_score]
    return

def research_Student(student_num):
    if student_num in student_register:
            print("===========%d번 학생 조회================" % student_num)
            print("학번 : ",student_num, "이름 : ",student_register[student_num][0], "학점 : ", student_register[student_num][1])
            print()
            return
    else:
        print("학번이 존재하지 않습니다")

def update_Student(student_num):
    if student_num in student_register:
        student_name, student_score=input("수정할 이름과 점수를 입력하세요 : ").split()
        student_register[student_num][0]=student_name
        student_register[student_num][1]=student_score
        print(student_register[student_num])
        return print("수정완료되었습니다")
    else:
        print("학번이 존재하지 않습니다")

def remove_Student(student_num):
    if student_num in student_register:
        del student_register[student_num]
        return print("삭제완료되었습니다")
    else:
        print("삭제할 학번이 존재하지 않습니다")

def research_Student_total():
    print("===========전체 학생 조회================")
    for key,value in student_register.items():
        print("학번:",key, "이름:", value[0],"등급",value[1])
    
student_register={}
while True:
    print("========학생 인적사항 관리====================")
    print("1.인적사항 등록  2. 학생 검색  3. 학생수정")
    print("4.학생 삭제   5.전체학생 보기  6.프로그램 종료")
    print("==============================================")
    User_num=int(input("원하는 번호를 입력하세요 : "))
    if User_num==1:
        register_Student()
    elif User_num==2:
        student_num=int(input("학번을 입력하세요 : "))
        research_Student(student_num)
    elif User_num==3:
        student_num=int(input("수정할 학번을 입력하세요 : "))
        update_Student(student_num)
    elif User_num==4:
        student_num=int(input("삭제할 학번을 입력하세요 : "))
        remove_Student(student_num)
    elif User_num==5:
        research_Student_total()
    elif User_num==6:
        break
    else:
        print("다시 입력해주세요")
        continue

print("프로그램을 종료합니다 ")

