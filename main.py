from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400, startx=2000)

width = screen.window_width()
x = (-width / 2) + 30

height = screen.window_height()
y = (-height / 2) + 25

selection = screen.textinput(title="Make your bet", prompt="Which turtle🐢 will win? Yellow, Orange, Red, Purple, Blue, or Green: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for color in colors:
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(color)
  new_turtle.penup()

  y  += 50

  new_turtle.goto(x, y)
  all_turtles.append(new_turtle)


if selection:
  is_race_on = True

while is_race_on:

  for turtle in all_turtles:
    if turtle.xcor() >= 215:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == selection:
        print(f"You won! The {winning_color} turtle is the winner of the race! 🏆")
      else:
        print(f"Sorry, the winner is the {winning_color} turtle. Better luck next time!")

  for turtle in all_turtles:
    movespeed = random.randint(0, 5)
    turtle.forward(movespeed)

screen.exitonclick()