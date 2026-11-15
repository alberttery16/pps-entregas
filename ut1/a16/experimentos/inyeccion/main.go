package main

import (
	"fmt"
	"os"
	"os/exec"
)

func ejecutar(cmd *exec.Cmd) {
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		panic(err)
	}
}
func main() {
	entrada := "hola; echo ORDEN_INYECTADA"
	fmt.Println("INSEGURO: texto concatenado (2 órdenes echo)")
	ejecutar(exec.Command("bash", "-c", "echo "+entrada))
	fmt.Println("SEGURO: argumento separado (1 orden echo)")
	ejecutar(exec.Command("echo", entrada))
}
