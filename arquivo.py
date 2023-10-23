from turtle import *


color('green')
bgcolor('black')
speed(10)
hideturtle()

setup(width=1000, height=800)

b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b += 1

done()





