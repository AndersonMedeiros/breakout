# background: https://www.pexels.com/photo/milky-way-photo-2873671/

import intro
import match
import turtle

# criando a tela do jogo e o menu
screen = intro.create_screen()
intro.create_menu()
screen.update()

# escutando as escolhas do usuário
screen.listen()
# movimentação pelo menu
screen.onkeypress(intro.down_select, 'Down')
screen.onkeypress(intro.down_select, 's')
screen.onkeypress(intro.up_select, 'Up')
screen.onkeypress(intro.up_select, 'w')
screen.onkeypress(intro.go_ahead, 'space')
screen.onkeypress(intro.go_ahead, 'Return')
screen.onkeypress(intro.go_back, 'BackSpace')
screen.onkeypress(intro.go_back, 'Escape')
screen.update()
# movimentação da raquete durante o jogo
screen.onkeypress(match.move_paddle_left, 'Left')
screen.onkeypress(match.move_paddle_left, 'a')
screen.onkeypress(match.move_paddle_right, 'Right')
screen.onkeypress(match.move_paddle_right, 'd')
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
