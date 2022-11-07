import turtle
win = turtle.Screen()

fInitial = turtle.Turtle()
fInitial.color("red")
fInitial.pensize(5)
fInitial.shape("turtle")

sInitial = turtle.Turtle()
sInitial.color("blue")
sInitial.pensize(3)
sInitial.shape("turtle")

fInitial.right(90)
fInitial.forward(100)
fInitial.left(90)
fInitial.forward(60)

sInitial.penup()
sInitial.forward(170)
sInitial.pendown()

sInitial.right(180)
sInitial.forward(60)
sInitial.left(90)
sInitial.forward(50)
sInitial.left(90)
sInitial.forward(60)
sInitial.right(90)
sInitial.forward(50)
sInitial.right(90)
sInitial.forward(60)

win.mainloop()

