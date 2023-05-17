import os
import time
import sys
fifo_lectura = "fifo_lectura"
fifo_escritura = "fifo_escritura"

if not os.path.exists(fifo_escritura): #checks if the file exists
    os.mkfifo(fifo_escritura)
if not os.path.exists(fifo_lectura): #checks if the file exists
    os.mkfifo(fifo_lectura)

fifo_lectura = open(fifo_lectura, "r") #opens the file in read mode
fifo_escritura = open(fifo_escritura, "w") #opens the file in write mode

while True:
    linea = fifo_lectura.readline() #reads the file
    if linea == "": #if the file is empty, it breaks the loop
        break
    print("Cliente: " + linea) #prints the client PID
    fifo_escritura.write("Servidor: " + time.asctime()) #writes the time
    fifo_escritura.flush() #flushes the file


fifo_escritura.close()
fifo_lectura.close() 