
def puntajeDeEquipos(lista):
    tabla = []
    for tupla in lista:
        if tupla[1] == tupla[3]:
            tabla.append((tupla[0],1))
            tabla.append((tupla[2],1))
        if tupla[1] > tupla[3]:
            tabla.append((tupla[0],2))
            tabla.append((tupla[2],0))
        if tupla[1] < tupla[3]:
            tabla.append((tupla[2],2))
            tabla.append((tupla[0],0))
    return tabla

def sumatoriaDePuntaje(resultados):
    tabla = {}
    for lista in resultados:
        if lista[0] not in tabla:
            tabla[lista[0]] = lista[1]
        else:
            tabla[lista[0]] = tabla[lista[0]] + lista[1]
    return tabla

def determinarCampeonDeLiga(diccionario):
    maximoPuntaje = max(diccionario.values())
    for equipo in diccionario:
        if diccionario[equipo] == maximoPuntaje:
            return equipo


def chequearIgualdadDePuntos(diccionario):
    puntajes = list(diccionario.values())
    puntaje1 = puntajes[0]
    for puntaje in puntajes[1:]:
        if puntaje == puntaje1:
            resultado = False
        else:
            resultado = True
        return resultado


def OrdenarDiccionario(diccionario):
    equipos = sorted(list(diccionario.keys()))
    return equipos[0]


def calcularEquipoCampeonDeLiga(lista):
    if len(lista) < 1:
        return ""
    listaDeTuplas = puntajeDeEquipos(lista)
    diccionario = sumatoriaDePuntaje(listaDeTuplas)
    if chequearIgualdadDePuntos(diccionario) == False:
        return OrdenarDiccionario(diccionario)
    return determinarCampeonDeLiga(diccionario)



def ejercicio3(var1):
    return calcularEquipoCampeonDeLiga(var1)



assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")