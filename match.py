import aux
import intro
import os
import time
import turtle

# criando a bola
ball = aux.drawn_sprites('circle', '#E0FFFF', 0, 0)


# movimentação da bola
def movement_ball(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# criando a raquete
paddle = aux.drawn_sprites('square', '#191970', 0, 0)
paddle.shapesize(stretch_wid=0.5, stretch_len=4)


# movimentação a raquete
def move_paddle_left():
    x = paddle.xcor()
    if x > -300:
        x -= 10
    else:
        x = -300
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 300:
        x += 10
    else:
        x = 300
    paddle.setx(x)


# criando o painel da vida
life_board = aux.drawn_sprites('square', '#E0FFFF', 150, 270)

# criando o painel da pontuação
score_board = aux.drawn_sprites('square', '#E0FFFF', -130, 270)


# escondendo e resetando a bola, a raquete e os painéis
def game_over():

    ball.hideturtle()
    ball.dx = -0.5
    ball.dy = -1.5
    ball.goto(0, 0)

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
        ball.goto(0, 0)
        ball.dy *= -1

    # fim de jogo (quantidade de vidas zerada)
    if life == 0:
        ball.setx(100)
        ball.sety(100)
        life_board.goto(0, 30)
        aux.write_message(life_board, 'GAME OVER', 40)
        score_board.goto(0, -30)
        aux.write_message(score_board, 'Final score: {}'.format(score), 30)
        time.sleep(3)
        intro.playing = False
