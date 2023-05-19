import unittest
import os, time

from MainServidor import Servidor

class TestServidor(unittest.TestCase):

        def test_socket(self):
            sock = Servidor()
            con = input('')
            sok2 = sock.socket(path_sok)
            self.assertEquals(sok2, con)

if __name__ == '__main__':
    unittest.main()

