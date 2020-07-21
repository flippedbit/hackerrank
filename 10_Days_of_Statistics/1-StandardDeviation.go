package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func mean(numList []float64) float64 {
	var sum float64
	for i := 0; i < len(numList); i++ {
		sum += numList[i]
	}
	return sum / float64(len(numList))
}

func squared(num float64) float64 {
	return num * num
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	size, err := reader.ReadString('\n')
	size = strings.Trim(size, "\r\n")
	n, err := strconv.ParseFloat(size, 64)
	if err != nil {
		fmt.Println(err)
		return
	}

	numArray, _ := reader.ReadString('\n')
	numArray = strings.Trim(numArray, "\r\n")
	numList := strings.Split(numArray, " ")
	var values []float64
	for _, val := range numList {
		floatVal, err := strconv.ParseFloat(val, 64)
		if err != nil {
			fmt.Println(err)
			return
		}
		values = append(values, floatVal)
	}

	mu := mean(values)
	var sum float64
	for _, val := range values {
		sum += squared(val - mu)
	}
	s2 := sum / n
	s := math.Sqrt(s2)
	ss := fmt.Sprintf("%.1f", s)
	fmt.Println(ss)
}
