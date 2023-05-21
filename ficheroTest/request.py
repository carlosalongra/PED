
class RequestManager:

    def funcion(self, fichero):
        num_lineas = 0
        num_palabras = 0
        for linea in fichero:
            num_lineas += 1
            palabras = linea.split()
            num_palabras += len(palabras)
        resultado = f"Lineas: {num_lineas} \nPalabras: {num_palabras}"
        return resultado
        #lineas = ("Lineas: " + self.contar_lineas())
        #lineas = ("Palabras: " + self.contar_palabras())
        #return lineas + palabras

    #def contar_lineas(self):
     #   num_lineas = 0
      #  for lineas in self.fichero:
       #     num_lineas += 1
        #resultado = num_lineas
        #return resultado

    #def contar_palabras(self):
     #   num_palabras = 0
      #  for lineas in self.fichero:
       #     palabras = linea.split()
        #    num_palabras += len(palabras)
        #resultado = num_palabras
        #return resultado

        
