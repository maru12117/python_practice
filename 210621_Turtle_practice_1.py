#거북이 대포 게임

import turtle as t
import math
screen=t.getscreen()
t.shape("turtle")

t.fd(300)
t.back(150)
#이곳부터 라인 시작
t1x = t.xcor()
t1y = t.ycor()
print(t1x, t1y)
t.pencolor('green')
t.pensize(3)
t.back(80)
t2x = t.xcor()
t2y = t.ycor()
print(t2x,t2y)
#여기까지가...골인라인
t.pencolor("black")
t.pensize(1)
t.back(500)
start=t.position()
print(start)
t.up()
def up() :
    t.left(15)
def down() :
    t.right(15)
def play() :
    t.fd(300)
    t.rt(86)
    t.fd(400)
    t3x = t.xcor()
    t3y = t.ycor()
    print(t3x,t3y)
    if t2x<=t3x<=t1x:
        print("pass!")
    t.goto(-430.00,0.00)

screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(play, "Right")
screen.listen()
t.goto(-430.00,0.00)
