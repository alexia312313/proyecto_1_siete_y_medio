import random


def generar_carta(jugadores, mazo, num, jugador):
    random_c = random.randrange(len(mazo))
    jugadores[jugador].append(mazo[random_c])
    print(mazo[random_c])
    num += mazo[random_c][2]
    mazo.pop(random_c)
    return num, jugadores, mazo


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
            if p_apostar >= puntos_jugador:
                print("No puede apostar mas de lo que tienes")
            else:
                puntos_jugador -= p_apostar
                break
    return p_apostar, puntos_jugador


def comprovacion_puntos(num, p_apostar, num_masgrande, puntos_jugador, nombre, flag, estado, turno):
    if num == 7.5:
        puntos_jugador += p_apostar + (p_apostar * 2)
        flag = True
    elif num > 7.5:
        pass
    elif num > num_masgrande:
        num_masgrande = [num, nombre]
    # ultimo turno, si nadie ha sacado 7.5
    if len(estado) == turno and not flag:
        for i in estado:
            if i[1] == num_masgrande[0]:
                i[1] += p_apostar + 1
    return flag, num_masgrande, puntos_jugador, estado
