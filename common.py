import random


def generar_carta(jugadores, mazo, sum_cartas, jugador):
    random_c = random.randrange(len(mazo))
    jugadores[jugador].append(mazo[random_c])
    print(f"{mazo[random_c][0]} de {mazo[random_c][3]}")
    sum_cartas.append(mazo[random_c][2])
    mazo.pop(random_c)
    return sum_cartas, jugadores, mazo


def ordenar(estado):
    len_lista = len(estado) - 1
    for i in range(len_lista):
        for j in range(len_lista - i):
            if estado[j] > estado[j + 1]:
                aux = estado[j]
                estado[j] = estado[j + 1]
                estado[j + 1] = aux


def apostar_puntos(puntos_jugador):
    while True:
        try:
            p_apostar = int(input("Cuantos puntos quieres apostar? "))
        except ValueError:
            pass
        else:
            if p_apostar > puntos_jugador:
                print("No puede apostar mas de lo que tienes")
            else:
                puntos_jugador -= p_apostar
                break
    return p_apostar, puntos_jugador


def comprovacion_puntos(sum_cartas, p_apostar, puntos_jugador, estado, puntos_banca):
    flag_75, flag_1 = False, False
    for i in range(len(estado)-1):
        # jugador
        if sum_cartas[i] > 7.5:
            pass
        elif sum_cartas[i] == 7.5 and sum_cartas[len(sum_cartas) - 1] != 7.5:
            flag_75 = True
            puntos_jugador += p_apostar + (p_apostar * 2)
            estado.insert(estado[len(estado) - 1], sum_cartas[i])
            estado.pop(i)
        elif sum_cartas[i] > sum_cartas[len(sum_cartas) - 1]:
            flag_1 = True
            puntos_jugador += 1

        # banca
        if sum_cartas[len(sum_cartas) - 1] > 7.5:
            pass
        elif not flag_75 and sum_cartas[len(sum_cartas) - 1] == 7.5:
            puntos_banca += p_apostar + (p_apostar * 2)
        elif not flag_1:
            puntos_banca += 1

    # comprovamos si tiene 0 puntos para eliminar-lo
    for i in range(len(estado)):
        if estado[i][1] <= 0:
            estado.pop(i)
            print("Tienes 0 puntos, estas eliminado")
    return puntos_jugador, estado, puntos_banca
