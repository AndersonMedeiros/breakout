import aux
import turtle


# variável para verificar a inicialização do jogo
playing = False


# criar a tela do jogo
def create_screen():
    global screen
    screen = turtle.Screen()
    screen.title('Breakout')
    screen.bgpic('arts/sky.gif')
    screen.setup(width=700, height=700)
    screen.tracer(100)
    screen.update()
    return screen

global title
title = aux.drawn_sprites('square', 'black', 0, 80)
global options
options = aux.drawn_sprites('square', '#E0FFFF', 0, -20)
global select
select = aux.drawn_sprites('arrow', '#E0FFFF', -120, 15)
global text
text = aux.drawn_sprites('square', '#E0FFFF', 0, 0)


# criar o menu inicial
def create_menu():

    colors = ['#FF6347', '#E9967A', '#F0E68C', '#00FF7F',
              '#40E0D0', '#1E90FF', '#7B68EE', '#EE82EE']
    letters = ['B       ', ' r      ', '  e     ', '   a    ',
               '    k   ', '     o  ', '      u ', '       t']
    for i in range(8):
        title.color(colors[i])
        aux.write_message(title, letters[i], 90)

    options.sety(-20)
    aux.write_message(options, 'Play', 40)
    options.sety(-80)
    aux.write_message(options, 'Help', 40)
    options.sety(-140)
    aux.write_message(options, 'Credit', 40)
    options.sety(-200)
    aux.write_message(options, 'Exit', 40)
    options.sety(320)
    aux.write_message(options, 'Press "Space" to select', 13)

    select.goto(-120, 15)
    select.showturtle()


# captar a movimentação pelo menu
def down_select():
    y = select.ycor()
    if y > -165:
        y += -60
    select.sety(y)


def up_select():
    y = select.ycor()
    if y < 15:
        y += 60
    select.sety(y)


# selecionar algum item do menu
def go_ahead():
    y = select.ycor()

    # impede que o usuário selecione as opções enquanto elas estão invisíveis
    select.sety(300)

    # apaga o menu
    select.hideturtle()
    title.clear()
    options.clear()

    # interior de cada opção do menu
    if y == 15:
        # inicia o jogo
        global playing
        playing = True
    elif y == -45:
        # mostra as instruções do jogo
        instructions = '''
Press the left and right keys or the
   the paddle and counter the ball.
  The goal is to hit and destroy as
       many blocks as you can.\n
           But be careful!
  The ball speeds up whenever you
            make points!
'''
        text.sety(-170)
        aux.write_message(text, instructions, 20)
    elif y == -105:
        # mostra os desenvolvedores
        developers = '''
        Developers:
 Yasmin Muniz de Oliveira
      Rafael Maquiné
     Gabriel Teixeira
      Daniely Dantas
Anderson de Paula Medeiros
'''
        text.sety(-130)
        aux.write_message(text, developers, 20)
    elif y == -165:
        # encerra o jogo
        screen.bye()

    text.sety(320)
    aux.write_message(text, 'Press "BackSpace" to return', 13)


# voltar para o menu
def go_back():
    text.clear()
    # encerra o jogo de imediato
    global playing
    playing = False
    screen.update()
    # reacria o menu
    create_menu()
