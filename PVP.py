import os
import random

import common
import conexion


def main():
    min_players, max_players, max_rounds, initial_points, auto_mode = conexion.import_config()
    mazo_referencia = conexion.import_cartas()
    mazo = mazo_referencia
    jugadores = {}
    estado = []
    ronda = 0

    # bucle for para añadir a los jugadores
    print(f"<--Escribe el nombre de entre {min_players} y {max_players} jugadores-->")
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

    # print(jugadores)  # DEBUG
    # print(mazo)  # DEBUG

    # elinamos valores que ya no necesitamos
    for i in estado:
        i.pop(0)
        i.pop(0)

    # print(estado)  # DEBUG

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

            print(f"###JUGADOR {i[0]}### puntos: {i[1]}".upper())
            sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)

            # le pregutamos cuantos puntos quiere apostar
            if len(estado) != turno:
                p_apostar, i[1] = common.apostar_puntos(p_apostar, i[1])

            # le preguntamos si quiere robar mas cartas
            while True:
                mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                if mas_cartas.upper() == "NO":
                    break
                else:
                    sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0], turno)

            # ultima ronda: comprovamos los puntos y resumen ronda
            if len(estado) == turno:
                estado, estado[len(estado) - 1][1] = common.comprovacion_puntos(sum_cartas, p_apostar, estado, estado[len(estado) - 1][1])
                os.system("clear")
                estado = common.resumen_ronda(estado)
        # print(mazo)  # DEBUG
        # print(jugadores)  # DEBUG
        # print(estado)  # DEBUG
