package main

import (
	"fmt"
	"os"
	"reflect"
	"syscall"
	"unsafe"
)

func main() {
	// Set the new process name
	SetProcessName("Client3")
	fifo_cliente_a_servidor := "/tmp/fifo_cliente_a_servidor"
	fifo_servidor_a_cliente := "/tmp/fifo_servidor_a_cliente"

	//Create the FIFOs
	if err := syscall.Mkfifo(fifo_cliente_a_servidor, 0666); err != nil {
		fmt.Println(err)
	}
	if err := syscall.Mkfifo(fifo_servidor_a_cliente, 0666); err != nil {
		fmt.Println(err)
	}

	// Abrir el archivo fifo_cliente_a_servidor
	fifo_cliente_a_servidor_fd, err := syscall.Open(fifo_cliente_a_servidor, syscall.O_WRONLY, 0666)
	if err != nil {
		fmt.Println(err)
	}

	// Abrir el archivo fifo_servidor_a_cliente
	fifo_servidor_a_cliente_fd, err := syscall.Open(fifo_servidor_a_cliente, syscall.O_RDONLY, 0666)
	if err != nil {
		fmt.Println(err)
	}

	// Escribir en el fifo_cliente_a_servidor el PID del cliente
	pid := syscall.Getpid()
	_, err = syscall.Write(fifo_cliente_a_servidor_fd, []byte(fmt.Sprintf("%d", pid)))
	if err != nil {
		fmt.Println(err)
	}

	// Leer del fifo_servidor_a_cliente
	var buf [1024]byte
	n, err := syscall.Read(fifo_servidor_a_cliente_fd, buf[:])
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Leido del fifo_servidor_a_cliente: ", string(buf[:n]))

	// Cerrar los archivos
	syscall.Close(fifo_cliente_a_servidor_fd)
	syscall.Close(fifo_servidor_a_cliente_fd)

}

func SetProcessName(name string) error {
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
