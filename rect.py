import turtle

Turtle = turtle.Turtle()
Turtle.speed(100)

x = -500
y = 400

def Rect(x, y):
    Turtle.setheading(0)
    Turtle.penup()
    Turtle.color("black")
    Turtle.fillcolor("black")
    Turtle.goto(x,y)
    Turtle.begin_fill()
    Turtle.forward(100)
    Turtle.left(90)
    
    Turtle.forward(100)
    Turtle.left(90)
    
    Turtle.forward(100)
    Turtle.left(90)
    
    Turtle.forward(100)
    Turtle.left(90)
    Turtle.end_fill()
    Turtle.pendown()
    
    
for i in range(5):
    x+=120
    y = -400
    for j in range(5):
        y+=120
        Rect(x, y)


turtle.exitonclick()
