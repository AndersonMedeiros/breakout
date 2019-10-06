import aux
import intro
import math
import os
import time
import turtle


# criando a bola
ball = aux.drawn_sprites('circle', '#E0FFFF', 0, 0)


# definir por onde a bola começa a se mover
def set_ball():
    global speed_ball
    speed_ball = 3
    ball.goto(0, 0)
    direction_angle(270)


# ângulo de direção da bola
def direction_angle(angle):
    ball.dx = speed_ball * math.cos(math.radians(angle))
    ball.dy = speed_ball * math.sin(math.radians(angle))


# criando a raquete
TAM_ONE_SEG = (5*10)/4
paddle = aux.drawn_sprites('square', '#191970', 0, 0)
paddle.shapesize(stretch_wid=0.7, stretch_len=5)


# movimentação da raquete
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
global brick_matrix
brick_matrix = []
colors = ['#FF6347', '#E9967A', '#F0E68C', '#00FF7F',
          '#40E0D0', '#1E90FF', '#7B68EE', '#EE82EE']
grown = [15, 12, 10, 8, 5, 3, 2, 1]
y = 250
for line in range(8):
    x = -300
    brick_matrix.append([])
    for column in range(9):
        brick = aux.drawn_sprites('square', colors[line], x, y)
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick_matrix[line].append(brick)
        x += 75
    y -= 25


# criando o painel da vida
life_hud = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_hud = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e, os blocos os painéis
def game_over():

    ball.hideturtle()
    set_ball()

    paddle.hideturtle()
    paddle.goto(0, -310)

    for line in range(8):
        for column in range(9):
            brick_matrix[line][column].hideturtle()

    life_hud.clear()
    life_hud.goto(150, 270)
    global life
    life = 3

    score_hud.clear()
    score_hud.goto(-130, 270)
    global score
    score = 0


# criando o jogo
def start_game():

    # mostrando a bola e a raquete
    ball.showturtle()
    paddle.showturtle()

    # ajustando o painel da vida
    global life
    if life == 3:
        life_hud.clear()
        aux.write_message(life_hud, 'Life: 3', 20)

    # ajustando o painel da pontuação
    global score
    if score == 0:
        score_hud.clear()
        aux.write_message(score_hud, 'Score: 0', 20)
        # mostrando os blocos
        for line in range(8):
            for column in range(9):
                brick_matrix[line][column].showturtle()

    # movimentando a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com a parede esquerda
    if ball.xcor() < -340:
        os.system('aplay arts/bounce.wav&')
        ball.setx(-340)
        ball.dx *= -1

    # colisão com a parede direita
    if ball.xcor() > 340:
        os.system('aplay arts/bounce.wav&')
        ball.setx(340)
        ball.dx *= -1

    # colisão com a parede superior
    if ball.ycor() > 340:
        os.system('aplay arts/bounce.wav&')
        ball.sety(340)
        ball.dy *= -1

    # colisão com a parede inferior
    if ball.ycor() < -340:
        life -= 1
        life_hud.clear()
        aux.write_message(life_hud, 'Life: {}'.format(life), 20)
        os.system('aplay arts/arcade-bleep-sound.wav&')
        set_ball()

    # colisão com a raquete
    if ball.ycor() < -292 and ball.xcor() < paddle.xcor() + 50 and \
            ball.xcor() > paddle.xcor() - 50:
        if ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 4 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 3:
            direction_angle(30)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 3 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 2:
            direction_angle(45)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 2 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 1:
            direction_angle(60)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 1 and \
                ball.xcor() > paddle.xcor() + TAM_ONE_SEG * 0:
            direction_angle(85)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 1 and \
                ball.xcor() == paddle.xcor() + TAM_ONE_SEG * 0:
            direction_angle(90)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 0 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -1:
            direction_angle(100)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -1 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -2:
            direction_angle(120)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -2 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -3:
            direction_angle(135)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -3 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -4:
            direction_angle(150)
        os.system('aplay arts/bounce.wav&')

    # colisão com os blocos
    for line in range(8):
        for column in range(9):
            posy = brick_matrix[line][column].ycor()
            posx = brick_matrix[line][column].xcor()
            if ((ball.ycor() >= posy - 12 and ball.ycor() <= posy + 12 or
               ball.ycor() == posy) and (ball.xcor() > posx - 35 and
               ball.xcor() < posx + 35 or ball.xcor() == posx)):
                if brick_matrix[line][column].isvisible():
                    ball.dy *= -1
                    global speed_ball
                    speed_ball += grown[line]*0.05
                    score += grown[line]
                    score_hud.clear()
                    aux.write_message(score_hud, 'Score: {}'.format(score), 20)
                    os.system('aplay arts/bounce.wav&')
                brick_matrix[line][column].hideturtle()

    # fim de jogo (zero vida e pontuação máxima)
    if life == 0 or score == 504:
        life_hud.goto(0, 30)
        if life == 0:
            aux.write_message(life_hud, 'GAME OVER', 40)
        elif score == 504:
            aux.write_message(life_hud, 'YOU WIN!', 40)
        score_hud.goto(0, -30)
        aux.write_message(score_hud, 'Final score: {}'.format(score), 30)
        time.sleep(5)
        intro.playing = False
