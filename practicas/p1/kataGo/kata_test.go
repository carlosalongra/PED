package main

import (
	"testing"
)

func TestNumeroDeRondas(t *testing.T) {
	rondas := map[int][]int{1: {0, 0}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}

	result := check_partida(rondas)

	if result != nil {
		t.Errorf("No se ha introducido un tamaño correcto de partida")
	}
}

func TestNumeroIncorrectoDeRondas(t *testing.T) {
	rondas := map[int][]int{1: {-1, 0}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}, 11: {0, 0}}

	result := check_partida(rondas)

	if result == nil {
		t.Errorf("No funciona método de chequeo de partidas")
	}
}

func TestSumarRondasSimple(t *testing.T) {
	rondas := map[int][]int{1: {1, 0}, 2: {1, 0}, 3: {0, 0}, 4: {0, 0}, 5: {1, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := sumarRondas(rondas)
	expected := 3
	if result != expected {
		t.Errorf("No se ha sumado correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}

func TestStrike(t *testing.T) {
	rondas := map[int][]int{1: {10}, 2: {2, 2}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := sumarRondas(rondas)
	expected := 18
	if result != expected {
		t.Errorf("No se ha sumado el strike correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}
func TestDosStrikesSeguidos(t *testing.T) {
	rondas := map[int][]int{1: {10}, 2: {10}, 3: {2, 2}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := sumarRondas(rondas)
	expected := 40
	if result != expected {
		t.Errorf("No se ha sumado correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}

func TestStrikeAlFinal(t *testing.T) {
	rondas := map[int][]int{1: {0, 0}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {10, 2, 3}}
	result := sumarRondas(rondas)
	expected := 15
	if result != expected {
		t.Errorf("No se ha sumado correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}
func TestStrikeAlFinalConPartidaNormal(t *testing.T) {
	rondas := map[int][]int{1: {3, 2}, 2: {5, 0}, 3: {5, 0}, 4: {3, 2}, 5: {5, 0}, 6: {5, 0}, 7: {5, 0}, 8: {5, 0}, 9: {5, 0}, 10: {10, 4, 1}}
	result := sumarRondas(rondas)
	expected := 60
	if result != expected {
		t.Errorf("No se ha sumado el strike correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}
 
func TestSpare(t *testing.T) {
	rondas := map[int][]int{1: {5, 5}, 2: {3, 2}, 3: {7, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := sumarRondas(rondas)
	expected := 25
	if result != expected {
		t.Errorf("No se ha sumado el spare correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}
func TestSpareEnd(t *testing.T) {
	rondas := map[int][]int{1: {0, 0}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {5, 5, 1}}
	result := sumarRondas(rondas)
	expected := 11
	if result != expected {
		t.Errorf("No se ha sumado el spare correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}

func TestPartidaPerfecta(t *testing.T) {
	rondas := map[int][]int{1: {10}, 2: {10}, 3: {10}, 4: {10}, 5: {10}, 6: {10}, 7: {10}, 8: {10}, 9: {10}, 10: {10, 10, 10}}
	result := sumarRondas(rondas)
	expected := 300
	if result != expected {
		t.Errorf("No se ha sumado correctamente. Se esperaba: %d, y se devolvió: %d", expected, result)
	}
}


func TestBolasNegativas(t *testing.T) {
	rondas := map[int][]int{1: {-1, 0}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := check_partida(rondas)

	if result == nil {
		t.Errorf("No funciona método de chequeo de partidas")
	}
}

func TestRondaConMasDeDiezPuntos(t *testing.T) {
	rondas := map[int][]int{1: {9, 9}, 2: {0, 0}, 3: {0, 0}, 4: {0, 0}, 5: {0, 0}, 6: {0, 0}, 7: {0, 0}, 8: {0, 0}, 9: {0, 0}, 10: {0, 0}}
	result := check_partida(rondas)

	if result == nil {
		t.Errorf("No funciona método de chequeo de partidas")
	}


}
