package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func median(list []int) int {
	if len(list)%2 == 0 {
		return (list[len(list)/2] + list[(len(list)/2)-1]) / 2
	}
	return list[len(list)/2]
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	size, err := reader.ReadString('\n')
	size = strings.Trim(size, "\r\n")
	length, err := strconv.Atoi(size)
	if err != nil {
		fmt.Println(err)
		return
	}

	numArray, _ := reader.ReadString('\n')
	numArray = strings.Trim(numArray, "\r\n")
	numList := strings.Split(numArray, " ")
	var values []int
	for _, val := range numList {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		values = append(values, intVal)
	}

	for x := 1; x < length; x++ {
		for y := 0; y < length-1; y++ {
			if values[y] > values[y+1] {
				tmp := values[y]
				values[y] = values[y+1]
				values[y+1] = tmp
			}
		}
	}

	var q1 int
	q2 := median(values)
	var q3 int

	if length%2 == 0 {
		q1 = median(values[:len(values)/2])
		q3 = median(values[len(values)/2:])
	} else {
		var first []int
		var second []int
		half := length / 2
		for i, val := range values {
			if i == half {
				continue
			} else if i < half {
				first = append(first, val)
			} else {
				second = append(second, val)
			}
		}

		q1 = median(first)
		q3 = median(second)
	}

	fmt.Println(q1)
	fmt.Println(q2)
	fmt.Println(q3)
}
