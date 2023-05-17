# Importamos la biblioteca de tuberías
require 'socket'

# Creamos la tubería con el nombre "fecha_hora"
pipe = 'fecha_hora'

# Nos conectamos al servidor a través de la tubería
client = UNIXSocket.new(pipe)

# Leemos la respuesta del servidor y la mostramos en la salida standard
puts client.recv(1024)

# Cerramos la conexión con el servidor
client.close
