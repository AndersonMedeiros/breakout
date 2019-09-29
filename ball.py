import turtle


# função para criar a bola
def create_ball(shape, color, xcor, ycor):
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape(shape)
    ball.color(color)
    ball.penup()
    ball.goto(xcor, ycor)
