package main

import (
	"errors"
)

func check_partida(rondas map[int][]int) error {
	if len(rondas) != 10 {
		return errors.New("mal tamaño de partida")
	}
	for _, element := range rondas {
		if len(element) == 1 {
			if element[0] < 0 || element[0] > 10 {
				return errors.New("formato de partida incorrecto")
			}
		} else {
			if element[0] < 0 || element[0] > 10 || element[1] > 10 || (element[0]+element[1]) > 10 {
				return errors.New("formato de partida incorrecto")
			}
		}

	}
	return nil
}

func sumarRondas(rondas map[int][]int) int {
	check_partida(rondas)
	result := 0
	for num_ronda, element := range rondas {
		if element[0] == 10 { //checks for strike
			strike(num_ronda, rondas, &result)
			continue
		} else {
			if (element[0] + element[1]) == 10 { //checks for spare
				spare(num_ronda, rondas, &result)
			} else {
				suma(num_ronda, rondas, &result) //if no spare nor strike, adds result
			}
		}
	}
	return result
}

func strike(num_ronda int, rondas map[int][]int, result *int) {
	if num_ronda == 10 { //checks for strike in last round
		strikeRondaFinal(rondas, result)
	} else {
		if rondas[num_ronda+1][0] == 10 { //checks if next ronda is strike
			if num_ronda == 9 { //avoids index out of bounds in 9th round
				*result += 10 + rondas[num_ronda+1][0] + rondas[num_ronda+1][1]
			} else { //Next round is strike, adds first ball of next two rounds
				*result += 10 + rondas[num_ronda+1][0] + rondas[num_ronda+2][0]
			}

		} else { //There is no strike in next round. Adds the points of next round
			*result += 10 + rondas[num_ronda+1][0] + rondas[num_ronda+1][1]
		}
	}

}

func strikeRondaFinal(rondas map[int][]int, result *int) {
	*result += 10 + rondas[10][1] + rondas[10][2]
}

func spare(num_rondas int, rondas map[int][]int, result *int) {
	if num_rondas == 10 { //checks for spare in last round
		spareRondaFinal(num_rondas, rondas, result)
	} else { //adds first ball of next round
		*result += rondas[num_rondas][0] + rondas[num_rondas][1] + rondas[num_rondas+1][0]
	}
}

func spareRondaFinal(num_rondas int, rondas map[int][]int, result *int) {
	*result += 10 + rondas[10][2] //adds third ball of last round
}

func suma(num_rondas int, rondas map[int][]int, result *int) {
	*result += rondas[num_rondas][0] + rondas[num_rondas][1] //adds both balls of current round
}
