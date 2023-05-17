import os, time, sys
fifo_serv = 'prueba_fifo'

timeformat = '%Y-%m-%d %H:%M:%S'

if not os.path.exists(fifo_serv):
    os.mkfifo(fifo_serv)

while True:
    send_fifo = open(fifo_serv, 'w')
    tiempo = time.strftime(timeformat)  
    send_fifo.write(tiempo)
    send_fifo.close()

    

