import time

class RequestManager:
    
    def responder(self, peticion):
        if peticion == 'hora':
            hora = time.strftime('%H:%M:%S')
            return hora
        elif peticion == 'fecha':
            fecha = time.strftime('m%-%d-%Y')
            return fecha
        else: 
            return 'error'

    if __name__ == '__main__':
        unittest.main()


