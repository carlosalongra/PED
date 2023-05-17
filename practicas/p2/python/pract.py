import os

readp1, writep1 = os.pipe()
r1, w1 = os.fdopen(readp1, 'rb', 0), os.fdopen(writep1, 'wb', 0)


readp2, writep2 = os.pipe()
r2, w2 = os.fdopen(readp2, 'rb', 0), os.fdopen(writep2, 'wb', 0)

pid_0 = os.fork()

if pid_0:
    w2.close()
    r1.close()

    path = './fichero.txt\n'
    w1.write(path.encode('utf'))
    #w1.write("\n".encode('utf'))
    while True:
        data = r2.readline()
        print(data.decode('utf8').strip())
    w1.close()
    r2.close()
    
else:
    w1.close()
    r2.close()
    data = r1.readline()
    fichero = open(data.decode('utf8').strip(), 'r')
    line = f.readline()
    while True:
        w2.write(line.encode('utf'))
        w2.flush()
        line = f.readline()
        
    w2.close()
    r1.close()

