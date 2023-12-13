import turtle  
t = turtle.Turtle()  

#beri judul layar
turtle.title("Ganti ukuran pena")

#atur ukuran layar
turtle.screensize()  
turtle.screensize(1000,400)  
turtle.screensize()  

t = turtle.Turtle()  

#ganti ukuran pena
t.pensize(4)  

# atur ukuran turtle  
t.shapesize(3,3,3)  
  
# warna isi  
t.fillcolor("pink")  
  
# warna pena  
t.pencolor("yellow")

t.forward(200)

# ganti warna isi & pena sekaligus
t.color("green", "red")  

t.left(90)
t.forward(200)

turtle.mainloop()  
