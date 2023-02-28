from connectDB import *
from utils import *

""" ################    """
""" #                   """
""" #   Clientes        """
""" #                   """
""" ################    """
def cargarCliente():
    while True:
        limpiarConsola()
        try:
            print("-----------------------")
            print("-- Datos del cliente --")
            print("-----------------------\n")
            d1 = input("DNI: ")
            if not d1.isnumeric():
                input('El DNI debe ser un número. Presione enter para volver a intentarlo')
                continue
            if existCliente(d1):
                input('El DNI ingresado ya esta registrado. Presione enter para ingresar otro DNI')
                continue

            d2 = input("Nombre completo: ")
            d3 = input("Número de teléfono: ")
            d4 = input("Dirección: ")

            mycursor = mydb.cursor()
            sql = "INSERT INTO clientes (dni, nombre_completo, telefono, direccion) VALUES (%s, %s, %s, %s)"
            val = (int(d1),d2,d3,d4)
            mycursor.execute(sql, val)
            mydb.commit()
            input("El cliente fue registrado. Presione enter para continuar")
            return
        except Exception as e: 
            print(e)
            opcion = input("Lo sentimos, ocurrio un error. Presione enter para volver a intentarlo o 9 para salir")
            if opcion == "9":
                return

def listarClientes():
    limpiarConsola()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM clientes")
    myresultado = mycursor.fetchall()
    clients = [["D.N.I.", "Nombre completo", "Teléfono","Dirección", "Estado"]]
    for row in myresultado:
        if row["estado"] == "D":
            estado = "Disponible"
        else:
            estado = "Ocupado"
        clients.append([row["dni"],row["nombre_completo"],row["telefono"],row["direccion"], estado])
    imprimirTabla(clients)
    input('Presione cualquier tecla para volver al menu de gestión del cliente')

def estadoCliente():
    while True:
        limpiarConsola()
        dni = input("Ingresar DNI de cliente: ")
        if (not dni.isnumeric()):
            opcion = input('Ingrese un campo númerico, vuelva a intentarlo o presione 9 para salir: ')
            if opcion == "9":
                return
            continue

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM clientes WHERE DNI = '"+dni+"'")
        dataCliente = mycursor.fetchone()
        if(dataCliente):
            nombreEstado = "disponible" if dataCliente["estado"] == "D" else "ocupado"
            opcion = input("El cliente "+dataCliente["nombre_completo"]+" esta "+ nombreEstado+". Presione enter para consultar por otro cliente o 9 para salir: ")
            if(opcion == "9"):
                return
            continue
        else: 
            opcion = input("No hemos encontrado un cliente con ese DNI. Presione enter para volver a intentarlo o 9 para salir: ")
            if(opcion == "9"):
                return
            continue
            
def modificarCliente(dni, column, newValue):
    try:
        if not existCliente(dni):
            input('El DNI ingresado no esta registrado. Precione enter para continuar')
            return

        mycursor = mydb.cursor()
        sql = "UPDATE clientes SET "+column+" = '"+newValue+"' WHERE dni = "+dni
        mycursor.execute(sql)
        mydb.commit()
        input('El dato fue modificado correctamente. Presione enter para continuar')
    except Exception as e:
        """ print(e) """
        input("Lo sentimos, ocurrio un error. Presione enter para continuar")

def eliminarCliente():
    while True:
        limpiarConsola()
        try:
            dni = input("Ingresar DNI del cliente: ")
            if not dni.isnumeric():
                input('El DNI debe ser un número. Presione enter para volver a intentarlo')
                continue
            if not existCliente(dni):
                input('El DNI ingresado no esta registrado. Presione enter para volver a intentarlo')
                continue

            mycursor = mydb.cursor()
            mycursor.execute("DELETE FROM clientes WHERE dni = "+dni)
            mydb.commit()
            input('El cliente fue eliminado. Presione enter para volver atras')
            return
        except:
            opcion = input('Lo sentimos, ocurrio un error. Presione enter para volver a intentarlo o 9 para salir: ')
            if opcion == "9":
                return

def existCliente(dni):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes WHERE dni = "+str(dni))
    myresultado = mycursor.fetchone()
    return myresultado




""" ################    """
""" #                   """
""" #   Peliculas       """
""" #                   """
""" ################    """
# CREATE
def cargarPelícula():
    while True:
        limpiarConsola()
        try:
            print("--------------------------")
            print("-- Datos de la pelicula --")
            print("--------------------------\n")
            d1 = int(input("Código de barras: "))

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM peliculas where codigo_de_barras = "+str(d1))
            myresultado = mycursor.fetchone()
            mycursor.close()
            if(myresultado):
                opcion = input('El código de barras ingresado ya existe, presione enter para volver a intentarlo o 9 para salir: ')
                if(opcion == "9"):
                    return
                continue

            d2 = input("Título: ")
            d3 = input("Género: ")
            d4 = "D"
            mycursor = mydb.cursor()
            sql = "INSERT INTO peliculas (codigo_de_barras,titulo,genero,estado) VALUES (%d, %s, %s, %s)"
            val = (d1,d2,d3,d4)
            mycursor.execute(sql, val)
            mydb.commit() 
            input("La pelicula fue registrada correctamente. Presione enter para continuar")
            return
        except Exception as e:
            print(e)
            opcion = input("Lo sentimos, ocurrio un error. Presione enter para volver a intentarlo o 9 para salir: ")
            if opcion == "9":
                return
    
