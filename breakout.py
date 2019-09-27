import os
from time import sleep
import turtle


# Funcao para criar a janela (screen)
def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("black")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen

# Funcao para criar o turtle das raquetes
def create_paddle(x, y, width, height, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=width, stretch_len=height)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

# Funcao para criar o turtle da bola
def create_ball(x, y, color):
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color(color)
    ball.penup()
    ball.goto(x, y)
    ball.dx = 0.5
    ball.dy = 0.5
    return ball

def create_hud(x,y):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(x, y)
    return hud

