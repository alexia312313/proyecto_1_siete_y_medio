import PVE
import PVP
# import conexion

eleccion = input("Que modo quieres jugar 1(PVP), 2(PVE):")

if eleccion == "1":
    PVP.main()
elif eleccion == "2":
    PVE.main()

# conexion.export_query1("resulted_query.xml")
