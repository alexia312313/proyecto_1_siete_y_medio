import os
import math
import random

import common
import conexion


def main():
    min_players, max_players, max_rounds, initial_points, auto_mode = conexion.import_config()
    mazo_referencia = conexion.import_cartas()
    mazo = mazo_referencia
    jugadores = {}
    estado = []
    player_name = ""
    ronda = 0

    # bucle for para añadir el jugador
    flag = True
    while len(jugadores) < max_players:
        if flag:
            flag = False
            nombre = input("Escribe tu nombre: ").lower()
            player_name = nombre
        else:
            nombre = f"bot{len(jugadores)}"
        # Comprobamos que el nombre sea alfanumérico y que el primer carácter sea una letra
        if nombre.isalnum() and nombre[0].isalpha() and nombre not in jugadores:
            # agregamos el jugador a la lista, con la carta generada
            jugadores[nombre] = []
            # le generamos una carta al jugador
            random_c = random.randrange(len(mazo))
            estado.append([mazo[random_c][2], mazo[random_c][1], nombre, initial_points, "jugando"])
            mazo.pop(random_c)
        else:
            print("El nombre tiene que ser alfanumérico, el primer carácter tiene que ser una letra y no puede "
                  "contener espacios!!")

    # Ordenamos los jugadores dependiendo de las cartas que han sacado.
    common.ordenar(estado)

    for i in estado:
        i.pop(0)
        i.pop(0)

    # print(mazo)  # DEBUG
    # print(estado)  # DEBUG
    # input(jugadores)  # DEBUG

    while ronda != max_rounds:
        if len(estado) == 1:
            break
        mazo, turno = mazo_referencia, 0
        sum_cartas, p_apostar = [], []
        ronda += 1

        # comienza la ronda
        for i in estado:
            turno += 1
            os.system("clear")

            if i[0] == player_name:
                # Ronda del jugador
                print(f"###JUGADOR {i[0]}###".upper())
                sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)
                # le preguntamos cuantos puntos quiere apostar
                if len(estado) != turno:
                    p_apostar, i[1] = common.apostar_puntos(p_apostar, i[1])
                # le preguntamos si quiere robar mas cartas
                while True:
                    mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                    if mas_cartas.upper() == "NO":
                        break
                    else:
                        sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)
            else:
                # Generamos la ronda del bot
                input(i[0])  # DEBUG
                sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)
                if len(estado) != turno:
                    puntos = random.randrange(math.trunc(i[1]*0.2))
                    i[1] -= puntos
                    p_apostar.append(puntos)
                if random.randrange(5) == 1:
                    sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)

            # última ronda: comprobamos los puntos y resumen ronda
            if len(estado) == turno:
                estado, estado[len(estado)-1][1] = common.comprobar_puntos(sum_cartas, p_apostar, estado, estado[len(estado) - 1][1])
                os.system("clear")
                estado = common.resumen_ronda(estado)
        # print(mazo)
        # input(mazo)  # DEBUG
        # print(estado)  # DEBUG