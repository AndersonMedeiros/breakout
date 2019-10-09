import aux
import math
import turtle


# acelera a criação dos elementos na tela
acc = turtle.Screen()
acc.tracer(1000)


# criando a bola
ball = aux.drawn_element('circle', '#E0FFFF', 0, 0)


# bola: velocidade e movimentação iniciais
def set_ball():
    global speed_ball
    speed_ball = 1.5
    ball.goto(0, 0)
    direction_angle(270)


# bola: angulação
def direction_angle(angle):
    ball.dx = speed_ball * math.cos(math.radians(angle))
    ball.dy = speed_ball * math.sin(math.radians(angle))


# criando a raquete
TAM_ONE_SEG = (5*10)/4
paddle = aux.drawn_element('square', '#191970', 0, -310)
paddle.shapesize(stretch_wid=0.7, stretch_len=5)


# raquete: movimentação
def move_paddle_left():
    x = paddle.xcor()
    if x > -300:
        x -= 30
    else:
        x = -300
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 300:
        x += 30
    else:
        x = 300
    paddle.setx(x)


# criando os blocos e colocando-os numa matriz 8x9
brick_matrix = []
colors = ['#FF6347', '#E9967A', '#F0E68C', '#00FF7F',
          '#40E0D0', '#1E90FF', '#7B68EE', '#EE82EE']
growth = [10, 8, 7, 5, 4, 3, 2, 1]
y = 250
for line in range(8):
    x = -300
    brick_matrix.append([])
    for column in range(9):
        brick = aux.drawn_element('square', colors[line], x, y)
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick_matrix[line].append(brick)
        x += 75
    y -= 25


# criando o painel da vida
life_hud = aux.drawn_element('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_hud = aux.drawn_element('square', '#E0FFFF', -130, 270)
