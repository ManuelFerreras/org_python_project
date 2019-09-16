
#!/bin/python3

# Trabajo Practico de Vacaciones
# Integrantes: Franco Casavecchia & Manuel Ferreras   4to Año "C"

import os # importa comandos del SO
import re # utilizado para los colores
import time # para poder hacer esperar el programa
import carga

#Importa los otros archivos
from carga import *
from funciones import *
from menu import *

nombre = []
donacione = []

os.system("clear")

cargar_datos = input("Si desea cargar los datos de su ultima sesion ingrese 1\n")

# Inicializacion de variables

os.system("clear")

donadores = []
restar = 0
menor_a_mayor = []
mayor_a_menor = []
minima_donacion  = 0
maxima_donacion = 0
nombre_del_max = ""
nombre_del_min = ""
donacion = []
seguir = 1
maxima_donacion_posible = 1000000 # es la cantidad de dinero necesaria para la organizacion

if cargar_datos.isnumeric() and cargar_datos == "1":
    leer_archivo(nombre, 'cargas.txt')
    leer_archivo(donacione, 'donacione.txt')

valor_sin_ordenar = donacione.copy()
nombre_sin_ordenar = nombre.copy()

if len(donacione) > 0:
    minima_donacion = min(donacione)
    maxima_donacion = max(donacione)
    nombre_del_max = nombre[donacione.index(maxima_donacion)]
    nombre_del_min = nombre[donacione.index(minima_donacion)]
    menor_a_mayor = donacione.copy()
    mayor_a_menor = donacione.copy()

for i in range(0, len(donacione)):
    maxima_donacion_posible -= donacione[i]

for i in range(0, len(donacione)):
    donadores += [[nombre[i], donacione[i]]]
#Inicio del programaoa

