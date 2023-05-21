import unittest
from request import RequestManager

class TestClienteServidor(unittest.TestCase):

    def test_respuesta_fichero(self):
        servidor = RequestManager()
        fichero_prueba = open('fichero.txt'.encode('utf8').strip(), 'r')
        contenido = "Lineas: 5 \nPalabras: 18"
        resultado = RequestManager().funcion(fichero_prueba)
        self.assertEqual(contenido, resultado)


    def test_respuesta_services(self):
        servidor = RequestManager()
        fichero_prueba = open('/etc/services'.encode('utf8').strip(), 'r')
        contenido = "Lineas: 361 \nPalabras: 1773"
        resultado = RequestManager().funcion(fichero_prueba)
        self.assertEqual(contenido, resultado)

if __name__ == '__main__':
    unittest.main()

