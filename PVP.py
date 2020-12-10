import os
import random
import conexion
import common


def main():
    # Lista con tuplas de los valores de las cartas del mazo
    # Cartas (num,palo(4=oro,3=copas,2=espadas,1=bastos,valor)
    mazo_referencia = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (2, 1, 2), (2, 2, 2), (2, 3, 2), (2, 4, 2),
                       (3, 1, 3), (3, 2, 3), (3, 3, 3), (3, 4, 3), (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4),
                       (5, 1, 5), (5, 2, 5), (5, 3, 5), (5, 4, 5), (6, 1, 6), (6, 2, 6), (6, 3, 6), (6, 4, 6),
                       (7, 1, 7), (7, 2, 7), (7, 3, 7), (7, 4, 7), (10, 1, 0.5), (10, 2, 0.5), (10, 3, 0.5),
                       (10, 4, 0.5), (11, 1, 0.5), (11, 2, 0.5), (11, 3, 0.5), (11, 4, 0.5), (12, 1, 0.5),
                       (12, 2, 0.5), (12, 3, 0.5), (12, 4, 0.5)]

    mazo = mazo_referencia
    jugadores = {}
    estado = []
    ronda = 0
    min_players = conexion.import_config()[0]
    max_players = conexion.import_config()[1]
    max_rounds = conexion.import_config()[2]
    initial_points = conexion.import_config()[3]
    auto_mode = conexion.import_config()[4]

    # bucle for para añadir a los jugadores
    while len(jugadores) < max_players:
        nombre = input("Escribe el nombre de un jugador: ").lower()
        # Comprobamos que el nombre sea alphanumerico y que el primer caracter sea una letra
        if nombre.isalnum() and nombre[0].isalpha() and nombre not in jugadores:
            # agregamos el jugador a la lista, con la carta generada
            jugadores[nombre] = []
            # le generamos una carta al jugador
            random_c = random.randrange(len(mazo))
            estado.append([mazo[random_c][2], mazo[random_c][1], nombre, initial_points, "jugando"])
            mazo.pop(random_c)
            if len(jugadores) > min_players - 1:
                continuar = input("Continuas? (Si, No): ")
                if continuar.upper() == "NO":
                    break
        else:
            print("El nombre tiene que ser alphanumerico, el primer caracter tiene que ser una letra y no puede "
                  "contener espacios!!")

    # Ordenamos los jugadores dependiendo de las cartas que han sacado (metodo burbuja)
    common.ordenar(estado)

    print(jugadores)  # DEBUG
    print(mazo)  # DEBUG
    print(estado)  # DEBUG

    # elinamos valores que ya no necesitamos
    for i in estado:
        i.pop(0)
        i.pop(0)

    while ronda != max_rounds or len(estado) != 1:
        mazo, flag = mazo_referencia, False
        ronda += 1

        # comienza la ronda
        for i in estado:
            turno = 0
            os.system("clear")

            num_masgrande, num = 0, 0

            print(f"###JUGADOR {i[0]}###".upper())
            num, jugadores, mazo = common.generar_carta(jugadores, mazo, num, i[0])

            # le pregutamos cuantos puntos quiere apostar
            p_apostar, i[1] = common.apostar_puntos(i[1])

            # le preguntamos si quiere robar mas cartas
            while True:
                mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                if mas_cartas.upper() == "NO":
                    break
                else:
                    num, jugadores, mazo = common.generar_carta(jugadores, mazo, num, i[0])

            # comprovamos los puntos
            turno += 1
            flag, num_masgrande, i[1], estado = common.comprovacion_puntos(num, p_apostar, num_masgrande, i[1], i[0],
                                                                           flag, estado, turno)

        # comprovamos si tiene 0 puntos para eliminar-lo
        for i in range(len(estado)):
            if estado[i][1] <= 0:
                estado.pop(i)
                print("Tienes 0 puntos, estas eliminado")

        # print(mazo)
        # print(jugadores)  # DEBUG
        # print(estado)  # DEBUG
