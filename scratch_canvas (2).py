import turtle
length = 10
#Initialize the length variable
while length <= 150:
    for i in range(0, 10):
        turtle.pencolor('red')
        turtle.forward(length)
        turtle.right(89)
        length += 0.5
        break
    turtle.pencolor('green')
    turtle.forward(length)
    turtle.right(89)
    length += 0.5
