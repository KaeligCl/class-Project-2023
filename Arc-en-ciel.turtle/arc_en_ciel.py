from turtle import *

purple = '#9400D3'
indigo = '#4B0082'
blue = '#0000FF'
green = '#00FF00'
yellow = '#FFFF00'
orange = '#FF7F00'
red = '#FF0000'
color_list = [purple, indigo, blue, green, yellow, orange, red]

speed(25)
hideturtle()
up()
goto(200, 0)
down()


def semi_circle():
    x = 200
    for i in range(7):
        fillcolor(color_list[i])
        up()
        forward(-20)
        down()
        begin_fill()
        left(90)
        circle(x, 180)
        left(90)
        forward(20)
        left(90)
        x -= 20
        circle(-x, 180)
        left(90)
        forward(20)
        end_fill()


semi_circle()
done()
