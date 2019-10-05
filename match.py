import aux
import intro
import math
import os
import random
import time
import turtle


# criando a bola
ball = aux.drawn_sprites('circle', '#E0FFFF', 0, 0)
speed_ball = 3


# definir por onde a bola começa a se mover
def set_ball():
    global speed_ball
    speed_ball = 1
    ball.goto(0, -50)
    possibily = random.randint(1, 2)
    if possibily == 1:
        direction_angle(285)
    else:
        direction_angle(255)


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


# criando os blocos e colocando-os numa matriz 5x7
global brick_list
brick_list = []
colors = ['#FF6347', '#E9967A', '#F0E68C', '#00FF7F',
          '#40E0D0', '#1E90FF', '#7B68EE']
grown = [10, 8, 5, 4, 3, 2, 1]
y = 250
for linha in range(7):
    x = -300
    brick_list.append([])
    for coluna in range(9):
        brick = aux.drawn_sprites('square', colors[linha], x, y)
        brick.shapesize(stretch_wid=0.6, stretch_len=3)
        brick_list[linha].append(brick)
        x += 75
    y -= 15


# criando os blocos
# def create_brick(color):
#    brick = aux.drawn_sprites('square', color, 0, 0)
#    brick.shapesize(stretch_wid=0.7, stretch_len=2)
#    return brick

# criando as linhas de blocos
# global brick_list
# brick_list = []

# def brick_wall():
#    y_position = 240
#    for ycolor in range(4):
#        x_position = -260
#        for _ in range(6):
#            if ycolor == 0:
#                colory = 'Red'
#            elif ycolor == 1:
#                colory = 'Purple'
#            elif ycolor == 2:
#                colory = 'Blue'
#            elif ycolor == 3:
#                colory = 'Green'
#            brick = create_brick(colory)
#            brick.goto(x_position, y_position)
#            brick_list.append(brick)
#            x_position += 100
#        y_position -= 40

# função para criar e mostrar os blocos
# brick_wall()
# global brick_len
# brick_len = len(brick_list)

# def hide_bricks():
#    for item in range(brick_len):
#        brick_list[item].hideturtle()

# def show_bricks():
#    for item in range(brick_len):
#        brick_list[item].showturtle()


# criando o painel da vida
life_hud = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_hud = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e, os blocos os painéis
life = 3
score = 0


def game_over():
    # global brick_on
    # brick_on = list(range(1, 25))
    # hide_bricks()

    ball.hideturtle()
    set_ball()

    paddle.hideturtle()
    paddle.goto(0, -310)

    for linha in range(7):
        for coluna in range(9):
            brick_list[linha][coluna].hideturtle()

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
        for linha in range(7):
            for coluna in range(9):
                brick_list[linha][coluna].showturtle()
        # show_bricks()

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
    for linha in range(7):
        for coluna in range(9):
            posy = brick_list[linha][coluna].ycor()
            posx = brick_list[linha][coluna].xcor()
            if ((ball.ycor() >= posy - 8 and ball.ycor() <= posy + 8 or
               ball.ycor() == posy) and (ball.xcor() > posx - 35 and
               ball.xcor() < posx + 35 or ball.xcor() == posx)):
                if brick_list[linha][coluna].isvisible():
                    ball.dy *= -1
                    global speed_ball
                    speed_ball += grown[linha]*0.1
                    score += grown[linha]
                    score_hud.clear()
                    aux.write_message(score_hud, 'Score: {}'.format(score), 20)
                brick_list[linha][coluna].hideturtle()

    # definindo colisão com os blocos
    '''if ball.ycor() > 119.3 and ball.ycor() < 120.7:
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
            xpos += 100'''

    # fim de jogo (zero vida e pontuação máxima)
    if life == 0 or score == 105:
        life_hud.goto(0, 30)
        if life == 0:
            aux.write_message(life_hud, 'GAME OVER', 40)
        elif score == 105:
            aux.write_message(life_hud, 'YOU WIN!', 40)
        score_hud.goto(0, -30)
        aux.write_message(score_hud, 'Final score: {}'.format(score), 30)
        time.sleep(2)
        intro.playing = False
