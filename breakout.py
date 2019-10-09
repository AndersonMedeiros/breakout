# background image: https://www.pexels.com/photo/milky-way-photo-2873671/
# sound effect: https://freesound.org/people/Kodack/sounds/258020/

import char
import intro
import match
import turtle

# criando a tela do jogo
screen = turtle.Screen()
screen.title('Breakout')
screen.bgpic('arts/sky.gif')
screen.setup(width=700, height=700)
screen.tracer(1000)
screen.update()

# criando o menu
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
screen.onkeypress(char.move_paddle_left, 'Left')
screen.onkeypress(char.move_paddle_left, 'a')
screen.onkeypress(char.move_paddle_right, 'Right')
screen.onkeypress(char.move_paddle_right, 'd')
screen.update()

# início do jogo
while True:
    screen.update()
    if intro.playing:
        # mostrando os elementos da partida
        match.start_game()
    else:
        # escondendo os elementos da partida
        match.game_over()
    if intro.finish:
        # fechando a tela
        screen.bye()
