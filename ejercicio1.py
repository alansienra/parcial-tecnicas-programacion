
def rotarPalabra(palabra):
    rotacion = []
    alerta = "no_espacio"
    for letra in palabra:
        if letra == " ":
            rotacion.append (letra)
        else:
            rotacion.append(alerta)
        if len (palabra) < 1 or alerta not in rotacion:
            return []


    rotacion2 = []
    rotar = len (palabra)
    ultimaLetra = -1
    for i in range (rotar):
        rotar1 = palabra [ultimaLetra:] + palabra[:ultimaLetra]
        rotacion2.append (rotar1)
        ultimaLetra= ultimaLetra - 1
    rotacion2 = rotacion2[::-1]
    return rotacion2