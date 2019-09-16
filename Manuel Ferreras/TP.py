
#!/bin/python3

# Trabajo Practico de Vacaciones
# Integrantes: Franco Casavecchia & Manuel Ferreras   4to Año "C"

import os # importa comandos del SO
import re # utilizado para los colores
import time # para poder hacer esperar el programa
import carga

def guardar_nombres(nombre, nombre_archivo):
    if len(nombre) > 0:
        archivo = open("nombre.txt", 'wb')
        tamano = len(nombre)
        for i in range(tamano):
            pickle.dump(nombre[i], "nombre.txt")
        "nombre.txt".close()

def leer_nombres(vector, nombre_archivo):
    if os.path.exists("nombre.txt"):
        archivo = open("nombre.txt", 'rb')
        tamano = os.path.getsize("nombre.txt")
        if tamano < 1:
            error("No hay datos")
        while "nombre.txt".tell() < tamano:
            elemento = pickle.load("nombre.txt")
            vector.append(elemento)

def guardar_donaciones(donacion, nombre_archivo):
    if len(nombre) > 0:
        archivo = open("donaciones.txt", 'wb')
        tamano = len(nombre)
        for i in range(tamano):
            pickle.dump(nombre[i], "donaciones.txt")
        "nombre.txt".close()

def leer_donaciones(donacion, nombre_archivo):
    if os.path.exists("donacion.txt"):
        archivo = open("nombre.txt", 'rb')
        tamano = os.path.getsize("nombre.txt")
        if tamano < 1:
            error("No hay datos")
        while "nombre.txt".tell() < tamano:
            elemento = pickle.load("nombre.txt")
            vector.append(elemento)


def bubblesort(list):
    while True:
        corrected = False
        for i in range(0, len(list) - 1):
          if list[i] > list [i+1]:
              list[i], list[i+1] = list[i+1], list[i]
              corrected = True
          if not corrected:
              return list

RED = '\033[6;31m' # se configura una variable que codifica el color de texto

NOCOLOR = '\033[0;0m' # se configura una variable que codifica el color de texto

COLOR = '\x1b[{estilo};{color}m'

COLOR.format(estilo=1, color=38)

os.system("clear")

menor_a_mayor = []

mayor_a_menor = []

nombre = []

minima_donacion  = 0

maxima_donacion = 0

nombre_del_max = ""

donacion = []

valor_sin_ordenar = []

nombre_sin_ordenar = []

seguir = 1

max_donacion = 1000000 # es la cantidad de dinero necesaria para la organizacion

os.system("clear")

print(COLOR.format(estilo=1, color=38)+"Bienvenido a la ORG Caritas Argentina\n")

print("Esta organizacion recauda fondos para niños que necesitan en Argentina\n")

time.sleep(0.6)

