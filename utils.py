from tabulate import tabulate
from os import system
import sys

def cerrarConsola():
    sys.exit()

def imprimirTabla(data):
    tableData = tabulate(data,headers="firstrow",tablefmt="grid", stralign="left")
    print(tableData)

def limpiarConsola():
    system("cls")
