package main

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

func main() {
	// probability that a machine produces a defective product is 1/3.
	// what is the probability that the first defect is found during
	// the fifth inspection?

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
	stringIn, _ = reader.ReadString('\n')
	stringIn = strings.Trim(stringIn, "\r\n")
	n, err := strconv.ParseFloat(stringIn, 64)
	if err != nil {
		fmt.Println(err)
		return
	}

	p := probabilityList[0] / probabilityList[1]
	q := 1 - p

	// g(n,p) = q^(n-1) * p
	g := exponent(q, n-1) * p
	fmt.Println(fmt.Sprintf("%.3f", g))
}
