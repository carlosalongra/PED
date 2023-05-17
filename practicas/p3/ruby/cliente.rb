fifo_path = 'myfifo'

# Abre la FIFO para escritura
fifo_fd = File.open(fifo_path, 'w')

# Lee el path del fichero desde la línea de comandos
print "Introduce el path completo del fichero: "
file_path = gets.chomp

# Envía el path del fichero al servidor a través de la FIFO
fifo_fd.puts(file_path)

# Cierra la FIFO de escritura
fifo_fd.close

# Abre la FIFO para lectura
fifo_fd = File.open(fifo_path, 'r')

# Lee el contenido del fichero desde la FIFO y lo muestra en la salida estándar
while chunk = fifo_fd.read(1024)
  print chunk
end

# Cierra la FIFO de lectura
fifo_fd.close
