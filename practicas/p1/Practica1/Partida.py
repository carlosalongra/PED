import random

class Game:

    def __init__(self):
        self.tabla_juego = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        
        #if self.check_type():
            #return False
    def sumar_puntuaciones(self):
        for elemento in self.tabla_juego:
            if type(elemento) == str:
                return False
            else:
                resultado = 0
                for elemento in self.tabla_juego:  
                    if(sum(elemento) >= 0):
                        if sum(elemento) < 10: 
                            resultado += sum(elemento)
                return resultado
            
    def bolo_lanzado(self):
        tirada = []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,(10 - tirada[0])))
        return tirada

    def Strike(self):
        resultado = 0
        for elemento in self.tabla_juego: 
            posicion = 0
            if self.check_strike(elemento):
                resultado += 10
                posicion += 1 
            else: 
                if True:
                    resultado += 2*(sum(elemento))
        return resultado
    
    def check_strike(self, turno):
        if turno[0] == 10:
            return True
        else:
            return False
        
    def Spare(self):
        resultado = 0
        for elemento in self.tabla_juego: 
            posicion = 0
            if self.check_spare(elemento):
                resultado += 10
                posicion += 1 
            else: 
                if True:
                    resultado = resultado + sum(elemento) + elemento[0]
        return resultado
    
    def check_spare(self, turno):
        if sum(turno) == 10:
            return True
        else:
            return False
        
    #def turno_bonus(self, turno):
     #   for elemento in self.tabla_juego:
      #      if turno[10] == 10:
       #         elemento += 1
    

