#연습문제
#.jpg와 .png를 구하세요
'''files=['font','1.png','10.jpg','11.gif','2.jpg', '3.png','table.xsls','spec.docx']

print(list(filter(lambda x: x[-3:]=='jpg' or x[-3:]=='png',files)))'''

#심화문제 : 파일 이름을 한꺼번에 바꾸기
text=input("숫자.파일명으로 입력하세요 : ").split()
a = list(map(lambda x:"%03s" % x,text))
print(a)
