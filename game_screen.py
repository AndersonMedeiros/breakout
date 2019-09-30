import turtle
import life
import ball
import os

# função para criação da tela de jogo


def create_screen(title, background_color, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor(background_color)
    screen.setup(width=width, height=height)
    screen.tracer()
    return screen

# criando a tela
game_screen = create_screen("Breakout", "black", 700, 700)

# criando a bola
game_ball = ball.create_ball("circle", "yellow", 0, -300)

# mostrando a "vida" no ecrã

life_screen = create_life("square", "white", 340, -340)

while True:
    game_screen.update()

    # movimentação da bola
    ball.movement_ball(game_ball)

    # colisão com parede esquerda
    if ball.xcor() < -340:   # olhar as medidas
        os.system("aplay bounce.wav&")
        ball.setx(-340)
        ball.dx *= -1

    # colisão com parede direita
    if ball.xcor() > 340:
        os.system("aplay bounce.wav&")
        ball.setx(340)
        ball.dx *= -1

        #  colisão com a parede de inferior
    if ball.ycor() < -340:
        life += 1
        life_screen.clear()
        life_screen.write("{}".format(life), align="center",
                  font=("Tlwg Typo", 24, "normal"))
        os.system("aplay arcade-bleep-sound.wav&")
        ball.goto(100, 100)
        ball.dy *= -1

        # score
    if life == 5:
        ball.setx(100)
        ball.sety(100)
        screen.write("GAME OVER".format(player), align="center",
                                     font=("Tlwg Typo", 24, "normal"))
