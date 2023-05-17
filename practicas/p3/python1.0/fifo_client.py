import os, time, sys
fifo_serv = 'prueba_fifo'

if not os.path.exists(fifo_serv):
    exit()

client_fifo = open(fifo_serv, 'r')
data = client_fifo.readline()
sys.stdout.write(data.strip())
client_fifo.close()

