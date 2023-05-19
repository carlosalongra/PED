
class Romano:
        #if numero == 2:                     numero = ''
         #   return "II"                     if n == 6: 
        #elif numero == 1:                   numero = "VI"
            #return "I"                      if n == 5:
        #                                    numero = "V"
        # "REFACTOR 1"                       else:
        #                                    for x in range(n):
        #                                    numero += 'I'
        #                                    return numero 
        #                               
        #                                    "REFACTOR 2"

        #   numero += "V"   suma V a los valores restante = 5, en este caso valora 6, 7 (restando 5 se queda con 1 y 2) 
        #   los que pasaran a x in range ya que no es 4 
        #   restante -= 5

    """ def cambio(self, n):
        numero = ''
        restante = n
        if restante >= 10:
            numero += "X"
            restante -= 10
        if restante == 9:
            numero += "IX"
            restante -= 9                       ##      REFACTOR  3    ##
        if restante >= 5:                    ## vemos que la funcion se repite##   --> lo sacamos a otra funcion
            numero += "V"                    ##         numero += ??          ##  
            restante -= 5                    ##         restante -= ??         ##
        if restante == 4:
            numero += "IV"
            restante -= 4
        for x in range(restante):
            numero += 'I'
        return numero """

    def cambio(self, n):
        numero = ''
        restante = n
        numero, restante = self.append_valores(restante, 24, "XXIV", numero)
        numero, restante = self.append_valores(restante, 20, "XX", numero)
        numero, restante = self.append_valores(restante, 10, "X", numero)
        numero, restante = self.append_valores(restante, 9, "IX", numero)
        numero, restante = self.append_valores(restante, 5, "V", numero)
        numero, restante = self.append_valores(restante, 4, "IV", numero)
        for x in range(restante):
            numero += 'I'
        return numero 

    def append_valores(self, n, decimal, numero_romano, numero):
        restante = n 
        if restante >= decimal:
            numero = numero + numero_romano
            restante -= decimal
        return numero, restante
