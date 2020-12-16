import random


# función de generar cartas
def generar_carta(jugadores, mazo, sum_cartas, jugador, num_jugador):
    random_c = random.randrange(len(mazo))
    jugadores[jugador].append(mazo[random_c])
    print(f"{mazo[random_c][1]} de {mazo[random_c][3]} ({mazo[random_c][2]})")
    try:
        sum_cartas[num_jugador - 1] += float(mazo[random_c][2])
    except IndexError:
        sum_cartas.append(float(mazo[random_c][2]))
    mazo.pop(random_c)
    return sum_cartas, jugadores, mazo


# función de ordenación (método burbuja)
def ordenar(estado):
    len_lista = len(estado) - 1
    for i in range(len_lista):
        for j in range(len_lista - i):
            if estado[j] > estado[j + 1]:
                aux = estado[j]
                estado[j] = estado[j + 1]
                estado[j + 1] = aux


# función donde el jugador aposta puntos
def apostar_puntos(p_apostar, puntos_jugador):
    while True:
        try:
            puntos = int(input("Cuantos puntos quieres apostar? "))
        except ValueError:
            pass
        else:
            if puntos > puntos_jugador:
                print("No puede apostar mas de lo que tienes")
            else:
                puntos_jugador -= puntos
                p_apostar.append(puntos)
                break
    return p_apostar, puntos_jugador


# función que comprueba los puntos de todos los jugadores y les resta o suma dependiendo el resultado
def comprobar_puntos(sum_cartas, p_apostar, estado, puntos_banca):
    flag = False
    # aquí pondremos si los jugadores han ganado a la banca
    desbancar = []
    # print(sum_cartas)  # DEBUG
    for i in range(len(estado) - 1):
        if sum_cartas[len(sum_cartas) - 1] > 7.5:
            if not sum_cartas[i] > 7.5:
                estado[i][1] += p_apostar[i]
                puntos_banca -= p_apostar[i]
        else:
            if sum_cartas[i] > 7.5:
                pass
            elif sum_cartas[i] == 7.5 and sum_cartas[len(sum_cartas) - 1] != 7.5:
                flag = True
                estado[i][1] += p_apostar[i] + (p_apostar[i] * 2)
                puntos_banca -= p_apostar[i]
            elif sum_cartas[i] > sum_cartas[len(sum_cartas) - 1]:
                flag = True
                estado[i][1] += p_apostar[i] + 1
                puntos_banca -= p_apostar[i]
            if not flag:
                desbancar.append("no")
                puntos_banca += p_apostar[i]
            else:
                desbancar.append("si")
    input(desbancar)
    # comprobamos si algún jugador a desbancado a la banca
    flag, nueva_banca = False, 0
    for i in range(len(desbancar)):
        if desbancar[-i] == "si":
            flag = True
            nueva_banca = i
    if flag:
        estado.insert(len(estado), estado[nueva_banca])
        estado.pop(nueva_banca)

    return estado, puntos_banca


# función para imprimir el resumen de la ronda y eliminar si un jugador tiene 0 puntos
def resumen_ronda(estado):
    print("Resumen de la ronda")
    for i in range(len(estado)):
        # comprobamos si tiene 0 puntos para eliminar-lo
        if estado[i][1] <= 0:
            print(f"Jugador {estado[i][0]}: Eliminado")
            estado.pop(i)
        else:
            print(f"Jugador {estado[i][0]}: {estado[i][1]} puntos")
    input()
    return estado
