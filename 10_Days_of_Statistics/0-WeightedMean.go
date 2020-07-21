package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	_, err := reader.ReadString('\n')
	//size = strings.Trim(size, "\r\n")
	//_, err := strconv.Atoi(size)
	if err != nil {
		fmt.Println(err)
		return
	}

	xArray, _ := reader.ReadString('\n')
	xArray = strings.Trim(xArray, "\r\n")
	xList := strings.Split(xArray, " ")

	wArray, _ := reader.ReadString('\n')
	wArray = strings.Trim(wArray, "\r\n")
	wList := strings.Split(wArray, " ")

	var values []int
	for _, val := range xList {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		values = append(values, intVal)
	}

	var weights []int
	for _, val := range wList {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		weights = append(weights, intVal)
	}

	//fmt.Println(values)
	//fmt.Println(weights)

	weightedValues := 0
	for i, value := range values {
		weightedValues += value * weights[i]
	}

	sumWeights := 0
	for _, weight := range weights {
		sumWeights += weight
	}

	weightedMean := float32(weightedValues) / float32(sumWeights)
	w := fmt.Sprintf("%.1f", weightedMean)
	fmt.Println(w)
}
