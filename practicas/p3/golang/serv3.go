package main

import (
	"fmt"
	"os"
	"syscall"
	"time"
	"reflect"
	"unsafe"
)

func main() {
	// Set the new process name
	SetProcessNames("Serv3")
	fifo_cliente_a_servidor := "/tmp/fifo_cliente_a_servidor"
	fifo_servidor_a_cliente := "/tmp/fifo_servidor_a_cliente"

	for {
		// Abrir el archivo fifo_cliente_a_servidor
		fifo_cliente_a_servidor_fd, err := syscall.Open(fifo_cliente_a_servidor, syscall.O_RDONLY, 0666)
		if err != nil {
			fmt.Println(err)
			continue
		}

		// Abrir el archivo fifo_servidor_a_cliente
		fifo_servidor_a_cliente_fd, err := syscall.Open(fifo_servidor_a_cliente, syscall.O_WRONLY, 0666)
		if err != nil {
			fmt.Println(err)
			continue
		}

		// Leer del fifo_cliente_a_servidor
		var buf [1024]byte
		n, err := syscall.Read(fifo_cliente_a_servidor_fd, buf[:])
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("PID del cliente: ", string(buf[:n]))
		// Escribir en el fifo_servidor_a_cliente
		_, err = syscall.Write(fifo_servidor_a_cliente_fd, []byte(time.Now().String()))
		if err != nil {
			fmt.Println(err)
		}

		time.Sleep(1 * time.Second)

		// Cerrar los archivos
		syscall.Close(fifo_cliente_a_servidor_fd)
		syscall.Close(fifo_servidor_a_cliente_fd)
	}
	
	// The program will never reach here unless the loop is exited manually
	fmt.Println("Program exited.")
	os.Exit(0)
}

func SetProcessNames(name string) error {
	argv0str := (*reflect.StringHeader)(unsafe.Pointer(&os.Args[0]))
	  argv0 := (*[1 << 30]byte)(unsafe.Pointer(argv0str.Data))[:argv0str.Len]
  
	  n := copy(argv0, name)
	  if n < len(argv0) {
		  argv0[n] = 0
	  }
	
	//
	//bytes := append([]byte(name), 0)
	//ptr := unsafe.Pointer(&bytes[0])
  //
	//if _, _, errno := syscall.RawSyscall6(syscall.SYS_PRCTL, syscall.PR_SET_NAME, uintptr(ptr), 0, 0, 0, 0); errno != 0 {
	//	return syscall.Errno(errno)
	//  	}
	return nil
  }

