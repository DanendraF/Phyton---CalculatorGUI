import turtle  
t = turtle.Turtle()  

n = 50  
if n<=60:  
    t.circle(n)  
else:  
    t.forward(n)  
    t.backward(n-10)
    
n = 70  
if n<=60:  
    t.circle(n)  
else:  
    t.forward(n)  
    t.backward(n-10)

turtle.mainloop()  
