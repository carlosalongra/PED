import unittest
import os, time

from MainServidor import Servidor

class TestServidor(unittest.TestCase):

        def test_fecha(self):
            sock = Servidor()
            fecha = time.strftime('')
            mensaje = 'fecha'
            fecha2 = sock.fecha(mensaje)
            self.assertEquals(fecha2, fecha)

if __name__ == '__main__':
    unittest.main()

