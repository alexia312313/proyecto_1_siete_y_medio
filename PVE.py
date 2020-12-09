import os
import random


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
    player_name = ""

    # bucle for para añadir el jugador
    flag = True
    while len(jugadores) < 8:
        if flag:
            flag = False
            nombre = input("Escribe tu nombre: ").lower()
            player_name = nombre
        else:
            nombre = f"bot{len(jugadores)+1}"
        # Comprobamos que el nombre sea alphanumerico y que el primer caracter sea una letra
        if nombre.isalnum() and nombre[0].isalpha() and nombre not in jugadores:
            # le generamos una carta al jugador
            random_c = random.randrange(len(mazo))
            carta = mazo[random_c]
            mazo.pop(random_c)
            estado.append([carta[2], carta[1], nombre, 20, "jugando"])
            # agregamos el jugador a la lista, con la carta generada
            jugadores[nombre] = []
        else:
            print("El nombre tiene que ser alphanumerico, el primer caracter tiene que ser una letra y no puede "
                  "contener espacios!!")

    # Ordenamos los jugadores dependiendo de las cartas que han sacado.
    len_lista = len(estado) - 1
    for i in range(len_lista):
        for j in range(len_lista - i):
            if estado[j] > estado[j + 1]:
                aux = estado[j]
                estado[j] = estado[j + 1]
                estado[j + 1] = aux

    for i in estado:
        i.pop(0)
        i.pop(0)

    # print(jugadores)  # DEBUG
    # print(mazo)  # DEBUG
    # print(estado)  # DEBUG

    rondas = 30
    ronda = 0

    while True:
        if len(jugadores) == 1:
            break
        if ronda == rondas:
            break
        ronda += 1
        mazo = mazo_referencia
        flag = False
        k = 0
        # comienza la ronda
        for i in estado:
            if i[2] == "eliminado":
                pass
            else:
                os.system("clear")

                num_masgrande, num = 0, 0

                if i[0] == jugadores[player_name]:
                    print(f"###JUGADOR {i[0]}###".upper())
                    # generamos al jugador una carta
                    random_c = random.randrange(len(mazo))
                    jugadores[i[0]].append(mazo[random_c])
                    # le enseñamos la carta
                    print(mazo[random_c])
                    num += mazo[random_c][2]
                    mazo.pop(random_c)

                    # le pregutamos cuantos puntos quiere apostar
                    while True:
                        try:
                            p_apostar = int(input("Cuantos puntos quieres apostar? "))
                        except ValueError:
                            pass
                        else:
                            if p_apostar >= i[1]:
                                print("No puede apostar mas de lo que tienes")
                            else:
                                i[1] -= p_apostar
                                break

                    # le preguntamos si quiere robar mas cartas
                    while True:
                        mas_cartas = input("Quieres recibir mas cartas del mazo? (Si, No): ")
                        if mas_cartas.upper() == "NO":
                            break
                        else:
                            random_c = random.randrange(len(mazo))
                            jugadores[i[0]].append(mazo[random_c])
                            print(mazo[random_c])
                            num += mazo[random_c][2]
                            mazo.pop(random_c)
                else:
                    random_c = random.randrange(len(mazo))
                    jugadores[i[0]].append(mazo[random_c])
                    num += mazo[random_c][2]
                    mazo.pop(random_c)
                    while True:
                        try:
                            p_apostar = random.randrange(5)
                        except ValueError:
                            pass
                        else:
                            if p_apostar >= i[1]:
                                pass
                            else:
                                i[1] -= p_apostar
                                break
                    while True:
                        mas_cartas = random.randrange(2)
                        if mas_cartas == 1:
                            break
                        else:
                            random_c = random.randrange(len(mazo))
                            jugadores[i[0]].append(mazo[random_c])
                            print(mazo[random_c])
                            num += mazo[random_c][2]
                            mazo.pop(random_c)

                # comprovamos los puntos
                if num == 7.5:
                    i[1] += p_apostar + (p_apostar * 2)
                    flag = True
                elif num > 7.5:
                    break
                elif num > num_masgrande:
                    num_masgrande = [num, i[0]]

                # ultima ronda, si nadie ha sacado 7.5
                k += 1
                if len(estado) == k and not flag:
                    for m in estado:
                        print(m, num_masgrande)
                        if m[1] == num_masgrande[0]:
                            m[1] += p_apostar + 1

                # comprovamos si tiene 0 puntos para eliminar-lo
                if i[1] <= 0:
                    i[2] = "eliminado"
                    print("Tienes 0 puntos, estas eliminado")

                # print(mazo)

        # print(jugadores)  # DEBUG
        # print(estado)  # DEBUG
