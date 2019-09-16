

def bubblesort_M_a_m(list):
    while True:
        corrected = False
        for i in range(0, len(list) - 1):
          if list[i] < list [i+1]:
              list[i], list[i+1] = list[i+1], list[i]
              corrected = True
          if not corrected:
              return list

def bubblesort_m_a_M(list):
    for a in range(len(list)-1,0,-1):
        for b in range(a):
            if list[b] > list[b+1]:
                temp = list[b+1]
                list[b+1] =  list[b]
                list[b] = temp
            else:
                pass

def mostrar_donador(donador):
    texto = ""
    texto += "Nombre Donador: " + donador[0] + "\n"
    texto += "\tDonacion {}: ${}\n\n".format(1, donador[1])
    return texto

def mostrar_donadores(donadores):
    texto = ""
    for i in donadores:
        texto += mostrar_donador(i)
    return texto
