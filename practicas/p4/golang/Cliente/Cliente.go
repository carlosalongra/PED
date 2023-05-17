package main

import (
	"fmt"
	"net"
	"os"
	"reflect"
	"unsafe"
)

func main() {
	SetProcessName("cli4")
	// Connect to the server's Unix Domain Socket
	var socket_name string
	fmt.Println("Ingrese el nombre del socket: ")
	fmt.Scanln(&socket_name)
	socket := "/tmp/" + socket_name

	conn, err := net.Dial("unix", socket)
	if err != nil {
		fmt.Println("Error connecting:", err.Error())
		return
	}
	defer conn.Close()

	// Send a path to the server
	var path string
	fmt.Print("Enter path: ")
	fmt.Scanln(&path)
	_, err = conn.Write([]byte(path))
	if err != nil {
		fmt.Println("Error writing:", err.Error())
		return
	}

	// Read the response from the server
	for {
		buf := make([]byte, 1024)
		n, err := conn.Read(buf)
		if err != nil {
			if err.Error() == "EOF" {
				return
			}
			fmt.Println("Error reading:", err.Error())
			return
		}
		fmt.Println("Contenido:", string(buf[:n]))
	}

}

// SetProcessName sets the name of the current process to |name|.
func SetProcessName(name string) error {
	argv0str := (*reflect.StringHeader)(unsafe.Pointer(&os.Args[0]))
	argv0 := (*[1 << 30]byte)(unsafe.Pointer(argv0str.Data))[:argv0str.Len]

	n := copy(argv0, name)
	if n < len(argv0) {
		argv0[n] = 0
	}
	return nil
}
