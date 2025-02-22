from turtle import *

def draw_bottle():
    speed(2)
    penup()
    goto(-50, -150)
    pendown()
    color("black", "lightblue")
    begin_fill()
    goto(50, -150)
    goto(50, 0)
    goto(-50, 0)
    goto(-50, -150)
    end_fill()
    penup()
    goto(-30, 0)
    pendown()
    color("black", "white")
    begin_fill()
    goto(-30, 50)
    goto(30, 50)
    goto(30, 0)
    goto(-30, 0)
    end_fill()
    penup()
    goto(-40, 50)
    pendown()
    color("black", "gray")
    begin_fill()
    goto(40, 50)
    goto(40, 70)
    goto(-40, 70)
    goto(-40, 50)
    end_fill()

    penup()
    goto(-30, 20)
    pendown()
    color("black")
    for i in range(5):
        penup()
        goto(-30, 20 + i * 4)
        pendown()
        goto(30, 20 + i * 4)

draw_bottle()
done()
