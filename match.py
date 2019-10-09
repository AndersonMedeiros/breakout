import aux
import char
import intro
import os
import time
import turtle


# acelera a criação dos elementos na tela
acc = turtle.Screen()
acc.tracer(1000)


# encerrar uma partida do jogo
def game_over():

    # resetando a bola
    char.ball.hideturtle()
    char.set_ball()

    # resetando a raquete
    char.paddle.hideturtle()
    char.paddle.setx(0)

    # resetando os blocos
    for line in range(8):
        for column in range(9):
            char.brick_matrix[line][column].hideturtle()

    # resetando o painel da vida
    char.life_hud.clear()
    char.life_hud.goto(150, 270)
    global life
    life = 3

    # resetando o painel da pontuação
    char.score_hud.clear()
    char.score_hud.goto(-130, 270)
    global score
    score = 0


# iniciar uma partida do jogo
def start_game():

    # mostrando a bola e a raquete
    char.ball.showturtle()
    char.paddle.showturtle()

    # ajustando o painel da vida
    global life
    if life == 3:
        char.life_hud.clear()
        aux.message(char.life_hud, 'Life: 3', 20)

    # ajustando o painel da pontuação
    global score
    if score == 0:
        char.score_hud.clear()
        aux.message(char.score_hud, 'Score: 0', 20)
        # mostrando os blocos
        for line in range(8):
            for column in range(9):
                char.brick_matrix[line][column].showturtle()

    # movimentando a bola
    char.ball.setx(char.ball.xcor() + char.ball.dx)
    char.ball.sety(char.ball.ycor() + char.ball.dy)

    # colisão com a parede esquerda
    if char.ball.xcor() < -340:
        os.system('aplay arts/bounce.wav&')
        char.ball.setx(-340)
        char.ball.dx *= -1

    # colisão com a parede direita
    if char.ball.xcor() > 340:
        os.system('aplay arts/bounce.wav&')
        char.ball.setx(340)
        char.ball.dx *= -1

    # colisão com a parede superior
    if char.ball.ycor() > 340:
        os.system('aplay arts/bounce.wav&')
        char.ball.sety(340)
        char.ball.dy *= -1

    # colisão com a parede inferior
    if char.ball.ycor() < -340:
        life -= 1
        char.life_hud.clear()
        aux.message(char.life_hud, 'Life: {}'.format(life), 20)
        os.system('aplay arts/arcade-bleep-sound.wav&')
        char.set_ball()
        char.paddle.setx(0)

    # colisão com a raquete
    if (char.ball.ycor() < -295 and
       char.ball.xcor() < char.paddle.xcor() + 70 and
       char.ball.xcor() > char.paddle.xcor() - 70):

        if char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*4 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*3:
            char.direction_angle(30)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*3 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*2:
            char.direction_angle(45)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*2 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*1:
            char.direction_angle(60)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*1 and \
                char.ball.xcor() > char.paddle.xcor() + char.TAM_ONE_SEG*0:
            char.direction_angle(85)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*1 and \
                char.ball.xcor() == char.paddle.xcor() + char.TAM_ONE_SEG*0:
            char.direction_angle(90)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*0 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*-1:
            char.direction_angle(100)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*-1 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*-2:
            char.direction_angle(120)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*-2 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*-3:
            char.direction_angle(135)

        elif char.ball.xcor() < char.paddle.xcor() + char.TAM_ONE_SEG*-3 and \
                char.ball.xcor() >= char.paddle.xcor() + char.TAM_ONE_SEG*-4:
            char.direction_angle(150)

        os.system('aplay arts/bounce.wav&')

    # colisão com os blocos
    for line in range(8):
        for column in range(9):
            brick_y = char.brick_matrix[line][column].ycor()
            brick_x = char.brick_matrix[line][column].xcor()
            if ((char.ball.ycor() >= brick_y - 20 and
               char.ball.ycor() <= brick_y + 20 or
               char.ball.ycor() == brick_y) and
               (char.ball.xcor() > brick_x - 40 and
               char.ball.xcor() < brick_x + 40 or
               char.ball.xcor() == brick_x) and
               char.brick_matrix[line][column].isvisible()):
                char.ball.dy *= -1
                char.speed_ball += char.growth[line]*0.03
                score += char.growth[line]
                char.score_hud.clear()
                aux.message(char.score_hud, 'Score: {}'.format(score), 20)
                os.system('aplay arts/bounce.wav&')
                char.brick_matrix[line][column].hideturtle()

    # fim de jogo (vida zerada ou pontuação máxima)
    if life == 0 or score == 360:
        char.life_hud.goto(0, 0)
        if life == 0:
            aux.message(char.life_hud, 'GAME OVER', 40)
        else:
            aux.message(char.life_hud, 'YOU WIN!', 40)
        char.score_hud.goto(0, -60)
        aux.message(char.score_hud, 'Final score: {}'.format(score), 30)
        time.sleep(5)
        intro.playing = False
