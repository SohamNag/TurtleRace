import random
from turtle import Turtle, Screen

turtle_list = []
color_list = ["red", "orange", "yellow", "green", "blue", "violet"]
ycoord = [-200, -120, -40, 40, 120, 200]
screen = Screen()
race = True
screen.setup(1000, 700, 250, 50)
pred = screen.textinput("Predict winner !", "Enter the colour of turtle : ")
for tur_num in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.resizemode("user")
    new_turtle.shapesize(3, 3)
    new_turtle.shape("turtle")
    new_turtle.color(color_list[tur_num])
    new_turtle.goto(-450, ycoord[tur_num])
    turtle_list.append(new_turtle)

while race:

    for turtles in turtle_list:
        step = random.randint(1, 10)
        turtles.forward(step)
        if turtles.xcor() > 440:
            win = turtles.pencolor()
            print(f"The winner is {win} turtle.")
            if pred == win:
                print("You won !!")
            else:
                print("Unfortunately you lost.")
            race = False
            break
screen.exitonclick()
