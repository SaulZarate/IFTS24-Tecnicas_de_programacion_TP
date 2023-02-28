import mariadb
from utils import *

# Limpiar consola
limpiarConsola()

mydb = mariadb.connect(
    host="127.0.0.1",
    user="root",      
    database = "VIDEOCLUB"
)
""" mycursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM clientes WHERE estado IN ('A','');")
myresultado = mycursor.fetchall()
clients = [["D.N.I.", "Nombre completo", "Teléfono","Dirección", "Estado"]]
for row in myresultado:
    if row["estado"] in ["","A"]:
        estado = "Activo"
    else:
        estado = "Eliminado"
    clients.append([row["dni"],row["nombre_completo"],row["telefono"],row["direccion"], estado])

imprimirTabla(clients) """

""" peli = input("Ingresa el título: ").lower()
mycursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM peliculas where LOWER(titulo) LIKE '%"+peli+"%'"
mycursor.execute(sql)
myresultado = mycursor.fetchone()
if(myresultado):
    print(myresultado) """

""" mycursor = mydb.cursor()
mycursor.execute("DELETE FROM peliculas WHERE codigo_de_barras = 12")
registrosAfectados = mycursor.rowcount
print("Registros eliminados: "+str(registrosAfectados))
mydb.commit()
mydb.close() """