import turtle as t

t.shape('turtle')

'''t.pencolor('Blue')
t.fillcolor("Red")
t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill()'''
#삼각형 만들기
t.pensize(3)
t.penup()
t.goto(-200,-50)
t.pendown()
t.circle(40, steps = 3) #반지름이 40인 원에 내각하는 3각형

#사각형 만들기
t.penup()
t.goto(-100,-50)
t.pendown()
t.circle(40, steps = 4)

#5각형 만들기
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(40, steps = 5)

#6각형 만들기
t.penup()
t.goto(100,-50)
t.pendown()
t.circle(40, steps = 6)


#원만들기
t.penup()
t.goto(200,-50)
t.pendown()
t.circle(40) #반지름이 40인 원을 만들기

