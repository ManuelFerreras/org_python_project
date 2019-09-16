import pickle
import os.path


def guardar_vector_disco(vector, nombre_archivo):
    """
    Guarda un vector dentro de el archivo, pisando el archivo anterior.

    Argumentos:
    vector         -- El vector a guardar
    nombre_archivo -- El archivo donde se guardara el vector
    """
    if len(vector) > 0:
        archivo = open(nombre_archivo, 'wb')
        tamano = len(vector)
        for i in range(tamano):
            pickle.dump(vector[i], archivo)
        archivo.close()
    else:
        print("El vector esta vacio, no se guardara nada!")

def clear_archivo(nombre_archivo):
    archivo = open(nombre_archivo, 'w')
    archivo.close()

def leer_archivo(vector, nombre_archivo):
    """
    Carga un vector desde el archivo.
    El vector dado debe existir, y no se borrará, sino que se agregaran elementos en el

    Argumentos:
    vector         -- El vector a cargar
    nombre_archivo -- El archivo de donde se carga el vector
    """
    if os.path.exists(nombre_archivo):
        archivo = open(nombre_archivo, 'rb')
        tamano = os.path.getsize(nombre_archivo)
        if tamano < 1:
            print("No hay datos")
        while archivo.tell() < tamano:
            elemento = pickle.load(archivo)
            vector.append(elemento)
    else:
        print("El Archivo no Existe!!")
