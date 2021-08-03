totalSting="the grown-ups' response, this time. was to advise me to lay aside my drawings of boa constrictors. whether from the inside or the outside, and devote myself instead to geography, history, arithemetic, and grammar. that is why, at the, age of six, I gave up what might have been a magnificent carreer as a painter. I had been disheatrened by the failure of my Drawing Number One and my Drawing Number Two Growns-up never understand anything by themselvese and it is tiresome for children to be always and forever explaining thing to the"
searchingString=input("찾을 문자열을 입력하세여 : ")
#첫번쨰 방법은 리스트로 다 나눠서 the를 찾아내서 바꾼다
#대신 이렇게하면...'the,'이었던 객체를 찾을 수가 없음
print(totalSting)
totalStingList=totalSting.split()
i=0
while True:
    stringIndex=totalStingList.index(searchingString) #해당 인덱스가 나옴
    i+=1
    totalStingList[stringIndex]="x"
    if searchingString not in totalStingList:
        break
print(i)

#print(searchingString in totalSting)

#두번쨰 방법은 그냥 문자열로 확인하기(실패)
'''while True:
    stringIndex=totalSting.find(searchingString)
    
    if searchingString not in totalSting:
        break
print("ho")'''




