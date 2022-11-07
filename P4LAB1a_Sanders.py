import turtle
win = turtle.Screen()
t = turtle.Turtle()


sides = 0
while sides < 3 :
    t.forward(100)  
    t.left(120)
    sides += 1

sides = 0
while sides < 4 :
    t.forward(50)
    t.left(90)
    sides += 1

win.mainloop()
