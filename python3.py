from turtle import *

speed('fastest')
pensize(1)
pencolor('dark blue')
penup()
goto(-500,0)
pendown()

lt(75)
spikes = 10  # Variable controls the no. of spikes
while spikes > 0:   # Loop to draw the spikes
    fd(100)
    rt(150)
    fd(100)
    lt(150)
    spikes -= 1  #decrement the spikes variable
hideturtle()
mainloop()