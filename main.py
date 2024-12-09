from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400, startx=2000)

width = screen.window_width()
x = (-width / 2) + 30

height = screen.window_height()
y = (-height / 2) + 50

selection = screen.textinput(title="Make your bet", prompt="Which turtle will win? Yellow, Orange, Red, Purple, Blue, or Green: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x=-220, y=-150)

for color in colors:
  color = Turtle(shape="turtle")
  color.penup()

  y  += 50

  color.goto(x, y)

screen.exitonclick()