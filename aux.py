import turtle


# escrever mensagens e textos
def message(element, text, size):
    element.write(text, align='center', font=('Tlwg Typo', size, 'bold'))


# desenhar quaisquer elementos (inclusive a bola e a raquete)
def drawn_element(shape, color, x, y):
    element = turtle.Turtle()
    element.hideturtle()
    element.speed(0)
    element.shape(shape)
    element.color(color)
    element.penup()
    element.goto(x, y)
    return element
