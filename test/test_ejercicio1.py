import unittest
import ejercicio1

class ejercicio1Test(unittest.TestCase):

    def testRotarPalabrasRecibeCadenaVaciaDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaVacia = ''
        # Act
        resultado = ejercicio1.rotarPalabra(cadenaVacia)
        # Assert
        self.assertTrue(resultado == [])


    def testRotarPalabrasRecibeCadenaConSoloEspaciosYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaConEspacios = '    '
        # Act
        resultado = ejercicio1.rotarPalabra(cadenaConEspacios)
        # Assert
        self.assertEqual(resultado, [])


    def testRotarPalabrasRecibeUnaLetraAMinusculaYDeberiaDevolverUnaListaConMismaLetraDentro(self):
            # Arrange
            cadena = 'a'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ['a'])


    def testRotarPalabrasRecibeUnaCadenaDeDosCaracteresYDeberiaDevolverUnaListaConSusTodasSusRotaciones(self):
            # Arrange
            cadena = 'ab'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertEqual(resultado, ["ab", "ba"])


    def testRotarPalabrasRecibeCadenaDeTresCaracteresYDeberiaDevolverUnaListaConTodasSusRotaciones(self):
            # Arrange
            cadena = 'paz'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ["paz", "azp", "zpa"])


    def testRotarPalabrasRecibeUnaCadenaConDosCaracteresUnEspacioYUnCaracterYDevuelveUnaListaConTodasSusRotaciones(self):
            # Arrange
            cadenaConEspacio = 'so l'
            # Act
            resultado = ejercicio1.rotarPalabra(cadenaConEspacio)
            # Assert
            self.assertEqual(resultado, ["so l", "o ls", " lso", "lso "])


    def testRotarPalabrasRecibeUnaCadenaDeCincoCaracteresYDeberiaDevolverUnaListaConTodasSusRotaciones(self):
            # Arrange
            cadena = 'rotar'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ["rotar", "otarr", "tarro", "arrot", "rrota"])