while seguir == 1:
    res = 0
    volver = 0
    back = 0
    exist = False
    print(cambiar_color(1, 38)+"Bienvenido a la ORG Caritas Argentina\n")
    print("Esta organizacion recauda fondos para niños que necesitan en Argentina\n")
    print(texto_menu(maxima_donacion_posible))

    if res < 1 or res > 10:
        res = input("\nEliga una opcion: \n")
        if res == "":
            res = 0
        elif not res.isalpha():
            res = int(res)
        else:
            res = 0
        #Opcion 9
        if res == 9:
            os.system("clear")
            print(historia())
            input("\n\nSi desea volver al menu presione enter\n")
            os.system("clear")

        # Opcion 1
        elif res == 1:
            verificador = 1
            os.system("clear")
            if maxima_donacion_posible == 0:
                verificador = 0
                print("Se ha logrado la meta de donaciones\n")
                input("Para regresar al menu ingrese enter")
            print("La donacion maxima puede ser de $",maxima_donacion_posible)
            while verificador == 1: # verificador es una variable que sirve para que se verifique si el nombre ha sido correctame ingresado y si la donacion tambien es correcta
                name = input("\nIngrese el nombre del donador, para volver al menu ingrese enter\n") # Una variable auxiliar con la cual se podra hacer una

                if name == "":
                    os.system("clear")
                    verificador = 0
                elif not name.isalpha():
                    nombre_del_min = name
                    print("\nEl nombre no puede contener valores numericos ni espacios\n")
                else:
                    valor = input("Ingrese el valor de la donacion\n")
                    if not valor.isnumeric():
                        print("El valor es incorrecto\n")
                    else:
                        valor = int(valor)
                        if valor > 0 and valor <= maxima_donacion_posible:
                            donacion += [valor]
                            nombre_sin_ordenar.append(name)
                            nombre.append(name)
                            donacione.append(valor)
                            valor_sin_ordenar.append(valor)
                            verificador = 0
                            donador = [name, valor]
                            donadores += [donador]
                            mayor_a_menor.append(valor) # Se agrega el valor ingresado al vector de mayor a menor
                            menor_a_mayor.append(valor) # Se agrega el valor ingresado al vector de menor a mayor

                            maxima_donacion_posible = maxima_donacion_posible - valor

                            if valor > maxima_donacion:
                                maxima_donacion = valor
                                nombre_del_max = name
                            elif valor < minima_donacion:
                                minima_donacion = valor
                                nombre_del_min = name
                                nombre_del_min = name

                            if minima_donacion == 0:
                                minima_donacion = valor
                                nombre_del_min = name

                            os.system("clear")
                            print("Gracias por su donacion")
                            time.sleep(0.5)
                            os.system("clear") #Limpia la pantalla

                        else:
                            print("La donacion no puede ser menor o igual a 0 y la donacion no puede ser superior a" ,maxima_donacion_posible, "pesos")

        # Opcion 2
        elif res == 2: #and len(nombre):
            os.system("clear")
            print(mostrar_donadores(donadores))
            input("\n\nSi desea volver al menu presione enter\n")
            os.system("clear")

        # Opcion 3
        elif res == 3 and len(donadores) > 0:
            os.system("clear")
            print("\nLa maxima donacion recibida fue de $" ,maxima_donacion, "y fue emitida por" ,nombre_del_max )
            input("\nSi desea volver al menu presione enter\n")

        # Opcion 4
        elif res == 4 and len(donadores) > 0:
            os.system("clear")
            print("\nLa minima donacion recibida fue de $" ,minima_donacion, "y fue emitida por" ,nombre_del_min )
            input("\n\nSi desea volver al menu presione enter\n")

        # Opcion 5
        elif res == 5 and len(donadores) > 0:
            bubblesort_M_a_m(mayor_a_menor)
            os.system("clear")
            print("Donaciones de mayor a menor:\n")
            print("$" + ", $".join(map(str, mayor_a_menor)))
            input("\n Si desea volver al menu presione enter\n")

        # Opcion 6
        elif res == 6 and len(donadores) > 0:
            bubblesort_m_a_M(menor_a_mayor)
            os.system("clear")
            print("Donaciones de menor a mayor:\n")
            print("$" + ", $".join(map(str, menor_a_mayor)))
            input("\nSi desea volver al menu presione enter\n")

        # Opcion 7
        elif res == 7 and len(donadores) > 0:
            os.system("clear")
            while exist == False:
                search = input("Ingrese el nombre a buscar, si desea volver ingrese enter:\n")
                if search == "":
                    exist = True
                if search.isalpha and search in nombre_sin_ordenar:
                    b = nombre_sin_ordenar.index(search)
                    print("\n", "El usuario", nombre_sin_ordenar[b], "Dono $", valor_sin_ordenar[b])
                    exist = True
                    input("\n\n Para volver al menu presione enter\n")
                elif not search.isalpha():
                    print("El nombre no puede contener caracteres numericos\n")
                else:
                    os.system("clear")
                    print("El nombre que busca no es un donador.\n")

        # Opcion 8
        elif res == 8 and len(donadores) > 0:
            os.system("clear")
            while exist == False:
                search = input("Ingrese el monto a buscar, si desea volver ingrese enter:\n")
                if search == "":
                    exist = True
                elif search.isnumeric():
                    search = int(search)
                    if search in valor_sin_ordenar:
                        b = valor_sin_ordenar.index(search)
                        print("\n", "El usuario que dono ese monto fue:" ,nombre_sin_ordenar[b])
                        exist = True
                        input("\nPara volver al menu presione enter\n")

                elif search.isalpha():
                    print("El valor no puede contener caracteres que no sean numericos\n")

                else:
                    os.system("clear")
                    print("El monto que ingreso nunca fue donado.\n")



        # Opcion 10
        elif res == 10:

            os.system("clear")
            print ("Gracias por su ayuda!")
            seguir = 0
            res = 10
            time.sleep(1.5)
            clear_archivo('/home/franco/Proyecto/cargas.txt')
            clear_archivo('/home/franco/Proyecto/donacione.txt')
            guardar_vector_disco(donacione, 'donacione.txt')
            print(donacione)
            guardar_vector_disco(nombre, 'cargas.txt')

        os.system("clear")
