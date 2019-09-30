# background: https://www.pexels.com/photo/milky-way-photo-2873671/

import aux
import intro
import turtle

# criando a tela do jogo e o menu
screen = intro.create_screen()
intro.create_menu()
screen.update()

# escutando as escolhas do usuário
screen.listen()
screen.onkeypress(intro.down_select, 'Down')
screen.onkeypress(intro.up_select, 'Up')
screen.onkeypress(intro.go_ahead, 'space')
screen.onkeypress(intro.go_back, 'BackSpace')
screen.update()

# aqui começa o jogo de fato (eu acho...)
# esse é apenas um protótipo para testar a inicialização do jogo
ball = aux.drawn_sprites('circle', 'black', 0, 0)
while True:
    if intro.playing:
        # mostrando os sprites do jogo
        ball.showturtle()
        ball.goto(100, 100)
        ball.goto(-100, -100)
    else:
        # escondendo os sprites do jogo
        ball.hideturtle()
