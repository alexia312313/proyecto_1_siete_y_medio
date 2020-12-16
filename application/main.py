import os

import PVE
import PVP
import common

while True:
    menu = input("""<--- Menu Proyecto 7 y medio --->
1 Jugador contra jugador
2 Jugador contra bots
3 Salir
-->""")
    os.system(common.detect_system())
    if menu == "1":
        PVP.main()
    elif menu == "2":
        if common.auto_mode.capitalize() == "False":
            input("La opción contra bots está desactivada!!")
        elif common.auto_mode.capitalize() == "True":
            PVE.main()
        else:
            input("Error al cargar el archivo de configuración")
    elif menu == "3":
        break
