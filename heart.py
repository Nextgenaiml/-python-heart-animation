import turtle
import math
import time

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

# ---------------- TURTLE ----------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# ---------------- HEART ----------------
def heart_x(a):
    return 16 * math.sin(a) ** 3

def heart_y(a):
    return (
        13 * math.cos(a)
        - 5 * math.cos(2 * a)
        - 2 * math.cos(3 * a)
        - math.cos(4 * a)
    )

# ---------------- SETTINGS ----------------
N = 400

# Multiple hearts
scales = [
    18,
    17,
    16,
    15,
    14,
    13,
    12,
    11,
    10,
    9
]

# Slow drawing
point_delay = 0.012

# Bright colors
colors = [
    (1.0, 0.05, 0.25),
    (1.0, 0.08, 0.35),
    (1.0, 0.12, 0.45),
    (1.0, 0.18, 0.55),
    (1.0, 0.25, 0.65),
    (1.0, 0.35, 0.75),
    (1.0, 0.45, 0.85),
    (1.0, 0.60, 0.92),
    (1.0, 0.75, 0.97),
    (1.0, 0.90, 1.0)
]

# ---------------- DRAW MULTIPLE HEARTS ----------------
for heart_number, scale in enumerate(scales):

    t.color(colors[heart_number])

    t.penup()

    for i in range(N + 1):

        angle = (i / N) * 2 * math.pi

        x = heart_x(angle) * scale
        y = heart_y(angle) * scale

        t.goto(x, y)

        if i == 0:
            t.pendown()

        screen.update()

        # Slow drawing
        time.sleep(point_delay)

    t.penup()

# ---------------- FINISH ----------------
turtle.done()