import pymysql
import xml.etree.ElementTree as ET

# Conexión de base de datos
conexion = "database-2.cjpcutbkgqpa.us-east-1.rds.amazonaws.com"
usuario = "admin"
password = "0123456789"
BBDD = ""


# Creamos la consulta.
def export_query1(outfileName):
    print("Informe sobre los productos de la tienda")
    with open(outfileName, "w") as outfile:
        db = pymysql.connect(conexion, usuario, password, BBDD)
        cursor = db.cursor()
        sql = "SELECT p.codigo,p.nombre, p.precio,f.nombre FROM producto p \
        inner join fabricante f on f.codigo=p.codigo_fabricante".format(0)
        cursor.execute(sql)
        rows = cursor.fetchall()
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<mydata>\n')
        for row in rows:
            codigo = row[0]
            nombre = row[1]
            precio = row[2]
            fabricante = row[3]
            # Now print fetched result
            print(f"codigo = {codigo}, nombre = {nombre}, precio = {precio}, fabricante = {fabricante}")
            outfile.write('  <row>\n')
            outfile.write('    <codigo>%s</name>\n' % row[0])
            outfile.write('    <nombre_producto>%s</desc>\n' % row[1])
            outfile.write('    <precio>%s</rating>\n' % row[2])
            outfile.write('    <nomre_fabricante>%s</rating>\n' % row[3])
            outfile.write('  </row>\n')
        outfile.write('</mydata>\n')
        outfile.close()
        db.close()  # desconectamos


# importacion  del fitxero de configuracion
def import_config():
    min_players, max_players, max_rounds, initial_points, auto_mode, num = "", "", "", "", "", 0
    tree = ET.parse("Basic_Config_Game.xml")
    root = tree.getroot()
    config = []
    for child in root:
        config.append(child.attrib)
    for i in config:
        for x in i.values():
            num += 1
            if num == 1:
                min_players = int(x)
            elif num == 2:
                max_players = int(x)
            elif num == 3:
                max_rounds = int(x)
            elif num == 4:
                initial_points = int(x)
            elif num == 5:
                auto_mode = bool(x)
    return min_players, max_players, max_rounds, initial_points, auto_mode
