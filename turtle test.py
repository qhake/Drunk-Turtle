import time
from turtle import Screen, Turtle
from random import randrange

#initialise turtle

turtle = Turtle()

# default values
max_turn = 45
turtle_steps = 10
starting_angle = 90
screen_width,screen_height=1600,900
allowance_frame = 4
allowance_toolbar = 4


#set screen size
screen = Screen()
screen.setup(screen_width + allowance_frame,screen_height + allowance_frame + allowance_toolbar) # add a bit for frame and toolbar


# Point up at start
turtle.left(starting_angle)

while True:
    LeftRight = int(randrange(10))
    if LeftRight > 5:
        turtle.right(randrange(max_turn))
        turtle.forward(turtle_steps)                
    if LeftRight < 5:
        turtle.left(randrange(max_turn))
        turtle.forward(turtle_steps)
    if LeftRight == 5:
        turtle.forward(turtle_steps)
#    tp = turtle.pos()
#    (x,y) = tp
#    print(f"x = {x} y = {y}")
#    if x < 0:
#        turtle.setx(screen_width + allowance_frame)
#    if x > screen_width + allowance_frame:
#        turtle.setx(0)
#    if y < 0:
#        turtle.sety(screen_height + allowance_frame + allowance_toolbar)
#    if y > screen_height + allowance_frame + allowance_toolbar:
#        turtle.sety(0)
