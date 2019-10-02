import aux
import intro
import math
import os
import random
import time
import turtle

# criando a bola
ball = aux.drawn_sprites('circle', '#E0FFFF', 0, 0)


# definir por onde a bola começa a se mover
def set_ball():
    global speed_ball
    speed_ball = 2
    ball.goto(0, 0)
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


# criando os blocos
def create_brick(color):
    brick = aux.drawn_sprites('square', color, 0, 0)
    brick.shapesize(stretch_wid=0.7, stretch_len=2)
    return brick


# criando as linhas de blocos
global brick_list
brick_list = []


def brick_wall():
    y_position = 240
    for ycolor in range(4):
        x_position = -260
        for _ in range(6):
            if ycolor == 0:
                colory = 'Red'
            elif ycolor == 1:
                colory = 'Purple'
            elif ycolor == 2:
                colory = 'Blue'
            elif ycolor == 3:
                colory = 'Green'
            brick = create_brick(colory)
            brick.goto(x_position, y_position)
            brick_list.append(brick)
            x_position += 100
        y_position -= 40


# função para criar e mostrar os blocos
brick_wall()
global brick_len
brick_len = len(brick_list)


def hide_bricks():
    for item in range(brick_len):
        brick_list[item].hideturtle()


def show_bricks():
    for item in range(brick_len):
        brick_list[item].showturtle()


# criando o painel da vida
life_board = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_board = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e os painéis
def game_over():
    global brick_on
    brick_on = list(range(1, 25))
    hide_bricks()

    ball.hideturtle()
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
        show_bricks()

    # movimentando a bola
    movement_ball(ball)

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
        life_board.clear()
        aux.write_message(life_board, 'Life: {}'.format(life), 20)
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

    # definindo colisão com os blocos
    if ball.ycor() > 119.3 and ball.ycor() < 120.7:
        xpos = -260
        for item in range(18, 24):
            if ball.xcor() > xpos-20 and ball.xcor() < xpos+20:
                if (brick_on[item] != 0):
                    brick_list[item].hideturtle()
                    score += 1
                    ball.dy *= -1
                    score_board.clear()
                    aux.write_message(score_board, 'Score: ' + str(score), 20)
                    brick_on[item] = 0
                    os.system('aplay arts/bounce.wav&')
            xpos += 100

    if ball.ycor() > 159.3 and ball.ycor() < 160.7:
        xpos = -260
        for item in range(12, 18):
            if ball.xcor() > xpos-20 and ball.xcor() < xpos+20:
                if (brick_on[item] != 0):
                    brick_list[item].hideturtle()
                    score += 3
                    ball.dy *= -1
                    score_board.clear()
                    aux.write_message(score_board, 'Score: ' + str(score), 20)
                    brick_on[item] = 0
                    os.system('aplay arts/bounce.wav&')
            xpos += 100

    if ball.ycor() > 199.3 and ball.ycor() < 200.7:
        xpos = -260
        for item in range(6, 12):
            if ball.xcor() > xpos-20 and ball.xcor() < xpos+20:
                if (brick_on[item] != 0):
                    brick_list[item].hideturtle()
                    score += 5
                    ball.dy *= -1
                    score_board.clear()
                    aux.write_message(score_board, 'Score: ' + str(score), 20)
                    brick_on[item] = 0
                    os.system('aplay arts/bounce.wav&')
            xpos += 100

    if ball.ycor() > 239.3 and ball.ycor() < 240.7:
        xpos = -260
        for item in range(0, 6):
            if ball.xcor() > xpos-20 and ball.xcor() < xpos+20:
                if (brick_on[item] != 0):
                    brick_list[item].hideturtle()
                    score += 7
                    ball.dy *= -1
                    score_board.clear()
                    aux.write_message(score_board, 'Score: ' + str(score), 20)
                    brick_on[item] = 0
                    os.system('aplay arts/bounce.wav&')
            xpos += 100

    # fim de jogo (todos os blocos foram destruídos)
    if score == 96:
        life_board.goto(0, 30)
        aux.write_message(life_board, 'YOU WIN!', 40)
        score_board.goto(0, -30)
        aux.write_message(score_board, 'Final score: {}'.format(score), 30)
        time.sleep(3)
        intro.playing = False

    # fim de jogo (quantidade de vidas zerada)
    if life == 0:
        life_board.goto(0, 30)
        aux.write_message(life_board, 'GAME OVER', 40)
        score_board.goto(0, -30)
        aux.write_message(score_board, 'Final score: {}'.format(score), 30)
        time.sleep(3)
        intro.playing = False
