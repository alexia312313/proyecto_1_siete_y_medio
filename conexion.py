import pymysql
# import main

# Conexión de base de datos
conexion = "database-2.cosxt3tlpu0w.us-east-1.rds.amazonaws.com"
usuario = "admin"
password = "admin123"
BBDD = ""

# db = pymysql.connect(conexion, usuario, password, BBDD)
# Este cursor lo usamos para ejecutar la query y almacenar sus datos
# cursor = db.cursor()


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

        # desconectamos
        db.close()
