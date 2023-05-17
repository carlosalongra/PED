import  unittest
from Partida import Game

class TestBolos(unittest.TestCase):

    # partida 
    def test_creo_partida(self):
        esperado = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        prueba = Game()
        resultado = prueba.tabla_juego
        self.assertEqual(esperado, resultado) 

    def test_check_partida(self):
        esperado = [[0,0],[0,0],[0,0],[0,0]]
        prueba = Game()
        resultado = prueba.tabla_juego
        self.assertLess(esperado, resultado)   

    def test_string_partida(self):
        prueba = Game()
        esperado = ["turno1", "turno2"]
        resultado = prueba.sumar_puntuaciones
        self.assertTrue(esperado, resultado) 

    def test_sumar_puntuacion(self):
        prueba = Game()
        esperado = [[1,0],[1,0],["tiro"],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        resultado = prueba.sumar_puntuaciones()
        self.assertTrue(esperado, resultado)
    
    # suma de bolos
    def test_sumar_puntuacion(self):
        prueba = Game()
        prueba.tabla_juego = [[1,0],[1,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        esperado = 3
        resultado = prueba.sumar_puntuaciones()
        self.assertEqual(esperado, resultado)

    # suma bolos mismo turno [1,1]
    def test_sumar_puntuacion_mismo_turno(self):
        prueba = Game()
        prueba.tabla_juego = [[1,1],[1,0],[0,1],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        esperado = 5
        resultado = prueba.sumar_puntuaciones()
        self.assertEqual(esperado, resultado)

    # suma mas de lo permitido
    def test_mas_bolos_tirados(self):
        prueba = Game()
        prueba.tabla_juego = [[11,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        resultado = prueba.sumar_puntuaciones()
        self.assertFalse(resultado)

    def test_bolos_negativos(self):
        prueba = Game()
        prueba.tabla_juego = [[-1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        resultado = prueba.sumar_puntuaciones()
        self.assertFalse(resultado)

    # bolo lanzado 
    def test_bolo_lanzado(self):
        prueba = Game()
        tirada = prueba.bolo_lanzado()
        esperado = sum(tirada) <= 10

    def test_bolo_lanzado_mayor_0(self):
        prueba = Game()
        tirada = prueba.bolo_lanzado()
        esperado = sum(tirada) >= 0

    def test_strike(self):
        prueba = Game()
        prueba.tabla_juego = [[10,0],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        esperado = 14
        resultado = prueba.Strike()
        self.assertEqual(esperado, resultado)

    def test_strike2(self):
        prueba = Game()
        prueba.tabla_juego = [[0,0],[10],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        esperado = 14
        resultado = prueba.Strike()
        self.assertEqual(esperado, resultado)

    def test_check_strike(self):
        prueba = Game()
        prueba.tabla_juego = [[10],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        turno = prueba.tabla_juego[0]
        self.assertTrue(prueba.check_strike(turno))

    def test_spare(self):
        prueba = Game()
        prueba.tabla_juego = [[0,0],[5,5],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        esperado = 13
        resultado = prueba.Spare()
        self.assertEqual(esperado, resultado)
    
    def test_check_spare(self):
        prueba = Game()
        prueba.tabla_juego = [[5,5],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        turno = prueba.tabla_juego[0]
        self.assertTrue(prueba.check_spare(turno))

    #def test_turno_bonus(self):
     #   prueba = Game()
      #  prueba.tabla_juego = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[10],[1,0]]
       # esperado = 11
        #resultado = prueba.turno_bonus()
        #self.assertTrue(resultado, esperado)
        

if __name__ == '__main__':
    unittest.main()


    


