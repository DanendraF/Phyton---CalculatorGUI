import turtle  
t = turtle.Turtle()  

turtle.bgcolor("black")  
turtle.pensize(4)
turtle.speed(10)
  
for i in range(2):  
  for colors in ["red", "green", "white"]:  
    turtle.color(colors)  
    turtle.circle(50)  
    turtle.left(70)  

turtle.mainloop()  
