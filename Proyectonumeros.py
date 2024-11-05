"""
Aqui van todos los generadores y el decorador
"""


def generador_perfumeria():
    x = 1
    p = "P"

    while x >= 1:
        yield f"{p} -- {x}"
        x += 1


def generador_farmacia():
    x = 1
    f = "F"

    while x >= 1:
        yield f"{f} -- {x}"
        x += 1


def generador_cosmeticos():
    x = 1
    c = "C"

    while x >= 1:
        yield f"{c} -- {x}"
        x += 1


def decorar_gen(generador):

    def saludo():
        print("Su turno es: ")
        print(next(generador))
        print("En un momento sera atendido")
    return saludo


perfumeria = generador_perfumeria()
perdecor = decorar_gen(perfumeria)

farmacia = generador_farmacia()
fardecor = decorar_gen(farmacia)

cosmeticos = generador_cosmeticos()
cosdecor = decorar_gen(cosmeticos)
