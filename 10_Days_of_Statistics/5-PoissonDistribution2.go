package main

// The manager of a industrial plant is planning to buy a machine of either type  or type . For each day’s operation:
// The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is CostA = 160 + 40X^2.
// The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is CostB = 128 + 40Y^2.
// Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func exponent(num float64, exp float64) float64 {
	var total float64 = 1
	for i := float64(0); i < exp; i++ {
		total = total * num
	}
	return total
}

func getCostA(a float64) float64 {
	return 160 + 40*(a+exponent(a, 2))
}

func getCostB(b float64) float64 {
	return 128 + 40*(b+exponent(b, 2))
}

func main() {
	// Input format:
	// A single line comprised of  space-separated values denoting the respective means for A and B

	// Output format:
	// There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):
	// On the first line, print the expected daily cost of machine .
	// On the second line, print the expected daily cost of machine .

	// P(x) = (lambda^x * e^-lambda) / x!
	// E(X) = lambda + lambda^2
	reader := bufio.NewReader(os.Stdin)
	stringIn, _ := reader.ReadString('\n')
	stringIn = strings.Trim(stringIn, "\r\n")
	stringList := strings.Split(stringIn, " ")
	var probabilityList []float64
	for _, val := range stringList {
		floatVal, err := strconv.ParseFloat(val, 64)
		if err != nil {
			fmt.Println(err)
			return
		}
		probabilityList = append(probabilityList, floatVal)
	}
	a := probabilityList[0]
	b := probabilityList[1]

	fmt.Println(fmt.Sprintf("%.3f", getCostA(a)))
	fmt.Println(fmt.Sprintf("%.3f", getCostB(b)))
}
