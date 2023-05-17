import os
from binaryornot.check import is_binary
import setproctitle
import time

# Set the new process name
new_process_name = "CliServ2"
setproctitle.setproctitle(new_process_name)

# Verify the new process name
current_process_name = setproctitle.getproctitle()
print("Current process name: ", current_process_name)


filepath = input('Enter document path: ') #Get the path to the file
binary = is_binary(filepath) #Check if the file is binary


read_descriptor1, write_descriptor1 = os.pipe() #Parent to child pipe
if not binary:
    read_obj1, write_obj1 = os.fdopen(read_descriptor1, 'r', 10), os.fdopen(write_descriptor1, 'w', 10) #is read only, w is write only, file objects
else:
    read_obj1, write_obj1 = os.fdopen(read_descriptor1, 'rb', 10), os.fdopen(write_descriptor1, 'wb', 10) #is read binary only and write binary only, file objects


read_descriptor2, write_descriptor2 = os.pipe() #Child to parent pipe
read_obj2, write_obj2 = os.fdopen(read_descriptor2, 'r', 10), os.fdopen(write_descriptor2, 'w', 10)

pid = os.fork()

if pid == 0:
    # Child
    read_obj2.close() #Close the read end of the child to parent pipe
    write_obj1.close() #Close the write end of the parent to child pipe

    write_obj2.write(filepath) #Write the path to the file to the child-to-parent pipe
    write_obj2.close()

    while True:
        data = read_obj1.readline()
        if not data:
            break
        print(data.strip())
    read_obj1.close()


else:
    # Parent
    read_obj1.close() #Close the read end of the parent to child pipe
    write_obj2.close() #Close the write end of the child to parent pipe

    while True:
        data = read_obj2.readline()
        if not data:
            break
        if binary:
            with open(data.strip(), 'rb') as f: #Open the file in binary mode
                for line in f:
                    write_obj1.write(line)
        else:
            with open(data.strip(), 'r') as f: #Open the file in text mode
                for line in f:
                    write_obj1.write(line)
    write_obj1.close()

    read_obj2.close()