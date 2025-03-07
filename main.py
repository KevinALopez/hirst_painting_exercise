import turtle
from turtle import Turtle, Screen
import colorgram
import random

COLORS = colorgram.extract('hirst_dots.jpg', 50)

def random_color_rbg():
    """Return a random color from the COLORS list as a rgb tuple(r,g,b). Example: (154,54,255)"""
    color = random.choice(COLORS).rgb
    return color.r, color.g, color.b

turtle.colormode(255) # Needed so that turtle knows it will be working with rgb values.

t = Turtle()
s = Screen()

t.speed('fastest')

S_WIDTH = s.window_width()
S_HEIGHT = s.window_height()

GAP = 40
DOT_SIZE = 20

starting_pos = (-S_WIDTH // 2 + GAP // 2, S_HEIGHT // 2 - GAP // 2)

t.hideturtle()
t.pu()
t.setpos(starting_pos)

ROWS = S_HEIGHT // GAP
COLS = S_WIDTH // GAP

for row in range(ROWS):
    for col in range(COLS):
        t.dot(DOT_SIZE, random_color_rbg())
        t.forward(GAP)

    t.setpos(starting_pos[0], t.ycor() - GAP) # Moves turtle to next row.

turtle.mainloop()
