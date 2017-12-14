import unittest
import ejercicio3

class ejercicio3test(unittest.TestCase):

    def testCalcularEquipoCampeonDeLigaRecibeListaVaciaDeberiaDevolverCadenaVacia(self):
        # Arrange
        listaVacia = []
        # Act
        resultado = ejercicio3.calcularEquipoCampeonDeLiga(listaVacia)
        # Assert
        self.assertEqual(resultado, "")

    def testCalcularEquipoCampeonDeLigaListaConTuplaDeCuatroElementosDeberiaDevolverEquipoConMayorPuntaje(self):
        # Arrange
        tuplaEnLista = [("a", 1, "b", 0)]
        # Act
        resultado = ejercicio3.calcularEquipoCampeonDeLiga(tuplaEnLista)
        # Assert
        self.assertTrue(resultado == "a")

    def testCalcularEquipoCampeonDeLigaRecibeListaConTuplasCadaUnoDeCuatroElementosDeberiaDevolverEquipoConMayorPuntaje(self):
        # Arrange
        listaDeTuplas = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]
        # Act
        resultado = ejercicio3.calcularEquipoCampeonDeLiga(listaDeTuplas)
        # Assert
        self.assertTrue(resultado == "c")

    def testCalcularEquipoCampeonDeLigaRecibeListaConTuplasCadaUnoDeCuatroElementosDeberiaDevolverEquipoConMayorPuntajeAlfabeticamente(self):
        # Arrange
        listaDeTuplas = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]
        # Act
        resultado = ejercicio3.calcularEquipoCampeonDeLiga(listaDeTuplas)
        # Assert
        self.assertTrue(resultado == "Almagro")

    def testCalcularEquipoCampeonDeLigaRecibeListaConTuplasDeCuatroElementosYDeberiaDevolverEquipoConMayorPuntaje(self):
        # Arrange
        listaDeTuplas = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]
        # Act
        resultado = ejercicio3.calcularEquipoCampeonDeLiga(listaDeTuplas)
        # Assert
        self.assertTrue(resultado == "a")