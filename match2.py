import aux
import intro2
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
    speed_ball = 3
    ball.goto(0, -50)
    possibility = random.randint(1, 2)
    if possibility == 1:
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
paddle.shapesize(stretch_wid=0.7, stretch_len=5)


# movimentação da raquete
def move_paddle_left():
    x = paddle.xcor()
    if x > -290:
        x -= 10
    else:
        x = -290
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 290:
        x += 10
    else:
        x = 290
    paddle.setx(x)


# criação da matriz dos blocos
global brick_list
brick_list = []
colors = ['#FF6347', '#F0E68C', '#00FF7F', '#1E90FF', '#7B68EE']
grown = [5, 4, 3, 2, 1]
y = 250
for linha in range(5):
    x = -300
    brick_list.append([])
    for coluna in range(7):
        brick = aux.drawn_sprites('square', colors[linha], x, y)
        brick.shapesize(stretch_wid=0.6, stretch_len=3)
        brick_list[linha].append(brick)
        x += 100
    y -= 20


# criando o painel da vida
life_board = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_board = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e os painéis
def game_over():
    global brick_on
    brick_on = list(range(1, 25))
    for linha in range(5):
        for coluna in range(7):
            brick_list[linha][coluna].hideturtle()

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
        for linha in range(5):
            for coluna in range(7):
                brick_list[linha][coluna].showturtle()

    # movimentando a bola
    movement_ball(ball)

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
        set_ball()

    # colisão com os blocos
    for linha in range(5):
        for coluna in range(7):
            posy = brick_list[linha][coluna].ycor()
            posx = brick_list[linha][coluna].xcor()
            if ((ball.ycor() >= posy - 8 and ball.ycor() <= posy + 8 or
               ball.ycor() == posy) and (ball.xcor() > posx - 35 and
               ball.xcor() < posx + 35 or ball.xcor() == posx)):
                if brick_list[linha][coluna].isvisible():
                    ball.dy *= -1
                    score += grown[linha]
                    global speed_ball
                    speed_ball += grown[linha]*0.3
                    score_board.clear()
                    aux.write_message(score_board, 'Score: '+str(score), 20)
                brick_list[linha][coluna].hideturtle()

    # fim de jogo (pontuação máxima, todos os blocos destruídos)
    # fim de jogo (quantidade de vidas zerada)
    if life == 0 or score == 105:
        life_board.goto(0, 30)
        if life == 0:
            aux.write_message(life_board, 'GAME OVER', 40)
        elif score == 105:
            aux.write_message(life_board, 'YOU WIN!', 40)
        score_board.goto(0, -30)
        aux.write_message(score_board, 'Final score: {}'.format(score), 30)
        time.sleep(2)
        intro2.playing = False
