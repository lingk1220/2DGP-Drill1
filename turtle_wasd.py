import turtle
import random

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
    
def move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
    
def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()


turtle.shape('turtle')
turtle.speed(5)
turtle.listen()
turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(reset, 'Escape')

turtle.mainloop()
