import turtle


# função para criação da tela de jogo
def create_screen(title, background_color, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor(background_color)
    screen.setup(width=width, height=height)
    screen.tracer()
    return screen

# criando tela
game_screen = create_screen("Breakout", "black", 700, 700)

while True:
    game_screen.update()
