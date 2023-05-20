import time, unittest
from request import RequestManager

class TestClienteServidor(unittest.TestCase):
    
    def test_respuesta_fecha(self):
        servidor = RequestManager()
        esperado = time.strftime('%D')
        self.assertTrue(esperado, servidor.obtener_fecha)


    def test_respuesta_hora(self):
        servidor = RequestManager()
        esperado = time.strftime('%H:%M:%S')
        self.assertTrue(esperado, servidor.obtener_hora)
    
    #def test_respuesta_error(self):
     #   servidor = RequestManager()
      #  esperado = 'error'
       # self.assertEqual(esperado, servidor.responder(''))

if __name__ == '__main__':
    unittest.main()