# FIND ALL 
def verPeliculasDisponibles():
    limpiarConsola()
    peliculas = [["Código de barras", "Título","Género"]]

    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM peliculas WHERE estado = 'D' ORDER BY titulo, genero"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for pelicula in results:
        peliculas.append([pelicula["codigo_de_barras"],pelicula["titulo"],pelicula["genero"]])
    imprimirTabla(peliculas)
    input('Presione cualquier tecla para volver al menu de gestión del cliente')

# UPDATE
def modificarPelícula():              # Solo modifica el estado de la película
    while True:
        limpiarConsola()
        print("-------------------------------------")
        print("-- Modificar estado de la pelicula --")
        print("--------------------------------------\n")
        try:
            codigo = int(input("Ingresar código: "))
        except Exception as e:
            opcion = input('El código ingresado no es válido. Vuelva a intentarlo o presione 9 para salir: ')
            if(opcion == '9'):
                return
            continue
        estado = input("Ingresar D para cambiar el estado a disponible u O para el estado ocupado: ")
        if estado not in ["D","O"]:
            opcion = input('El estado ingresado no es válido. Vuelva a intentarlo o presione 9 para salir: ')
            if(opcion == '9'):
                return
            continue
        
        mycursor = mydb.cursor()
        sql = "UPDATE peliculas SET estado = '"+estado+"' WHERE codigo_de_barras = "+str(codigo)
        mycursor.execute(sql)
        peliculaModificada = mycursor.rowcount > 0
        mydb.commit()
        if(peliculaModificada):
            input('El estado de la película fue modificado con correctamente. Presione enter para continuar')
            return
        else:
            opcion = input('No hemos encontrado a ninguna pelicula con ese código, vuelva a intentarlo o presione 9 para continuar: ')
            if(opcion == "9"):
                return
    
# DELETE
def eliminarPelícula():
    while True:
        limpiarConsola()
        print("---------------------------")
        print("--   Eliminar película   --")
        print("---------------------------\n")
        try:
            codigoDeBarras = int(input("Ingresar código de barras: "))
        except Exception as ex:
            opcion = input('El código de barras no es válido. Vuelva a intentarlo o presione 9 para salir: ')
            if(opcion == "9"):
                return
            continue
        
        mycursor = mydb.cursor()
        sql = "DELETE FROM peliculas WHERE codigo_de_barras = "+str(codigoDeBarras)
        mycursor.execute(sql)
        peliculaEliminada = mycursor.rowcount
        mydb.commit()
        if(peliculaEliminada > 0):
            input('La película fue eliminada. Presione enter para continuar')
            return
        else:
            opcion = input('No hemos encontrado a ninguna pelicula con ese código, vuelva a intentarlo o presione 9 para continuar: ')
            if(opcion == "9"):
                return

# QUERY STATE
def estadoDePelicula():
    while True:
        limpiarConsola()
        print("-----------------------------------")
        print("-- Consultar estado de películas --")
        print("-----------------------------------\n")

        codigoBarra = input('Ingrese el código de barras de la película: ')
        # Valido que el campo no este vacío
        if (codigoBarra == ""):
            opcion = input('No hemos encontrado una película con ese código de barras. Presione entener para volver a intentarlo o 9 para salir')
            if(opcion == "9"):
                return
            continue
        

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT p.*, c.* FROM peliculas p LEFT JOIN clientes c ON p.idCliente = c.idCliente WHERE p.codigo_de_barras = "+codigoBarra)
        dataPelicula = mycursor.fetchone()
        mycursor.close()

        # Valido que exista la pelicula
        if (not dataPelicula):
            opcion = input('No hemos encontrado una película con ese código de barras. Presione entener para volver a intentarlo o 9 para salir')
            if(opcion == "9"):
                return
            continue
        
        # Muestor el estado
        if dataPelicula["idCliente"]:
            opcion = input('La película '+ dataPelicula["titulo"]+" fue prestada a "+dataPelicula["nombre_completo"]+". Presione entener para consultar por otra película o 9 para salir. ")
        else:
            opcion = input('La película '+ dataPelicula["titulo"]+" esta disponible. Presione entener para consultar por otra película o 9 para salir. ")
        if opcion == "9":
            return



