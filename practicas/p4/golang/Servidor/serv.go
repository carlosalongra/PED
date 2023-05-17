package main

import (
	"fmt"
	"reflect"
	"unsafe"
	"os"
	"net"
	"io"
)

func main(){
	SetProcessName("serv4")
	var socket_name string
	fmt.Println("Ingrese el nombre del socket: ")
	fmt.Scanln(&socket_name)
	

	// Remove any existing socket file
	socket := "/tmp/" + socket_name
    os.Remove(socket)

	// Create a new socket
	l, err := net.Listen("unix", socket)
	if err != nil {
		fmt.Println("Error al crear el socket")
		return
	}
	defer l.Close()

	// Accept a connection
	for {
			conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error al aceptar la conexion")
			break
		}

		// Handle the connection
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
    defer conn.Close()

    // Read incoming path from client
    buf := make([]byte, 1024)
    n, err := conn.Read(buf)
    if err != nil {
        fmt.Println("Error reading:", err.Error())
        return
    }
	// Save incoming path to variable
    path := string(buf[:n])

	// Open the file
	file, err := os.Open(path)
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    // Send the file contents by chunks
    for {
        n, err := file.Read(buf)
        if err == io.EOF {
            break
        }

        _, err = conn.Write(buf[:n])
        if err != nil {
            fmt.Println("error writing to the conn:", err)
            break
        }
    }

}

//SetProcessName sets the process name
func SetProcessName(name string) error {
	argv0str := (*reflect.StringHeader)(unsafe.Pointer(&os.Args[0]))
	  argv0 := (*[1 << 30]byte)(unsafe.Pointer(argv0str.Data))[:argv0str.Len]
  
	  n := copy(argv0, name)
	  if n < len(argv0) {
		  argv0[n] = 0
	  }
	return nil
  }
