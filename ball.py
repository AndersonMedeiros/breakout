import turtle


# função para criar a bola
def create_ball(shape, color, xcor, ycor):
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape(shape)
    ball.color(color)
    ball.penup()
    ball.goto(xcor, ycor)
    ball.dx = 1
    ball.dy = 3
    return ball

# função para movimentar a bola
def movement_ball(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
