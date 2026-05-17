# Event listener

#from turtle import Turtle, Screen

#tim = Turtle()

#screen = Screen()

#def move_forwards():
 #   tim.forward(10)

#screen.listen()
#screen.onkey(key="space", fun=move_forwards)


#screen.exitonclick()

# Higher order function in Python

#def add(n1, n2):
 #   return n1 +n2

#def substract(n1, n2):
 #   return n1 - n2

#def multiply(n1, n2):
 #   return n1 * n2

#def divide(n1, n2):
 #   return n1 / n2

#def calculator(n1, n2, func):
 #   return func(n1, n2)


#result = calculator(5, 5, divide)
#print(result)

# Etch_Sketch Project

#from turtle import Turtle, Screen

#tim = Turtle()

#def move_forwards():
 #   tim.forward(10)

#def move_backwards():
 #   tim.backward(10)

#def turn_left():
 #   new_heading = tim.heading() + 10
 #   tim.setheading(new_heading)  

#def turn_right():
 #   new_heading = tim.heading() - 10
 #   tim.setheading(new_heading)


#def clear():
 #   tim.clear()
 #   tim.penup()
 #   tim.home()
 #   tim.pendown()

#screen = Screen()

#screen.listen()
#screen.onkey(move_forwards, "f")
#screen.onkey(move_backwards, "b")
#screen.onkey(turn_left, "l")
#screen.onkey(turn_right, "r")
#screen.onkey(clear, "c")

#screen.exitonclick()


# Object State and instances

#timmy.color = "green"(state)

#tommy.color = "purple"(state)

# Understanding the Turtle Coordinate System

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "yellow", "purple", "green", "blue", "orange"]

y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
