import turtle

# Funções auxiliares para desenhar sprites e escrever mensagens na tela


# escrever mensagens e textos
def write_message(sprite, text, size):
    sprite.write(text, align='center', font=('Tlwg Typo', size, 'bold'))


# desenhar quaisquer sprites (inclusive a bola e a raquete)
def drawn_sprites(shape, color, x, y):
    sprite = turtle.Turtle()
    sprite.hideturtle()
    sprite.speed(0)
    sprite.shape(shape)
    sprite.color(color)
    sprite.penup()
    sprite.goto(x, y)
    return sprite
