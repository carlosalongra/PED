package main

import (
	"log"
	"net"
	"os"
	"reflect"
	"unsafe"
	"time"
	"fmt"
	
)

func main() {
	SetProcessName("serv5")

	udpServer, err := net.ListenPacket("udp", ":5005")
	if err != nil {
		log.Fatal(err)
	}
	defer udpServer.Close()

	for {
		buf := make([]byte, 1024)
		_, addr, err := udpServer.ReadFrom(buf)
		if err != nil {
			continue
		}
		println("PID: ",string(buf))
		go response(udpServer, addr, buf)

	}

}

func response(udpServer net.PacketConn, addr net.Addr, buf []byte) {
	time := time.Now().Format(time.ANSIC)
	responseStr := fmt.Sprintf("Time: %v. ", time)

	udpServer.WriteTo([]byte(responseStr), addr)
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
