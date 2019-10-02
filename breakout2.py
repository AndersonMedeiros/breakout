# background: https://www.pexels.com/photo/milky-way-photo-2873671/

import intro2
import match2
import turtle

# criando a tela do jogo e o menu
screen = intro2.create_screen()
intro2.create_menu()
screen.update()

# escutando as escolhas do usuário
screen.listen()
# movimentação pelo menu
screen.onkeypress(intro2.down_select, 'Down')
screen.onkeypress(intro2.up_select, 'Up')
screen.onkeypress(intro2.go_ahead, 'space')
screen.onkeypress(intro2.go_back, 'BackSpace')
screen.update()
# movimentação da raquete durante o jogo
screen.onkeypress(match2.move_paddle_left, 'Left')
screen.onkeypress(match2.move_paddle_right, 'Right')
screen.update()

# aqui começa o jogo de fato
while True:
    screen.update()
    if intro2.playing:
        # mostrando os sprites do jogo
        match2.start_game()
    else:
        # escondendo os sprites do jogo
        match2.game_over()
