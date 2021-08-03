#파일 사용하기(파일쓰기)
'''file=open("hello.txt","w",encoding="utf-8")
file.write("Hello, world")
file.close()'''

#파일 읽기
'''file=open("hello.txt","r",encoding="utf-8")
readline=file.readline()
print(readline)
file.close()'''

#자동으로 close()하기
'''with open("hello.txt","a",encoding="utf-8") as file:
    file.write("Hi, Python, I am ami") #들여쓰기 해야함'''

'''with open("hello.txt","r",encoding="utf-8") as file:
    read=file.readline()
    print(read)'''

#문자열 여러줄을 파일에 쓰기
'''with open("hello.txt","w",encoding="utf-8") as file:
    for i in range(3):
        file.write("Hi, cyworld %s" % "안녕\n")'''

#리스트에 들어있는 문자열을 파일에 쓰기
'''lines=["안녕하세요\n","파이썬\n","나랑 놀아주어\n"]
with open("hello.txt","w",encoding='utf-8') as file:
    file.writelines(lines) #문자열을 그대로 넣음'''

#파일의 내용을 한 줄씩 리스트로 가져오기
'''with open("hello.txt","r",encoding='utf-8') as file:
    readlines=file.readlines()
    print(readlines)'''

#파일의 내용을 한줄씩 순차적으로 가져오기(while문 사용)
'''with open("hello.txt","r",encoding='utf-8') as file:
    readline=None
    while True:
        readline=file.readline()
        if readline=="": #만약에 아무것도 없으면 끝
            break
        print(readline.strip('\n')) #줄바꿈 없애서 출력함'''

#for문 사용
'''with open("hello.txt","r",encoding='utf-8') as file:
    for x in file: #open한 file을 돌림
        print(x.strip('\n'))'''

#파이썬 객체를 파일에 저장하기, 가져오기

import pickle

'''name="james"
age=17
address="서울시 서초구"
scores={'korean':90,'english':95,'mathematic':85,'science':82}
with open("james.p","wb") as file: #바이너리 쓰기 모드인 wb로 열기(사람도 읽기 어려운 p파일)
    pickle.dump(name, file) file에 객체를 넣어서 값도 같이 집어넣음
    pickle.dump(age, file)
    pickle.dump(address,file)
    pickle.dump(scores, file)'''

#사람도 읽기어려운 pickle파일을 읽기

'''with open('james.p',"rb") as file: #바이너리 읽기모드 "rb"=read binary
    name=pickle.load(file)
    age=pickle.load(file)
    address=pickle.load(file)
    scores=pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)'''

#연습문제
'''with open("hello.txt","r",encoding="utf-8") as file:
    i=0
    while True:
        word=file.readline()
        if len(word)>10:
            i+=1
            print(word.strip('\n'))
        elif word=="":
            break
        else:
            continue
print(i)'''
with open("hello.txt","r",encoding="utf-8") as file:
    lines=file.readlines()
    c_lines=lines[0].replace(",","").replace(".","")
    lines_list=c_lines.split(" ") #모든 문자열을 나눔....
    for x in lines_list:
        if "c" in x:
            print(x)


    











