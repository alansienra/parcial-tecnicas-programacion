
def longitudDeFilasEnMapa(mapa):
    if len(mapa) > 0:
        longitudes = []
        for fila in mapa:
            longitudes.append(len(fila))
            longitudGenerica = longitudes[0]
        for longitud in longitudes:
            if longitud != longitudGenerica:
                return []


def revisarValidezDelMapa(mapa):
    if longitudDeFilasEnMapa(mapa) == []:
        return []
    if type(mapa) != list or len(mapa) < 1:
        return []
    if len(mapa) > 0 and len(mapa[0]) > 0:
        verificarCaracter = mapa[0][:2]
        cadenaValida = '.b'
        for caracter in verificarCaracter:
            if caracter not in cadenaValida:
                return []


def encuentraBotes(mapa):

    botes = []

    for fila in mapa:
        if 'b' in fila:
            coordenada = 0
            for caracter in fila:
                if caracter == 'b':
                    bote = (mapa.index(fila) + 1, coordenada + 1)
                    coordenada = coordenada + 1
                else:
                    coordenada = coordenada + 1
                    continue
                botes.append(bote)

    return botes


def eliminarBotes(botes, disparos):

    for disparo in disparos:

        if disparo in botes:
            botes.remove(disparo)

    return botes



def calcularPosicionesBarcosSobrevivientes(mapa, disparos):

    if revisarValidezDelMapa(mapa) == []:
        return []

    botesEnElMapa = encuentraBotes(mapa)
    sobrevivientes = eliminarBotes(botesEnElMapa, disparos)

    return sobrevivientes

def ejercicio2(var1,var2):
    return calcularPosicionesBarcosSobrevivientes(var1,var2)
