package main

import (
	"fmt"
	"net"
	"os"
	"reflect"
	"unsafe"
)

func main() {
	SetProcessName("serv6")

	// Crear direccion TCP en donde escuchar
	listenAddress, err := net.ResolveTCPAddr("tcp", "0.0.0.0:5005")
	if err != nil {
		fmt.Println(err)
		return
	}
	 

	// Escuchar en direccion TCP
	listener, err := net.ListenTCP("tcp", listenAddress)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer listener.Close()

	// Aceptar conexiones entrantes
	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}

		// Manejar conexion entrante
		go handleConnection(conn)
	}

}

// Manejar conexion entrante
func handleConnection(conn net.Conn) {
	// Cerrar conexion al terminar
	defer conn.Close()

	// Buffer para leer datos
	var buf [1024]byte

	// Leer datos desde conexion
	n, err := conn.Read(buf[:])
	if err != nil {
		fmt.Println(err)
		return
	}

	// Imprimir datos recibidos
	ruta := string(buf[:n])

	// Abrir archivo de la ruta recibida
	file, err := os.Open(ruta)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Enviar contenido del archivo
	for {
		_, err = file.Read(buf[:])
		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			fmt.Println(err)
			return
		}

		// Enviar contenido del archivo
		_, err = conn.Write(buf[:])
		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			fmt.Println(err)
			return
		}
	}
}

// SetProcessName sets the process name
func SetProcessName(name string) error {
	argv0str := (*reflect.StringHeader)(unsafe.Pointer(&os.Args[0]))
	argv0 := (*[1 << 30]byte)(unsafe.Pointer(argv0str.Data))[:argv0str.Len]

	n := copy(argv0, name)
	if n < len(argv0) {
		argv0[n] = 0
	}
	return nil
}
