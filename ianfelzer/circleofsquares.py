import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

ian = turtle.Turtle()

ian.pencolor("blue")

for i in range(4):
    ian.forward(50)
    ian.right(90)

for i in range(360):
    ian.speed(10)
    ian.right(1)
    ian.forward(50)
    ian.right(90)




window.exitonclick()
