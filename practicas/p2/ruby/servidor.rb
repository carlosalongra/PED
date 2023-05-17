# Importamos la biblioteca de tuberías
require 'socket'

# Creamos la tubería con el nombre "fecha_hora"
pipe = 'fecha_hora'

# Creamos el servidor y lo ponemos en espera de conexiones
server = UNIXServer.new(pipe)
client = server.accept

# Obtenemos la fecha y hora actual del sistema
fecha_hora = Time.now

# Enviamos la fecha y hora al cliente
client.puts(fecha_hora.strftime("%Y-%m-%d %H:%M:%S %z"))

# Cerramos la conexión con el cliente
client.close

# Cerramos el servidor
server.close