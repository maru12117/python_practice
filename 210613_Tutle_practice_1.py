import turtle as t

'''n = 6
t.shape('turtle')
t.color('#FFFF00')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()'''

'''n=90
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(120) #반지름이 120인 원형을 만들기
    t.rt(360/n)'''
a, b=map(int,input("입력 : ").split())
t.shape('arrow')
t.speed(5)
for i in range(a):
    t.fd(b)
    t.rt((360/a)*2)
    t.fd(b)
    t.lt(360/a)

