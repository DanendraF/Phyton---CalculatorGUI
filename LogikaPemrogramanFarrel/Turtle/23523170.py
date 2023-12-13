import turtle

def draw_letter(letter, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(letter, align="center", font=("Arial", 50, "normal"))
    turtle.penup()

def draw_background():
    turtle.bgcolor("#F0D917")
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-400, 300)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
    turtle.penup()

def draw_star():
    turtle.color("#FFFFFF")
    turtle.penup()
    turtle.goto(-50, -300)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

# Draw background
draw_background()

# F
draw_letter("F", -320, 0)

# A
draw_letter("A", -200, 0)

# R
draw_letter("R", -70, 0)

# R
draw_letter("R", 70, 0)

# E
draw_letter("E", 200, 0)

# L
draw_letter("L", 320, 0)

# Draw star
draw_star()

turtle.done()