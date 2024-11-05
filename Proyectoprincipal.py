import Proyectonumeros
"""
Aqui van todas las funciones que inician el programa,
instrucciones para elegir un area
ofrecer un nuevo turno
o finalizar el programa
"""


def saludo():
    print("Bienvenido a Farmacias Patito\n")


def elegir_opcion():
    opcion = int(input("""
Presiona [1] para Perfumeria
Presiona [2] para Farmacia
Presiona [3] para Cosmeticos
    
"""))

    return opcion


def ofrecer_nuevonumero():
    respuesta = "a"

    while respuesta != 2:
        respuesta = int(input("""
Deseas elegir otro turno?
[1] - Si
[2] - No
            
"""))
        if respuesta == 1:
            return True
        elif respuesta == 2:
            print("Gracias, vuelva pronto")
            return False


def inicio():
    saludo()
    eleccion = "cuquito"

    while eleccion != 4:
        eleccion = elegir_opcion()

        if eleccion == 1:
            Proyectonumeros.perdecor()
        elif eleccion == 2:
            Proyectonumeros.fardecor()
        elif eleccion == 3:
            Proyectonumeros.cosdecor()

        nuevo = ofrecer_nuevonumero()
        if not nuevo:
            eleccion = 4


inicio()
