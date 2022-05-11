import turtle

Turtle = turtle.Turtle()
Turtle.speed(100)

def Cercle(x, y, rayon, color):
    Turtle.setheading(0)
    Turtle.penup()
    Turtle.color(color)
    Turtle.fillcolor(color)
    Turtle.goto(x,y-rayon)
    Turtle.begin_fill()
    Turtle.circle(rayon)
    Turtle.end_fill()
    Turtle.pendown()
 



Cercle(-240, 0, 25, "black") # centre
Cercle(-240, 55, 10, "grey") # haut
Cercle(-240, -55, 10, "grey") # bas
Cercle(-290, 25, 10, "grey") # gauche haut
Cercle(-290, -25, 10, "grey") # gauche bas
Cercle(-190, 25, 10, "grey") # droite haut
Cercle(-190, -25, 10, "grey") # droite bas

Cercle(-120+300, 0, 25, "black") # centre
Cercle(-120+300, 90, 40, "grey") # haut
Cercle(-120+300, -90, 40, "grey") # bas
Cercle(-200+300, 45, 40, "grey") # gauche haut
Cercle(-200+300, -45, 40, "grey") # gauche bas
Cercle(-40+300, 45, 40, "grey") # droite haut
Cercle(-40+300, -45, 40, "grey") # droite bas


turtle.exitonclick()
