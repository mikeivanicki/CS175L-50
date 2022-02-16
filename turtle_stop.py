#Michael Ivanicki
#CS 175 - 50L
#turtle_stop

import math
import turtle

Window_Width=400
Window_Height=400
Animation_Speed=0
Num_Sides=8
Length=100
Angle=45
Text_X=-5
Text_Y=-10

turtle.setup(Window_Width, Window_Height)

s=Length
x = s / math.sqrt(2)
diameter= s + (2 * x)

turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
for x in range (Num_Sides):
    turtle.forward(Length)
    turtle.left(Angle)

turtle.penup()
turtle.goto(-20,10)
turtle.write('STOP', font=20)
turtle.hideturtle()

