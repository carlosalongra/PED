import unittest
from mainNUM import Romano

class Numeros(unittest.TestCase):
    
    #def test_uno(self):
     #   secuencia = Romano()
      #  secuencia.numero = "I"
       ## esperado = 1
        #equivale = secuencia.check()
        #self.assertTrue(esperado, equivale)

    def test_uno(self):
        secuencia = Romano()
        self.assertEqual("I", secuencia.cambio(1))

    def test_dos(self):
        secuencia = Romano()
        self.assertEqual("II", secuencia.cambio(2))
    
    def test_tres(self):
        secuencia = Romano()
        self.assertEqual("III", secuencia.cambio(3))
    
    def test_cuatro(self):
        secuencia = Romano()
        self.assertEqual("IV", secuencia.cambio(4))
        
    def test_cinco(self):
        secuencia = Romano()
        self.assertEqual("V", secuencia.cambio(5))

    def test_seis(self):
        secuencia = Romano()
        self.assertEqual("VI", secuencia.cambio(6))
    
    def test_siente(self):
        secuencia = Romano()
        self.assertEqual("VII", secuencia.cambio(7))

    def test_ocho(self):
        secuencia = Romano()
        self.assertEqual("VIII", secuencia.cambio(8))
    
    def test_nueve(self):
        secuencia = Romano()
        self.assertEqual("IX", secuencia.cambio(9))

    def test_diecisiete(self):
        secuencia = Romano()
        self.assertEqual("XVII", secuencia.cambio(17))
    
    def test_veinte(self):
        secuencia = Romano()
        self.assertEqual("XX", secuencia.cambio(20))

    def test_veinticuatro(self):
        secuencia = Romano()
        self.assertEqual("XXIV", secuencia.cambio(24))

    """def test_sin_vlaor(self):
        secuencia = Romano()
        self.assertEqual("Q", secuencia.cambio("")) """
    

    


if __name__ == '__main__':
    unittest.main()