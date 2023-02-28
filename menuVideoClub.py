import videoclub
from utils import cerrarConsola, limpiarConsola, imprimirTabla

def mostrarMenuPrincipal():
    data = [
        ["#", "Menu Principal - Opciones"],
        ["1", "Consulta de disponibilidad de película"],
        ["2", "Préstamos de películas"],
        ["3", "Gestión del clientes"],
        ["4", "Gestión de películas"],
        ["",""],
        ["0", "Salir"]
    ]
    imprimirTabla(data)

""" 
    ###################
    #
    #   MENU CLIENTE
    #
    ###################
"""

def subMenuCliente():
    while True:
        limpiarConsola()
        data = [
            ["#", "Gestión del cliente - Opciones"],
            ["1", "Ver clientes"],
            ["2", "Alta del cliente"],
            ["3", "Consulta estado del cliente"],
            ["4", "Modificar teléfono o dirección del cliente"],
            ["5", "Eliminar cliente"],
            ["",""],
            ["9", "Ir al menu principal"]
        ]
        imprimirTabla(data)
        opcion = input("\nIngresar una opción: ")
        if opcion == "1":
            videoclub.listarClientes()
        if opcion == "2":
            videoclub.cargarCliente()
        if opcion == "3":
            videoclub.estadoCliente()
        if opcion == "4":
            subMenuModificacionDelCliente()
        if opcion == "5":
            videoclub.eliminarCliente()
        if opcion == "9":
            break

def subMenuModificacionDelCliente():
    while True:
        limpiarConsola()
        data = [
            ["#","Modificar datos del cliente"],
            ["1","Modificar Teléfono"],
            ["2","Modificar Dirección"],
            ["",""],
            ["3","Volver"],
        ]
        imprimirTabla(data)

        opcionModificarCliente = input("Elegir opción para modificar: ")
        if opcionModificarCliente == "3":
            return

        if opcionModificarCliente not in ["1","2","3"]:
            input('La opción seleccionada no es correcta. Presione cualquier tecla para volver a intentarlo')
            continue
            
        dniCliente = input('\nIngrese el DNI del cliente: ')
        if (not dniCliente.isnumeric()):
            opcion = input('El dni es un campo númerico. Vuelva a ingresar el DNI o presione 9 para volver atras: ')
            if (opcion == "9"):
                return
            continue

        if opcionModificarCliente == "1":
            columnEdit = "telefono"
            newDate = input('Ingrese el nuevo número de teléfono: ')
        else:
            columnEdit = "direccion"
            newDate = input('Ingrese la nueva dirección: ')

        videoclub.modificarCliente(dniCliente, columnEdit, newDate)
        return

""" 
    ###################
    #
    #   MENU PELICULA
    #
    ###################
"""

def subMenuPelicula():
    while True:
        limpiarConsola()
        data = [
            ["#", "Gestión de peliculas - Opciones"],
            ["1", "Alta de película"],
            ["2", "Consultar película"],
            ["3", "Modificar película"],
            ["4", "Eliminar película"],
            ["",""],
            ["9", "Ir al menu principal"]
        ]
        imprimirTabla(data)
        opcion = input("\nIngresar una opción: ")
        
        if opcion == "1":
            videoclub.cargarPelícula()
        if opcion == "2":
            videoclub.consultarPelícula()
        if opcion == "3":
            videoclub.modificarPelícula()
        if opcion == "4":
            videoclub.eliminarPelícula()
        if opcion == "9":
            break

""" 
    ###################
    #
    #   MENU PRESTAMOS
    #
    ###################
"""
def subMenuPrestamos():
    while True:
        limpiarConsola()
        data = [
            ["#", "Préstamos"],
            ["1", "Ver peliculas disponibles"],
            ["2", "Registrar préstamo"],
            ["3", "Registrar devolución"],
            ["",""],
            ["9", "Ir al menu principal"]
        ]
        imprimirTabla(data)
        opcion = input("\nIngresar una opción: ")
        
        if opcion == "1":
            videoclub.verPeliculasDisponibles()
        if opcion == "2":
            videoclub.registrarPrestamo()
        if opcion == "3":
            videoclub.registrarDevolucion()

        if opcion == "9":
            break



""" ----------------------------------------------------------------------------------- """
""" ----------------------------------------------------------------------------------- """
"""                                 INICIALIZADOR DEL PRYECTO                           """
""" ----------------------------------------------------------------------------------- """
""" ----------------------------------------------------------------------------------- """
def start():
    while True:
        limpiarConsola()
        mostrarMenuPrincipal()
        opciónElegida = int(input("\nIngresar una opción: "))
        if opciónElegida == 1:
            videoclub.estadoDePelicula()
        if opciónElegida == 2:
            subMenuPrestamos()
        if opciónElegida == 3:
            subMenuCliente()
        if opciónElegida == 4:
            subMenuPelicula()
        if opciónElegida == 0:
            cerrarConsola()
