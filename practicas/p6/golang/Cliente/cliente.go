package main

import (
	"fmt"
	"net"
	"os"
	"reflect"
	"unsafe"
)

func main() {
	SetProcessName("cli6")

	// conectarse al servidor
	fmt.Println("Escribe la dirección del servidor")
	var direccion string
	fmt.Scanln(&direccion)
	conn, err := net.Dial("tcp", direccion+":5005")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	// enviar mensaje al servidor
	fmt.Println("Escribe la ruta del archivo")
	var ruta string
	fmt.Scanln(&ruta)
	_, err = conn.Write([]byte(ruta))
	if err != nil {
		fmt.Println(err)
		return
	}

	// recibir respuesta del servidor
	for {
		buffer := make([]byte, 512)
		longitud, err := conn.Read(buffer)
		if err != nil {
			if err.Error() == "EOF"{
				break
			}
			fmt.Println(err)
			return
		}

		fmt.Println(string(buffer[:longitud]))
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
