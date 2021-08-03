#text 타자게임
#기능추가
''' 1. 모든 게임의 결과를 파일로 저장
    2.저장시 YYYYMMDD_NO(20120301.xtx)
    3.날짜별로 저장
    4. 저장시 저장시간 : 30초(13/23/15 : 30초)형태로 저장'''

import random
import time

timeStr=time.strftime('%Y%m%d', time.localtime(time.time()))
timeStr_today=time.strftime('%Y년 %m월 %d일', time.localtime(time.time()))
timeStr_txt=timeStr+'.txt' #시간을 담아서 txt파일명 저장
readList=[]
readStr=open("Eng_LowData.txt","r",encoding="utf-8")
writeStr=open(timeStr_txt,"w",encoding="utf-8")
readList_str=readStr.readlines()
for x in readList_str:
    if x!= "\n":
        x=x.replace("\n","")
        readList.append(x)
#print(readList) 줄바꿈 제외 완료
#print(len(readList)) 리스트 총 58개
start=input("게임을 시작합니다: (엔터)")
writeStr.writelines(timeStr_today)
writeStr.write("\n")
start=time.time()
count=0
false =0
while True:
    quiznum=random.randint(0,58)
    if count==5:
        break
    while count<5:
        print(count+1,"번 문제", readList[quiznum])
        user_str=input("타자를 입력해주세요 : ")
        writeStr.writelines(user_str)
        if user_str==readList[quiznum]:
            print("정답")
            writeStr.writelines("정답\n")
            count+=1
            break
        else:
            print("오답")
            writeStr.write("오답\n")
            false += 1
            continue
end=time.time()
et=end-start
print("오타 %d 번 경과시간 %.2f초" % (false,et))
writeStr.write("오타 %d 번 경과시간 %.2f초" % (false,et))
writeStr.write("")

readStr.close()
writeStr.close()
    
    
