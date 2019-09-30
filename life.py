import turtle


def create_life(shape, color, width, height):
    life = turtle.Turtle()
    life.speed(0)
    life.shape(shape)
    life.color(color)
    life.penup()
    life.hideturtle()
    life.goto(width, height)
    life.write("1", align="center", font=("Twlg Typo", 24, "normal"))
    return life
