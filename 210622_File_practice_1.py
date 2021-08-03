'''inFp = open("C:/data/data1.txt","r",encoding="utf-8")
inStr = inFp.readline()
print(inStr, end="")
inStr = inFp.readline()
print(inStr, end="")
inStr = inFp.readline()
print(inStr, end="")
inStr = inFp.readline()
print(inStr, end="")
inFp.close()'''

'''inFp=None
inStr="" #빈 문자열을 생성
inFp=open("C:/data/data1.txt","r",encoding="utf-8") #오픈 열고
while True:
    inStr = inFp.readline() #읽기
    if inStr=="": #읽는 str이 ""일떄까지 계속 읽음
        break
    print(inStr, end="") #그대로 print함
inFp.close() #파일을 꼭 닫아줘야함'''

'''inFp=open("C:/data/data1.txt","r",encoding="utf-8")
inList=[]
inList=inFp.readlines() #readlines의 경우는 모든 리스트형식으로 넣음
for x in inList:
    print(x, end="")
inFp.close()'''

'''filename=input("파일명을 입력하세요 : ")
inFp=None
instr=""
inFp=open(filename,"r",encoding="utf-8")
while True:
    instr=inFp.readline() #먼저 읽어줘야함
    if instr=="":
        break
    print(instr, end="")
inFp.close()'''

'''outFp = None
outStr = ""
outFp=open("data2.txt","w",encoding='utf-8')
while True:
    outStr=input("내용 입력 : ")
    if outStr != "":
        outFp.write(outStr+"\n")
    else:
        break
outFp.close()
print("정상적으로 파일에 써졌음")'''

#연습문제(복사본 만들기)
'''filename=input("파일명을 입력하세요 : ")
inFp=None
instr=""
outstr=""
inFp=open(filename,"r",encoding="utf-8") #파일을 읽어드리는 객체
outFp=open("data2_copy.txt","w",encoding="utf-8") #파일을 쓰는 객체
while True:
    instr=inFp.readline() #먼저 읽어줘야함
    outFp.write(instr) #읽은 것을 그대로 쓰여짐
    if instr=="":
        break
print("복사가 완료되었습니다")
inFp.close()
outFp.close()'''

'''filename=input("파일명을 입력하세요 : ")
inFp=None
instr=""
outstr=""
inFp=open(filename,"r",encoding="utf-8") #파일을 읽어드리는 객체
outFp=open("data2_copy.txt","w",encoding="utf-8") #파일을 쓰는 객체
inList=inFp.readlines() #for문을 돌릴떄는 lines()
for inStr in inList :
    outFp.write(inStr)
inFp.close()
outFp.close()
print("복사완료")'''

'''filename=input("파일명을 입력하세요 : ")
inFp=None
instr=""
outstr=""
inFp=open(filename,"r",encoding="utf-8") #파일을 읽어드리는 객체
outFp=open("data2_copy.txt","w",encoding="utf-8") #파일을 쓰는 객체
inList=inFp.readlines() 
outFp.writelines(inList) #읽기,쓰기 모두 lines를 써서 그대로 갖다 붙이기
inFp.close()
outFp.close()
print("복사완료")'''

#파일 암호화 및 해독 프로그램

#ord() : 문자의 고유한 숫자를 알려줌
#chr() : 숫자에 해당하는 문자를 알려줌

#변수선언
inFp, outFp=None, None
inStr, outStr="",""
i=0
secu=0

#메인코드 부분
'''secuYN= input("1.암호화 2.암호 해석 중 선택 : ")
inFname = input("입력 파일명을 입력하세요 : ")
outFname = input("출력 파일명을 입력하세요 : ")

inFp=open(inFname,"w",encoding="utf-8")
OutFp=open(outFname,"r",encoding="utf-8")

if secuYN =="1":
    secu=100
elif secuYN=="2":
    secu=-100
    
while True:
    inStr=input("암호를 입력해주세요 : ")
    inStr_ord=str(ord(inStr)+secu)
    inFp.write(inStr_ord)
        outStr=OutfFp.readline()
        outStr_chr=chr(int(outStr)+secu)
        if outStr==" ":
            break
        print(outStr_chr, end=" ")
        
inFp.close()
outFp.close()'''

secuYN= input("1.암호화 2.암호 해석 중 선택 : ")
inFname = input("입력 파일명을 입력하세요 : ")
outFname = input("출력 파일명을 입력하세요 : ")

inFp=open(inFname,"r",encoding="utf-8")
outFp=open(outFname,"w",encoding="utf-8")

if secuYN =="1":
    secu= 100
elif secuYN=="2":
    secu= -100
    
while True:
    inStr=inFp.readline()
    if not inStr: #inStr에 아무것도 없으면 break
        break

    outStr=""
    for i in range(0,len(inStr)):
        ch=inStr[i]
        chNum=ord(ch) #숫자로 변환
        chNum=chNum+secu
        ch2=chr(chNum)
        outStr = outStr+ch2

    outFp.write(outStr)
        
inFp.close()
outFp.close()

    
    




















