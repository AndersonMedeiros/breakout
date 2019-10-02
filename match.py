import aux
import intro
import os
import random
import time
import turtle
import math

# criando a bola
ball = aux.drawn_sprites('circle', '#E0FFFF', 0, 0)
speed_ball = 0.5


# definir por onde a bola começa a se mover
def set_ball():
    ball.goto(0, 200)
    possibily = random.randint(1, 2)
    if possibily == 1:
        direction_angle(285)
    else:
        direction_angle(255)


# movimentação da bola
def movement_ball(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# ângulo de direção da bola
def direction_angle(angle):
    ball.dx = speed_ball * math.cos(math.radians(angle))
    ball.dy = speed_ball * math.sin(math.radians(angle))


# criando a raquete
wid_paddle = 0.7
len_paddle = 5
TAM_ONE_SEG = (len_paddle*10)/4
paddle = aux.drawn_sprites('square', '#191970', 0, 0)
paddle.shapesize(stretch_wid=wid_paddle, stretch_len=len_paddle)


# movimentação da raquete
def move_paddle_left():
    x = paddle.xcor()
    if x > -290:
        x -= 30
    else:
        x = -290
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 290:
        x += 30
    else:
        x = 290
    paddle.setx(x)


# criando o painel da vida
life_board = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_board = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e os painéis
def game_over():
    ball.hideturtle()
    global speed_ball
    speed_ball = 1
    set_ball()

    paddle.hideturtle()
    paddle.goto(0, -310)

    life_board.clear()
    life_board.goto(150, 270)
    global life
    life = 3

    score_board.clear()
    score_board.goto(-130, 270)
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
        life_board.clear()
        aux.write_message(life_board, 'Life: 3', 20)

    # ajustando o painel da pontuação
    global score
    if score == 0:
        score_board.clear()
        aux.write_message(score_board, 'Score: 0', 20)

    # movimentando a bola
    movement_ball(ball)

    # colisão com a parede esquerda
    if ball.xcor() < -340:
        os.system('arts/aplay bounce.wav&')
        ball.setx(-340)
        ball.dx *= -1

    # colisão com a parede direita
    if ball.xcor() > 340:
        os.system('arts/aplay bounce.wav&')
        ball.setx(340)
        ball.dx *= -1

    # colisão com a parede superior
    if ball.ycor() > 340:
        os.system('arts/aplay bounce.wav&')
        ball.sety(340)
        ball.dy *= -1

    # colisão com a parede inferior
    if ball.ycor() < -340:
        life -= 1
        life_board.clear()
        aux.write_message(life_board, 'Life: {}'.format(life), 20)
        os.system('arts/aplay arcade-bleep-sound.wav&')
        global speed_ball
        speed_ball = 1
        set_ball()

    # colisão com a raquete
    if ball.ycor() < -292 and ball.xcor() < paddle.xcor() + 50 and \
            ball.xcor() > paddle.xcor() - 50:
        if ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 4 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 3:
            print(speed_ball)
            direction_angle(30)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 3 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 2:
            print(speed_ball)
            direction_angle(45)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 2 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * 1:
            print(speed_ball)
            direction_angle(60)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 1 and \
                ball.xcor() > paddle.xcor() + TAM_ONE_SEG * 0:
            print(speed_ball)
            direction_angle(85)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 1 and \
                ball.xcor() == paddle.xcor() + TAM_ONE_SEG * 0:
            print(speed_ball)
            direction_angle(90)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * 0 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -1:
            print(speed_ball)
            direction_angle(100)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -1 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -2:
            print(speed_ball)
            direction_angle(120)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -2 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -3:
            print(speed_ball)
            direction_angle(135)
        elif ball.xcor() < paddle.xcor() + TAM_ONE_SEG * -3 and \
                ball.xcor() >= paddle.xcor() + TAM_ONE_SEG * -4:
            print(speed_ball)
            direction_angle(150)

        speed_ball += 0.1
        os.system('arts/aplay bounce.wav&')

    # fim de jogo (quantidade de vidas zerada)
    if life == 0:
        life_board.goto(0, 30)
        aux.write_message(life_board, 'GAME OVER', 40)
        score_board.goto(0, -30)
        aux.write_message(score_board, 'Final score: {}'.format(score), 30)
        time.sleep(3)
        intro.playing = False
