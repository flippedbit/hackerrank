package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func factorial(num float64) float64 {
	var total float64 = 1
	for i := float64(1); i <= num; i++ {
		total = total * i
	}
	return total
}

func exponent(num float64, exp float64) float64 {
	var total float64 = 1
	for i := float64(0); i < exp; i++ {
		total = total * num
	}
	return total
}

func combination(total float64, choose float64) float64 {
	return factorial(total) / (factorial(choose) * factorial(total-choose))
}

func binomial(total float64, probability float64, choosen float64) float64 {
	return combination(total, choosen) * exponent(probability, choosen) * exponent(1-probability, total-choosen)
}

func main() {
	// a manufactor of metal pistons finds that, on avg, 12% of pistons are rejected.
	// what is the probability that a batch of 10 will contain
	// 1. no more than 2 rejects?
	// 2. at least 2 rejects?

	reader := bufio.NewReader(os.Stdin)

	numIn, _ := reader.ReadString('\n')
	numIn = strings.Trim(numIn, "\r\n")
	numList := strings.Split(numIn, " ")
	var values []float64
	for _, val := range numList {
		floatVal, err := strconv.ParseFloat(val, 64)
		if err != nil {
			fmt.Println(err)
			return
		}
		values = append(values, floatVal)
	}

	total := values[1]                              // 10
	rejectedProbability := values[0] / float64(100) // 12% or 0.12
	var numRejected float64 = 2

	var totalProbability float64
	for i := float64(0); i <= numRejected; i++ {
		totalProbability += binomial(total, rejectedProbability, i)
	}
	fmt.Println(fmt.Sprintf("%.3f", totalProbability))

	totalProbability = 0
	for i := numRejected; i <= total; i++ {
		totalProbability += binomial(total, rejectedProbability, i)
	}

	fmt.Println(fmt.Sprintf("%.3f", totalProbability))
}
