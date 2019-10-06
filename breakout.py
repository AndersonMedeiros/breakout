# background: https://www.pexels.com/photo/milky-way-photo-2873671/

import intro
import match
import turtle

# criando a tela do jogo
screen = turtle.Screen()
screen.title('Breakout')
screen.bgpic('arts/sky.gif')
screen.setup(width=700, height=700)
screen.tracer(100)
screen.update()

# criando o menu
intro.create_menu()
screen.update()

# escutando as escolhas do usuário
screen.listen()

# movimentação pelo menu
screen.onkeypress(intro.down_select, 'Down')
screen.onkeypress(intro.up_select, 'Up')
screen.onkeypress(intro.go_ahead, 'space')
screen.onkeypress(intro.go_back, 'BackSpace')
screen.update()

# movimentação da raquete durante o jogo
screen.onkeypress(match.move_paddle_left, 'Left')
screen.onkeypress(match.move_paddle_right, 'Right')
screen.update()

# aqui começa o jogo de fato
while True:
    screen.update()
    if intro.playing:
        # mostrando os sprites do jogo
        match.start_game()
    else:
        # escondendo os sprites do jogo
        match.game_over()
    if intro.bye:
        # fechando a tela
        screen.bye()
