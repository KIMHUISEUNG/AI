from turtle import *
import random

#%% target 난수 생성
targetX = (random.randint(-10, 10)) * 10
targetY = (random.randint(-10, 10)) * 10

mypen=Turtle()

#%% 울타리 그리기
mypen.penup()
mypen.pencolor("black")
mypen.setposition(-100,-100)
mypen.pendown()
for x in range(4):
    mypen.forward(200)
    mypen.left(90)
    
#%% 출발 지점 표시
mypen.penup()
mypen.pen(pencolor="blue", pensize=10)
mypen.setpos(0,0)
mypen.pendown()
mypen.setpos(0,0)

#%% 목표 지점 표시
mypen.penup()
mypen.pen(pencolor="red", pensize=10)
mypen.setpos(targetX,targetY)
mypen.pendown()
mypen.setpos(targetX,targetY)

#%% 거북이 설정
mypen.penup()
mypen.pen(pencolor="black", pensize=1)
mypen.setpos(0,0)
mypen.speed(10)
mypen.shape("turtle")
mypen.pendown()

print("시작점 : ",mypen.pos())
print("목표 : " + "[" + str(targetX) + "," + str(targetY) + "]")

#%% 거북이 움직임 기록
number=0

while True:
    posX = round(mypen.xcor())
    posY = round(mypen.ycor())
    
    if posX == targetX and posY == targetY:
        print("총"+str(number)+"의 움직임 발생")
        break
    
    number += 1
    rand = random.randint(0, 3)
    
    if(rand==0):
        rotate = 0
    elif(rand==1):
        rotate = 90
    elif(rand==2):
        rotate = 180
    else:
        rotate = 270
    mypen.seth(rotate)
    
#%% 울타리 범위 벋어나지 못하게 한다.

    if(posX >= 100 and mypen.heading()==0): #동쪽
        continue
    elif(posY <= -100 and mypen.heading()==270): #남쪽
        continue
    elif(posX <= -100 and mypen.heading()==180): #북쪽
        continue
    elif(posY >= 100 and mypen.heading()==90): #서쪽
        continue
    else:
        mypen.forward(10)