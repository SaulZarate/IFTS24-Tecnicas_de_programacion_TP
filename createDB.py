""" 
    Intalacion de librerias 
        - pip install mariadb
        - pip install tabulate
"""

import mariadb 
from tabulate import tabulate

mydb = mariadb.connect(
    host="127.0.0.1",
    user="root",      
    database = "VIDEOCLUB",
    autocommit=True
)



""" 
    TABLAS
"""
mycursor = mydb.cursor()
# Clientes
mycursor.execute("CREATE TABLE `videoclub`.`clientes` (`idCliente` INT(5) UNSIGNED NOT NULL AUTO_INCREMENT , `dni` INT NOT NULL , `nombre_completo` VARCHAR(30) NOT NULL , `telefono` VARCHAR(20) NOT NULL , `direccion` VARCHAR(50) NOT NULL , `estado` CHAR(1) NOT NULL , PRIMARY KEY (`idCliente`))")

# Peliculas
mycursor.execute("CREATE TABLE `videoclub`.`peliculas` (`idPelicula` INT(5) UNSIGNED NOT NULL AUTO_INCREMENT , `codigo_de_barras` VARCHAR(20) NOT NULL , `titulo` VARCHAR(20) NOT NULL , `genero` VARCHAR(20) NOT NULL , `estado` CHAR(1) NOT NULL , PRIMARY KEY (`idPelicula`))")

# Prestamos
mycursor.execute("CREATE TABLE `videoclub`.`prestamos` (`idPrestamo` INT(5) UNSIGNED NOT NULL AUTO_INCREMENT , `idCliente` INT(5) NOT NULL , `idPelicula` INT(5) NOT NULL , `estado` CHAR(1) NOT NULL , PRIMARY KEY (`idPrestamo`))")

""" 
    INSERTS
"""
# Clientes
mycursor.execute("INSERT INTO `clientes` (`idCliente`, `dni`, `nombre_completo`, `telefono`, `direccion`, `estado`) VALUES (NULL, '12312312', 'rick sanchez', '12312312', 'calle falsa 123', '');")



""" 
    Mostrar tablas creadas
"""
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

contador = 1
numbers = []
tablas = []
for name in mycursor:
    numbers.append(contador)
    tablas.append(name[0])
    contador += 1

mycursor.close()

tableData = tabulate({
    "#": numbers,
    "Nombre": tablas
    },
    headers="keys",
    tablefmt="grid"
)
print(tableData)
