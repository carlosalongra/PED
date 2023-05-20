import time

class RequestManager:

    def obtener_fecha(self):
        fecha_actual = time.strftime('%D')
        return fecha_actual
    
    def obtener_hora(self):
        hora_actual = time.strftime('%H:%M:%S')
        return hora_actual
        
    def responder(self, peticion):
        if peticion.decode('utf8') == 'hora':
            return self.obtener_hora()
        elif peticion.decode('utf8') == 'fecha':
            return self.obtener_fecha()
        else: 
            return 'error'



