import os

import PVE
import PVP
import conexion

while True:
    menu = input("""<--- Menu Proyecto 7 y medio --->
1 Jugador contra jugador
2 Jugador contra bots
3 Salir
-->""")
    os.system("clear")

    if menu == "1":
        PVP.main()
    elif menu == "2":
        if conexion.import_config()[4].capitalize() == "False":
            input("La opción contra bots está desactivada!!")
        elif conexion.import_config()[4].capitalize() == "True":
            PVE.main()
        else:
            input("Error al cargar el archivo de configuración")
    elif menu == "3":
        break
