package main

import "fmt"

func main() {
	// probability of tossing two fair six-sided dice that their values
	// rolled are different and their sum will be equal to 6
	var S []int
	var A []int
	for dice1 := 1; dice1 <= 6; dice1++ {
		for dice2 := 1; dice2 <= 6; dice2++ {
			val := dice1 + dice2
			S = append(S, val)
			if val == 6 && dice1 != dice2 {
				A = append(A, val)
			}
		}
	}
	fmt.Println(A)
	fmt.Println(S)
	fmt.Println(len(A), " / ", len(S))
}
