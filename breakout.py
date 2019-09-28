# background: https://www.pexels.com/photo/milky-way-photo-2873671/

import os
import time
import turtle


# escrever mensagens e texos
def write_message(sprite, text, size):
    sprite.write(text, align='center', font=('Tlwg Typo', size, 'bold'))


# desenhar quaisquer sprites
def drawn_sprites(shape, color, x, y):
    sprite = turtle.Turtle()
    sprite.hideturtle()
    sprite.speed(0)
    sprite.shape(shape)
    sprite.color(color)
    sprite.penup()
    sprite.goto(x, y)
    return sprite


# variável para verificar a inicialização do jogo
playing = False

# criando uma única tela para o jogo inteiro (da linha 28 a linha 125)
screen = turtle.Screen()
screen.title('Breakout')
screen.bgpic('sky.gif')
screen.setup(width=700, height=700)
screen.tracer(100)
screen.update()


# criando o menu inicial
def create_menu():
    global title
    title = drawn_sprites('square', '#E0FFFF', 0, 80)
    write_message(title, 'Breakout', 90)

    global op1
    op1 = drawn_sprites('square', '#E0FFFF', 0, -20)
    write_message(op1, 'Play', 40)

    global op2
    op2 = drawn_sprites('square', '#E0FFFF', 0, -80)
    write_message(op2, 'Help', 40)

    global op3
    op3 = drawn_sprites('square', '#E0FFFF', 0, -140)
    write_message(op3, 'Exit', 40)

    global select
    select = drawn_sprites('arrow', '#E0FFFF', -100, 15)
    select.showturtle()

    screen.update()

create_menu()


# movimentação pelo menu
def down_select():
    y = select.ycor()
    if y > -105:
        y += -60
    select.sety(y)


def up_select():
    y = select.ycor()
    if y < 15:
        y += 60
    select.sety(y)


# selecionando algum item do menu
def go_ahead():
    y = select.ycor()

    # impede que o usuário selecione as opções enquanto elas estão invisíveis
    select.sety(300)

    # apagando o menu
    select.hideturtle()
    title.clear()
    op1.clear()
    op2.clear()
    op3.clear()

    # dentro das opções do menu
    global read
    read = drawn_sprites('square', 'white', 0, 0)
    if y == 15:
        # inicia o jogo
        global playing
        playing = True
    elif y == -45:
        # mostra as instruções do jogo
        write_message(read, 'Vou pensar no que\npôr aqui ainda', 20)
    elif y == -105:
        # encerra o jogo
        screen.bye()


# voltando para o menu
def go_back():
    read.clear()
    # encerra o jogo de imediato
    global playing
    playing = False
    screen.update()
    # reacria o menu
    create_menu()


# escutando as escolhas do usuário
screen.listen()
screen.onkeypress(down_select, 'Down')
screen.onkeypress(up_select, 'Up')
screen.onkeypress(go_ahead, 'space')
screen.onkeypress(go_back, 'BackSpace')
screen.update()


# aqui começa o jogo de fato (eu acho...)
# esse é apenas um protótipo para testar a inicialização do jogo
ball = drawn_sprites('circle', 'black', 0, 0)
while True:
    if playing:
        # mostrando os sprites do jogo
        ball.showturtle()
        ball.goto(100, 100)
        ball.goto(-100, -100)
    else:
        # escondendo os sprites do jogo
        ball.hideturtle()

# não entendi para o que isso serve, então não mudei
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)
