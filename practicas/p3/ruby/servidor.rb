fifo_path = 'myfifo'

# Crea la FIFO si no existe
if not File.exists?(fifo_path)
  system("mkfifo #{fifo_path}")
end

# Abre la FIFO para lectura
fifo_fd = File.open(fifo_path, 'r')

# Lee el path del fichero que envía el cliente
file_path = fifo_fd.gets.chomp

# Cierra la FIFO de lectura
fifo_fd.close

# Intenta abrir el fichero y enviar su contenido a través de la FIFO
begin
  file_size = File.size(file_path)
  fifo_fd = File.open(fifo_path, 'w')
  File.open(file_path, 'rb') do |file|
    while chunk = file.read(1024)
      fifo_fd.write(chunk)
    end
  end
rescue
  error_message = "Error al abrir el fichero #{file_path}"
  fifo_fd = File.open(fifo_path, 'w')
  fifo_fd.puts(error_message)
end

# Cierra la FIFO
fifo_fd.close
