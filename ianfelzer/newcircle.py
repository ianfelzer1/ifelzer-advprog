import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

circle = turtle.Turtle()

circle.pensize(10)

circle.pencolor("green")

circle.circle(100)

circle.penup()

circle.setx(-300)

circle.pendown()

circle.circle(100)

window.exitonclick()
