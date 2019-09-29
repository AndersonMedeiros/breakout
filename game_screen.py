import turtle
import ball


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

while True:
    game_screen.update()

    # movimentação da bola
    ball.movement_ball(game_ball)
