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

func factorial(num float64) float64 {
	var total float64 = 1
	for i := float64(1); i <= num; i++ {
		total = total * i
	}
	return total
}

func combination(total float64, choose float64) float64 {
	return factorial(total) / (factorial(choose) * factorial(total-choose))
}

func negBinomial(x float64, n float64, p float64) float64 {
	// b*(x,n,p) = (n-1 choose x-1) * p^x * p^(n-x)
	var q float64 = 1 - p
	return combination(n-1, x-1) * exponent(p, x) * exponent(q, n-x)
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

	var g float64
	//g := negBinomial(1, n, p)
	for i := float64(1); i <= n; i++ {
		g += negBinomial(1, i, p)
	}
	fmt.Println(fmt.Sprintf("%.3f", g))
	// expected answer: 0.868
}
