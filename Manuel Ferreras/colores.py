RED = '\033[6;31m' # se configura una variable que codifica el color de texto

NOCOLOR = '\033[0;0m' # se configura una variable que codifica el color de texto

COLOR = '\x1b[{};{}m'


def cambiar_color(estilo=1, color=38):
    return COLOR.format(estilo, color)
