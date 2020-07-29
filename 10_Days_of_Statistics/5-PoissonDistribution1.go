package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// TODO: work out better way to deal with negative
// and fractional exponents
/*
func exponent(num, exp float64) float64 {
	var total float64 = 1
	if exp < 0 {
		fmt.Println("num: ", num, " neg exp: ", exp, " sending: ", exp*-1)
		return 1 / exponent(num, exp*-1)
	} else {
		for i := float64(0); i < exp; i++ {
			total = total * num
		}
		fmt.Println("num: ", num, " exp: ", exp, " total: ", total)
		return total
	}
}
*/
func factorial(num float64) float64 {
	var total float64 = 1
	for i := float64(1); i <= num; i++ {
		total = total * i
	}
	return total
}

func poisson(k, l float64) float64 {
	var e float64 = 2.71828
	return (math.Pow(l, k) * math.Pow(e, (l*-1))) / factorial(k)
}

func main() {
	// random var X follows Poisson distribution with mean of 2.5
	// Find probability which X == 5

	reader := bufio.NewReader(os.Stdin)
	stringIn, _ := reader.ReadString('\n')
	stringIn = strings.Trim(stringIn, "\r\n")
	l, err := strconv.ParseFloat(stringIn, 64)
	if err != nil {
		fmt.Println(err)
		return
	}
	stringIn, _ = reader.ReadString('\n')
	stringIn = strings.Trim(stringIn, "\r\n")
	k, err := strconv.ParseFloat(stringIn, 64)
	if err != nil {
		fmt.Println(err)
		return
	}

	x := poisson(k, l)
	fmt.Println(fmt.Sprintf("%.3f", x))
	// expected output: 0.067
}
