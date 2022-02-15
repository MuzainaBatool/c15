import turtle
side = int(input('enter the valuefor side'))
if side >= 200:
    for i in range(0, 3):
        turtle.forward(side)
        turtle.left(120)
else:
    turtle.circle(side)
