import os
import random
import conexion
import common


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
        # Comprobamos que el nombre sea alphanumerico y que el primer caracter sea una letra
        if nombre.isalnum() and nombre[0].isalpha() and nombre not in jugadores:
            # agregamos el jugador a la lista, con la carta generada
            jugadores[nombre] = []
            # le generamos una carta al jugador
            random_c = random.randrange(len(mazo))
            estado.append([mazo[random_c][2], mazo[random_c][1], nombre, initial_points, "jugando"])
            mazo.pop(random_c)
        else:
            print("El nombre tiene que ser alphanumerico, el primer caracter tiene que ser una letra y no puede "
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
        sum_cartas = []
        ronda += 1

        # comienza la ronda
        for i in estado:
            turno += 1
            os.system("clear")

            if i[0] == player_name:
                print(f"###JUGADOR {i[0]}###".upper())
                sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0])
                # le pregutamos cuantos puntos quiere apostar
                p_apostar, i[1] = common.apostar_puntos(i[1])
                # le preguntamos si quiere robar mas cartas
                while True:
                    mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                    if mas_cartas.upper() == "NO":
                        break
                    else:
                        sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0])
            else:
                # input(i[0])
                # Generamos la ronda del bot
                sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0])
                while True:
                    p_apostar = random.randrange(5)
                    if not p_apostar > i[1]:
                        i[1] -= p_apostar
                        break
                if random.randrange(10) == 1:
                    sum_cartas, jugadores, mazo = common.generar_carta(jugadores, mazo, sum_cartas, i[0])

            # ultima ronda: comprovamos los puntos
            if len(estado) == turno:
                i[1], estado, estado[len(estado)-1][1] = common.comprovacion_puntos(sum_cartas, p_apostar, i[1], estado, estado[len(estado)-1][1])

        # print(mazo)
        # input(mazo)  # DEBUG
        # print(estado)  # DEBUG
