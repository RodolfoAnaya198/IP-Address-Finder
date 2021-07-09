# Modulos
import socket
import requests
from tabulate import tabulate

# Clase para los colores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

# Obtiene las IP´s
def obtenerIPs():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    public_ip = requests.get('https://api.ipify.org').text

    encabezado = ["Hostname", "IP Local", "IP Pública"]
    datos = [hostname, local_ip, public_ip]
    tabla = [encabezado, datos] 
    return tabla

# Imprime los resultados en una tabla
def imprimirResultados(tabla):
    print(f"{bcolors.OKGREEN}")
    print(tabulate(tabla, headers="firstrow", tablefmt="fancy_grid"))
    print(f"{bcolors.ENDC}\n")

# Imprime mensaje de error de conexión
def mensajeErorConexion():
    tabla = [["ERROR de conexión"], ["Verifica la conexión de tu red."]]
    print(f"{bcolors.FAIL}")
    print(tabulate(tabla, headers="firstrow", tablefmt="fancy_grid"))
    print(f"{bcolors.ENDC}\n")

def imprimeAutor():
    print(f"{bcolors.BOLD} {bcolors.WARNING}\t\tPor Rodolfo Anaya 😎{bcolors.ENDC}\n")

# Inicio del programa
try:
    tabla = obtenerIPs()
    imprimirResultados(tabla)
    imprimeAutor()
except:
    mensajeErorConexion()
    imprimeAutor()

