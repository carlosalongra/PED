import time, os, sys

timeformat = '%Y-%m-%d %H:%M:%S'

read, write = os.pipe()
r, w = os.fdopen(read, 'rb', 0), os.fdopen(write, 'wb', 0)

pid_0 = os.fork()
if pid_0:
    w.close()
    pid_1 = os.fork()
    if pid_1:
        r.close()
    else:
        data = r.readline()
        sys.stdout.write(data.decode('utf8').strip())
        r.close()
else:
    r.close()
    tiempo = time.strftime(timeformat)
    w.write(tiempo.encode('utf8'))
    w.flush()
    w.close()
