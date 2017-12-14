import unittest
import ejercicio2

class ejercicio2Test(unittest.TestCase):

    def testCalcularPosicionesBarcosSobrevivientesRecibeUnMapaVacioYDeberiaDevolvereUnaListaVacia(self):
        # Arrange
        listaVacia = []
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaVacia, disparos)
        # Assert
        self.assertListEqual(resultado, [])


    def testCalcularPosicionesBarcosSobrevivientesRecibeCadenaVaciaYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaVacia = ''
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(cadenaVacia, disparos)
        # Assert
        self.assertTrue(resultado == [])


    def testCalcularPosicionesBarcosSobrevivientesRecibeCadenaSoloConEspaciosYDeberiaDevolverUnaListaVacia(self):
        # Arrage
        cadenaConEspacios = '     '
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(cadenaConEspacios, disparos)
        # Assert
        self.assertEqual(resultado, [])


    def testCalcularPosicionesBarcosSobrevivientesRecibeUnaListaConUnaCadenaDeCaracteresDistintosAPuntoOBLargaYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        listaConCadenaInesperada = ["soy NO valido"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaConCadenaInesperada, disparos)
        # Assert
        self.assertListEqual(resultado, [])

    def testCalcularPosicionesBarcosSobrevivientesRecibeOtraListaConCadenasDeCaracteresDistintosAPuntoOBLargaYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        listaConCadenasInesperadas = ["yo", "tambien", "soy", "invalido"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaConCadenasInesperadas, disparos)
        # Assert
        self.assertTrue(resultado == [])


    def testCalcularPosicionesBarcosSobrevivientesRecibeUnaListaConCadenasDeDistintoLargoYDeberiaDevolverUnaListaVacia(self):
        # Arrange
        listaConCadenasDeDistintoLargo = ["b.b.", "....", "..bb", "b.b"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaConCadenasDeDistintoLargo, disparos)
        # Assert
        self.assertEqual(resultado, [])


    def testCalcularPosicionesBarcosSobrevivientesRecibeUnMapaValidoYDeberiaDevolverUnaListaDeTuplasConPosicionesDeBotesIntactos(self):
        # Arrange
        listaValida = ["b.b..", "b...b", ".....", "....b"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaValida, disparos)
        # Assert
        self.assertListEqual(resultado, [(2, 1), (2, 5)])


    def testCalcularPosicionesBarcosSobrevivientesRecibeListaDeDisparosVaciaYUnMapaValidoYDeberiaDevolverUnaListaDeTuplasConPosicionesDeBotesIntactos(self):
        # Arrange
        listaValida = ["b..", "...", "..b"]
        disparosInvalidos = []
        # Act
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(listaValida, disparosInvalidos)
        # Assert
        self.assertTrue(resultado == [(1, 1), (3, 3)])