import time
import turtle
from random import randrange
turtle.left(90)
while True:
    LeftRight = int(randrange(10))
    if LeftRight > 5:
        turtle.right(randrange(45))
        turtle.forward(10)
    if LeftRight < 5:
        turtle.left(randrange(45))
        turtle.forward(10)
    if LeftRight == 5:
        turtle.forward(10)
