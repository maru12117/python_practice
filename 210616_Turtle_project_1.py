import turtle as t
import random
import math

#math.sqrt
'''print(3.1622776601683795*3.1622776601683795)
print(math.sqrt(10))'''
swidth = 300
sheight = 300
t.screensize(swidth, sheight)
t.setup(width = swidth+200, height=sheight +200)
t1 = t.Turtle('turtle')
t2 = t.Turtle('turtle')
t3 = t.Turtle('turtle')
t1.speed(0)
t2.speed(0)
t3.speed(0)
t1.up()
t2.up()
t3.up()
t1.color("red")
t1.goto(100,100)
t2.color("green")
t2.goto(200,200)
t3.color("blue")
t3.goto(100,200)

while True:
    angle1=random.randint(0,360)
    dist1=random.randint(1,50)
    angle2=random.randint(0,360)
    dist2=random.randint(1,50)
    angle3=random.randint(0,360)
    dist3=random.randint(1,50)
    t1.fd(dist1)
    t1.rt(angle1)
    t2.fd(dist2)
    t2.rt(angle2)
    t3.fd(dist3)
    t3.rt(angle3)

t1x = t1.xcor()
t1y = t1.ycor()
t2x = t2.xcor()
t2y = t2.ycor()
t3x = t3.xcor()
t3y = t3.ycor()

#화면 밖으로 나가면 다시 원위치
if not((-swidth /2 <= t1x and t1x <= swidth/2) and (-sheight /2 <= t1y and t1y <= sheight/2)):
    t1.goto(100,100)
if not((-swidth /2 <= t2x and t2x <= swidth/2) and (-sheight /2 <= t2y and t2y <= sheight/2)):
    t2.goto(200,200)
if not((-swidth /2 <= t3x and t3x <= swidth/2) and (-sheight /2 <= t3y and t3y <= sheight/2)):
    t3.goto(100,200)

#두 거북이다 만났을때 도장찍는 부분
if math.sqrt((t1x-t2x)*(t1x-t2x)) +((t1y-t2y)*(t1y-t2y)) <=100:
    t1.stamp()
    t2.stamp()
if math.sqrt((t1x-t3x)*(t1x-t3x)) +((t1y-t3y)*(t1y-t3y)) <=100:
    t1.stamp()
    t3.stamp()
if math.sqrt((t3x-t2x)*(t3x-t2x)) +((t3y-t2y)*(t3y-t2y)) <=100:
    t2.stamp()
    t3.stamp()


