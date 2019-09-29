import turtle
import tkinter


def move_paddle_left():
    while True:
        x = paddle.xcor()
        if x > -300:
            x -= 0.005
        else:
            x = -300
        paddle.setx(x)

def move_paddle_right():
    while True:
        x = paddle.xcor()
        if x < 300:
            x += 0.005
        else:
            x = 300
        paddle.setx(x)

paddle = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('#000000')
screen.setup(width=700, height=700)
screen.tracer(100)


paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=0.5, stretch_len=4)
paddle.penup()
paddle.color("pink")
paddle.goto(0,-310)



while True:

    screen.listen()

    screen.onkeypress(move_paddle_left, 'a')
    screen.onkeypress(move_paddle_right, 'd')
    
    paddle.penup()
    paddle.color("pink")
    paddle.goto(0,-310)
 
    screen.update()