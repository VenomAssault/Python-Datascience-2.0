from turtle import *
from random import randint, choice
squares = 0
speed = ('fastest')
while squares < 10:
    x = randint(-300, 300)
    y = randint(-300, 300)
    size = randint(50,100)
    penup()
    goto(x,y)
    pendown()
    colors = ['red','green','violet','blue','brown']
    fillcolor(choice(colors))
    begin_fill()
    for i in range (4):
        fd (100)
        rt(90)
        circle(size/2)
    end_fill()
    squares += 1
hideturtle()
mainloop()