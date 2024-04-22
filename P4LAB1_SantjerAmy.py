#this program creates a triangle and a square using turtle
import turtle
t = turtle.Turtle()

#draws a square
for _ in range(4):
    t.forward(100)
    t.left(90)
        
#draws a triangle 
for _ in range(1):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