while seguir == 1:
    res = 10
    volver = 0
    back = 0
    exist = False
    volv = 0
    rep = 1
    largo = len(str(max_donacion))

    # Variable utilizada en el menu para corregir espacios cada vez que un numero disminuye una cifra

    if largo == 6:
        a = " "
    elif largo == 5:
        a = "  "
    elif largo == 4:
        a = "   "
    elif largo == 3:
        a = "    "
    elif largo == 2:
        a = "     "
    elif largo == 1:
        a = "      "
    else:
        a = ""

    print(COLOR.format(estilo=1, color=33)+" _____________________________________________________________________________________________________________________ ")
    print("|                                                                                                                     |")
    print("|              ________        ___         _____      ___________  __________        ___         ______               |")
    print("|             |               /   \       |     \          |            |           /   \       |                     |")
    print("|             |              /     \      |      \         |            |          /     \      |                     |")
    print("|             |             /       \     |-------|        |            |         /       \     |______               |")
    print("|             |            /         \    |      \         |            |        /         \          |               |")
    print("|             |           /-----------\   |       \        |            |       /-----------\         |               |")
    print("|             |________  /             \  |        \  _____|_____       |      /             \  ______|               |")
    print("|                                                                                                                     |")
    print("|                                                                                                                     |")
    print("|                                       Todavia se necesitan recaudar $" ,max_donacion,"          " ,a, "                          |")
    print("|                                                                                                                     |")
    print("|                                                                                                                     |")
    print("|             1-Añadir un donador                                             2-Ver todas las donaciones              |")
    print("|                                                                                                                     |")
    print("|             3-Maxima donacion recibida                                      4-Minima donacion recibida              |")
    print("|                                                                                                                     |")
    print("|             5-Donaciones de mayor a menor                                   6-Donaciones de menor a mayor           |")
    print("|                                                                                                                     |")
    print("|             7-Buscar donadores por nombre                                   8-Buscar donadores por monto            |")
    print("|                                                                                                                     |")
    print("|             9-Breve historia de CARITAS                                     0-Salir del programa                    |")
    print("|                                                                                                                     |")
    print("|_____________________________________________________________________________________________________________________|"+NOCOLOR)
    while res < 0 or res > 9:
        res = int(input("\nEliga una opcion: \n"))

        if res == 9:
            os.system("clear")
            while volver == 0: # Muestra la opcion 9
                print(COLOR.format(estilo=1, color=34) + "")
                print(" ____________________________________________________________________________________________________________________ ")
                print("|                                                                                                                    |")
                print("|                                               CARITAS ARGENTINA                                                    |")
                print("|                                                                                                                    |")
                print("|                                                                                                                    |")
                print("|     Cáritas Argentina es el organismo oficial de la Iglesia Católica que lleva adelante la pastoral caritativa,    |")
                print("|    para lograr el desarrollo integral de todo el hombre y de todos los hombres, con especial preferencia por       |")
                print("|    las personas y por las comunidades más pobres y marginadas.                                                     |")
                print("|                                                                                                                    |")
                print("|                                                                                                                    |")
                print("|     Esta enorme tarea es posible gracias al compromiso cotidiano de más de 32.000 voluntarios y a la colaboración  |")
                print("|    solidaria de toda la sociedad.                                                                                  |")
                print("|                                                                                                                    |")
                print("|                                                                                                                    |")
                print("|     A través de ellos, Cáritas lleva adelante proyectos de promoción humana y micro emprendimientos productivos    |")
                print("|    y de autoconsumo, acompaña el abordaje pastoral y comunitario de las adicciones, brinda capacitación laboral,   |")
                print("|    formación en ciudadanía y cuidados de la primera infancia, becas escolares y universitarias, talleres de        |")
                print("|    alfabetización y apoyo escolar.                                                                                 |")
                print("|                                                                                                                    |")
                print("|                                                                                                                    |")
                print("|     También acompaña tareas de prevención y atención de emergencias climáticas y trabaja con personas en           |")
                print("|    situación de calle, junto a otras acciones de tipo asistencial, conforme a necesidades y lugares específicos.   |")
                print("|                                                                                                                    |")
                print("|____________________________________________________________________________________________________________________|"+NOCOLOR)

                while volver != 1:
                    volver = int(input("\n Ingrese 1 para volver\n"))
                os.system("clear")

# Respuesta de opcion 1

        if res == 1:
            os.system("clear")
            print("La donacion maxima puede ser de $",max_donacion)

            while rep == 1: # rep es una variable que sirve para que se verifique si el nombre ha sido correctame ingresado y si la donacion tambien es correcta
                name = input("Ingrese el nombre del donador\n") # Una variable auxiliar con la cual se podra hacer una

                if "1" in name or "2" in name or "3" in name or "4" in name or "5" in name or "6" in name or "7" in name or "8" in name or "9" in name or "0" in name:
                    print("El nombre no puede contener valores numericos")
                else:
                    valor = int(input("Ingrese el valor de la donacion\n"))

                    if valor > 0 and valor <= max_donacion:
                        nombre.append(name) # Se utiliza para agregar el nombre al vector
                        donacion.append(valor) # Se utiliza para agregar el monto ingresado al vector
                        rep = 0
                        max_donacion = max_donacion - valor
                        os.system("clear")
                        print("Gracias por su donacion")
                        time.sleep(0.5)
                        os.system("clear") #Limpia la pantalla
                        mayor_a_menor.append(("$"+str(valor), name)) # Se agrega el valor ingresado al vector de mayor a menor
                        menor_a_mayor.append(("$"+str(valor),name)) # Se agrega el valor ingresado al vector de menor a mayor
                        nombre_sin_ordenar.append(name) # Se agrega el nombre ingresado al vector de nombre sin ordenar
                        valor_sin_ordenar.append(valor) # Se agrega el valor ingresado al vector de valor sin ordenar

