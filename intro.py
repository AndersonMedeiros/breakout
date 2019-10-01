import aux
import turtle



# variável para verificar a inicialização do jogo
playing = False


# criar a tela do jogo
def create_screen():
    global screen
    screen = turtle.Screen()
    screen.title('Breakout')
    screen.bgpic('sky.gif')
    screen.setup(width=700, height=700)
    screen.tracer(100)
    screen.update()
    return screen


# criar o menu inicial
def create_menu():
    global title
    title = aux.drawn_sprites('square', 'black', 0, 80)
    colors = ['#FF6347', '#E9967A', '#F0E68C', '#00FF7F',
              '#40E0D0', '#1E90FF', '#7B68EE', '#EE82EE']
    letters = ['B       ', ' r      ', '  e     ', '   a    ',
               '    k   ', '     o  ', '      u ', '       t']
    for i in range(8):
        title.color(colors[i])
        aux.write_message(title, letters[i], 90)

    global op1
    op1 = aux.drawn_sprites('square', '#E0FFFF', 0, -20)
    aux.write_message(op1, 'Play', 40)

    global op2
    op2 = aux.drawn_sprites('square', '#E0FFFF', 0, -80)
    aux.write_message(op2, 'Help', 40)

    global op3
    op3 = aux.drawn_sprites('square', '#E0FFFF', 0, -140)
    aux.write_message(op3, 'Credit', 40)

    global op4
    op4 = aux.drawn_sprites('square', '#E0FFFF', 0, -200)
    aux.write_message(op4, 'Exit', 40)

    global select
    select = aux.drawn_sprites('arrow', '#E0FFFF', -120, 15)
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
    op1.clear()
    op2.clear()
    op3.clear()
    op4.clear()

    # interior de cada opção do menu
    global text
    text = aux.drawn_sprites('square', '#E0FFFF', 0, 0)
    if y == 15:
        # inicia o jogo
        global playing
        playing = True
    elif y == -45:
        # mostra as instruções do jogo
        instructions = '''
Press the left and right keys to move 
the paddle and counter the ball. The 
goal is to hit and destroy as many 
bricks as you can. \nBut be careful! 
The ball speeds up and the paddle gets
smaller whenever you make points!
'''
        text.sety(-140)
        aux.write_message(text, instructions, 20)
    elif y == -105:
        # mostra os desenvolvedores
        developers = '''
Developed by:
Anderson Medeiros
Daniely Dantas
Elikson Bastos
Gabriel Teixeira
Rafael Maquiné
Yasmin Muniz
'''
        text.sety(0)
        aux.write_message(text, developers, 20)
    elif y == -165:
        # encerra o jogo
        screen.bye()


# voltar para o menu
def go_back():
    text.clear()
    # encerra o jogo de imediato
    global playing
    playing = False
    screen.update()
    # reacria o menu
    create_menu()