""" ################    """
""" #                   """
""" #   Prestamos       """
""" #                   """
""" ################    """
def consultarPelícula():
    while True:
        limpiarConsola()
        peli = input("Ingresa el título: ").lower()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM peliculas where LOWER(titulo) LIKE '%"+peli+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        if(myresultado):
            imprimirTabla([
                ["Título","Codigo de barras", "Género","Estado"],
                [myresultado["titulo"], myresultado["codigo_de_barras"], myresultado["genero"], "Disponible" if myresultado["estado"] == "D" else "Prestado"]
            ])
            opcion = input('Si desea buscar otra película presione enter. Si desea salir presione 9: ')
            if(opcion=="9"):
                return
            continue
        else:
            opcion = input('No encontramos ninguna pelicula con ese título. Vuelva a intentarlo o presione 9 para salir: ')
            if(opcion=="9"):
                return

def registrarPrestamo():
    while True:
        limpiarConsola()
        print("----------------------------")
        print("--   Registrar préstamo   --")
        print("----------------------------\n")
        codigoDeBarras = input("Código de barras de la película: ")
        dniCliente = input('Número de documento del cliente: ')
        
        # Valido los campos
        if( not codigoDeBarras.isnumeric() or not dniCliente.isnumeric()):
            input('Los campos deben ser númericos. Presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM peliculas where codigo_de_barras = "+codigoDeBarras)
        dataPelicula = mycursor.fetchone()
        mycursor.close()

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM clientes where dni = "+dniCliente)
        dataCliente = mycursor.fetchone()
        mycursor.close()

        # Valido que exista la pelicula
        if(not dataPelicula):
            opcion = input('El código de barras ingresado no existe, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        if(dataPelicula["estado"] == "O"):
            opcion = input('La película no esta disponible, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue


        # Valido que exista el cliente
        if(not dataCliente):
            opcion = input('El dni ingresado no existe, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue
        
        if (dataCliente["estado"] == "O"):
            opcion = input('El cliente no esta disponible, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        try:

            # Registro el prestamo 
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO prestamos (idCliente, idPelicula) VALUES ("+str(dataCliente['idCliente'])+", "+str(dataPelicula['idPelicula'])+") ")
            mydb.commit()
            mycursor.close()

            # Actualizo el estado del cliente 
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE clientes SET estado = 'O' WHERE idCliente = "+str(dataCliente['idCliente']))
            mydb.commit()
            mycursor.close()

            # Actualizo el estado de la pelicula 
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE peliculas SET estado = 'P', idCliente = "+str(dataCliente['idCliente'])+" WHERE idPelicula = "+str(dataPelicula['idPelicula']))
            mydb.commit()
            mycursor.close()

            input('Hemos registrado el préstamos correctamente. Presione entener para salir ')
            return
        except Exception as e:
            print(e)
            opcion = input('Lo sentimos, no pudimos registrar el préstamo, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue



    return

def registrarDevolucion():
    while True:
        limpiarConsola()
        print("----------------------------")
        print("--  Registrar devolución  --")
        print("----------------------------\n")
        codigoDeBarras = input('Código de barras de la pelicula: ')
        dniCliente = input('Ingrese el DNI del cliente: ')

        # Valido los campos
        if( not codigoDeBarras.isnumeric() or not dniCliente.isnumeric()):
            input('Los campos deben ser númericos. Presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM peliculas where codigo_de_barras = "+codigoDeBarras)
        dataPelicula = mycursor.fetchone()
        mycursor.close()

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM clientes where dni = "+dniCliente)
        dataCliente = mycursor.fetchone()
        mycursor.close()

        # Valido que exista la pelicula
        if(not dataPelicula):
            opcion = input('El código de barras ingresado no existe, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        # Valido que exista el cliente
        if(not dataCliente):
            opcion = input('El dni ingresado no existe, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue
        
        if(dataPelicula["idCliente"] != dataCliente["idCliente"]):
            opcion = input('El cliente ingresado no coincide con la persona que reservó la película, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue

        try:

            # Registro la devolucion 
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO prestamos (idCliente, idPelicula, tipoTransaccion) VALUES ("+str(dataCliente['idCliente'])+", "+str(dataPelicula['idPelicula'])+", 'D') ")
            mydb.commit()
            mycursor.close()

            # Actualizo el estado del cliente 
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE clientes SET estado = 'D' WHERE idCliente = "+str(dataCliente['idCliente']))
            mydb.commit()
            mycursor.close()

            # Actualizo el estado de la pelicula 
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE peliculas SET estado = 'D', idCliente = NULL WHERE idPelicula = "+str(dataPelicula['idPelicula']))
            mydb.commit()
            mycursor.close()

            input('Hemos registrado el la devolución correctamente. Presione entener para salir ')
            return
        except Exception as e:
            print(e)
            opcion = input('Lo sentimos, no pudimos registrar la devolución, presione enter para volver a intentarlo o 9 para salir: ')
            if(opcion == "9"):
                return
            continue
