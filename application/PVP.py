import os
import random

import common


def main():
    mazo = common.mazo_referencia
    jugadores = {}
    estado = []
    ronda = 0

    # bucle for para añadir a los jugadores
    print(f"<--Escribe el nombre de entre {common.min_players} y {common.max_players} jugadores-->")
    while len(jugadores) < common.max_players:
        nombre = input("Escribe el nombre de un jugador: ").lower()
        # Comprobamos que el nombre sea alfanumérico y que el primer carácter sea una letra
        if nombre.isalnum() and nombre[0].isalpha() and nombre not in jugadores:
            # agregamos el jugador a la lista, con la carta generada
            jugadores[nombre] = []
            # le generamos una carta al jugador
            random_c = random.randrange(len(mazo))
            estado.append([mazo[random_c][2], mazo[random_c][1], nombre, common.initial_points, "jugando"])
            mazo.pop(random_c)
            if len(jugadores) > common.min_players - 1:
                continuar = input("Quieres añadir otro jugador? (Si, No): ")
                if continuar.upper() == "NO" or continuar.upper() == "N":
                    break
        else:
            print("El nombre tiene que ser alfanumérico, el primer carácter tiene que ser una letra y no puede "
                  "contener espacios!!")

    # Ordenamos los jugadores dependiendo de las cartas que han sacado (método burbuja)
    common.ordenar(estado)

    # print(jugadores)  # DEBUG
    # print(mazo)  # DEBUG

    # eliminamos valores que ya no necesitamos
    for i in estado:
        i.pop(0)
        i.pop(0)

    # print(estado)  # DEBUG
    flag = True
    while ronda != common.max_rounds:
        if len(estado) == 1:
            flag = False
            os.system(common.detect_system())
            print(f"El Ganador es {estado[0][0]}!!! 😀")
            break
        mazo, turno = common.mazo_referencia, 0
        sum_cartas, p_apostar = [], []
        ronda += 1

        # comienza la ronda
        for i in estado:
            turno += 1
            os.system(common.detect_system())

            print(f"###JUGADOR {i[0]}### puntos: {i[1]}".upper())
            sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)

            # le preguntamos cuantos puntos quiere apostar
            if len(estado) != turno:
                p_apostar, i[1] = common.apostar_puntos(p_apostar, i[1])

            # le preguntamos si quiere robar mas cartas
            while True:
                if sum_cartas[turno - 1] >= 7.5:
                    input("Te has pasado!! 😪")
                    break
                mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                if mas_cartas.upper() == "NO" or mas_cartas.upper() == "N":
                    break
                elif mas_cartas.upper() == "SI" or mas_cartas.upper() == "S":
                    sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)

            # última ronda: comprobamos los puntos y resumen ronda
            if len(estado) == turno:
                estado, estado[len(estado) - 1][1] = common.comprobar_puntos(sum_cartas, p_apostar, estado, estado[len(estado) - 1][1])
                os.system(common.detect_system())
                estado = common.resumen_ronda(estado, ronda)
        # print(mazo)  # DEBUG
        # print(jugadores)  # DEBUG
        # print(estado)  # DEBUG
    if flag:
        ganador = [0, ""]
        for i in estado:
            if i[1] > ganador[0]:
                ganador[0] = i[1]
                ganador[1] = i[0]
        os.system(common.detect_system())
        print(f"El Ganador es {ganador[1]}!!! 😀")
