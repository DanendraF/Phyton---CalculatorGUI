import turtle  
t = turtle.Turtle()  

t.speed(2)
t.fillcolor("red")

t.shape("turtle")  

t.begin_fill()  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.end_fill()  

t.fillcolor("yellow")

t.shape("arrow")  


t.begin_fill()  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.end_fill()  

t.fillcolor("blue")

t.shape("circle")

t.begin_fill()  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.lt(120)  
t.fd(100)  
t.end_fill()  
turtle.mainloop()  