# Utilizado
                        if valor > maxima_donacion:
                            maxima_donacion = valor
                            nombre_del_max = name
                        elif valor < minima_donacion:
                            minima_donacion = valor
                            nombre_del_min = name

                        if minima_donacion == 0:
                            minima_donacion = valor
                            nombre_del_min = name
                    else:
                        print("La donacion no puede ser menor o igual a 0 y la donacion no puede ser superior a" ,max_donacion, "pesos")

# Respuesta a opcion 2

        if res == 2 and len(nombre) > 0:
            while back != 1:
                os.system("clear")
                print("\nNombre de los donadores:\n")
                print(list(nombre))
                print("\n")
                print("Valor de la donacion:\n")
                print(list(donacion))
                back = int(input("\n\nSi desea volver al menu ingrese 1\n"))
                os.system("clear")


# Respuesta a opcion 3

        if res == 3 and len(nombre) > 0:
            os.system("clear")
            print(COLOR.format(estilo=1, color=40)+"\n La maxima donacion recibida fue de $" ,maxima_donacion, "y fue emitida por" ,nombre_del_max + NOCOLOR)
            print("\n Para volver ingrese 1:\n")
            while volv != 1:
                volv = int(input())

# Respuesta a opcion 4

        if res == 4 and len(nombre) > 0:
            os.system("clear")
            print(COLOR.format(estilo=1, color=40)+"\nLa minima donacion recibida fue de $" ,minima_donacion, "y fue emitida por" ,nombre_del_min + NOCOLOR)
            print("\n Para volver ingrese 1:\n")
            while volv != 1:
                volv = int(input())

# Respuesta a opcion 5

        if res == 5 and len(nombre) > 0:
            mayor_a_menor.sort(reverse=True)
            os.system("clear")
            print("Donaciones de mayor a menor:\n")
            print('\n\n ')
            join(map(str, mayor_a_menor))
            print("\n Para volver ingrese 1:\n")
            while volv != 1:
                volv = int(input())

# Respuesta a opcion 6

        if res == 6 and len(nombre) > 0:
            menor_a_mayor.sort()
            os.system("clear")
            print("Donaciones de menor a mayor:\n")
            print('\n '.join(map(str, menor_a_mayor)))
            print("\n Para volver ingrese 1:\n")
            while volv != 1:
                volv = int(input())

# Respuesta a opcion 7

        if res == 7 and len(nombre) > 0:
            os.system("clear")
            while exist == False:
                search = input("Ingrese el nombre a buscar, si desea volver ingrese 1:\n")
                if search in nombre_sin_ordenar:
                    b = nombre_sin_ordenar.index(search)
                    print("\n", menor_a_mayor[b])
                    while volv != 1:
                        volv = int(input("\n\n Ingrese 1 para volver al menu:\n"))
                        exist = True
                elif search == "1":
                    exist = True
                else:
                    exist = False
                    os.system("clear")
                    print("El nombre que busca no es un donador.\n")

# Respuesta a opcion 8

        if res == 8 and len(nombre) > 0:
            os.system("clear")
            while exist == False:
                search = int(input("Ingrese el monto a buscar, si desea volver ingrese 1:\n"))

                if search in valor_sin_ordenar:
                    b = valor_sin_ordenar.index(search)
                    print("\n", menor_a_mayor[b])
                    while volv != 1:
                        volv = int(input("\n\n Ingrese 1 para volver al menu:\n"))
                        exist = True
                elif search == "1":
                    exist = True
                else:
                    exist = False
                    os.system("clear")
                    print("El monto que ingreso nunca fue donado.\n")

# Respuesta a opcion 0

        if res == 10:
            carga.guardar_vector_disco(nombre, "nombre.ong")
            carga.guardar_vector_disco(donacion, "donacion.ong")
            os.system("clear")
            print ("Gracias por su ayuda!")
            seguir = 0
            time.sleep(2.5)

        os.system("clear")
