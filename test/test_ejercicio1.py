import unittest
import ejercicio1

class ejercicio1Test(unittest.TestCase):

    def testRotarPalabraRecibeCadenaVaciaDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaVacia = ''
        # Act
        resultado = ejercicio1.rotarPalabra(cadenaVacia)
        # Assert
        self.assertTrue(resultado == [])


    def testRotarPalabraRecibeCadenaConSoloEspaciosYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaConEspacios = '    '
        # Act
        resultado = ejercicio1.rotarPalabra(cadenaConEspacios)
        # Assert
        self.assertEqual(resultado, [])


    def testRotarPalabraRecibeUnaLetraAMinusculaYDeberiaDevolverUnaListaConMismaLetraDentro(self):
            # Arrange
            cadena = 'a'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ['a'])


    def testRotarPalabraRecibeUnaCadenaDeDosCaracteresYDeberiaDevolverUnaListaCon2Rotaciones(self):
            # Arrange
            cadena = 'ab'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertEqual(resultado, ["ab", "ba"])


    def testRotarPalabraRecibeCadenaDeTresCaracteresYDeberiaDevolverUnaListaCon3Rotaciones(self):
            # Arrange
            cadena = 'paz'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ["paz", "azp", "zpa"])


    def testRotarPalabrasRecibeUnaCadenaConDosCaracteresUnEspacioYUnCaracterYDevuelveUnaListaCon4Rotaciones(self):
            # Arrange
            cadenaConEspacio = 'so l'
            # Act
            resultado = ejercicio1.rotarPalabra(cadenaConEspacio)
            # Assert
            self.assertEqual(resultado, ["so l", "o ls", " lso", "lso "])


    def testRotarPalabrasRecibeUnaCadenaDeCincoCaracteresYDeberiaDevolverUnaListaCon5Rotaciones(self):
            # Arrange
            cadena = 'rotar'
            # Act
            resultado = ejercicio1.rotarPalabra(cadena)
            # Assert
            self.assertTrue(resultado == ["rotar", "otarr", "tarro", "arrot", "rrota"])