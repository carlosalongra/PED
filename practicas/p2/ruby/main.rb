IO.popen("wc -w ruby/prueba.txt") do |output|
    count = output.read.split.first.to_i
    puts "El archivo tiene #{count} palabras."
  end