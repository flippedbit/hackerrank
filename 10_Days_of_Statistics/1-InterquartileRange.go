package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func median(list []int) float32 {
	if len(list)%2 == 0 {
		return (float32(list[len(list)/2]) + float32(list[(len(list)/2)-1])) / 2
	}
	return float32(list[len(list)/2])
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	_, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		return
	}

	xArray, _ := reader.ReadString('\n')
	xArray = strings.Trim(xArray, "\r\n")
	xList := strings.Split(xArray, " ")

	fArray, _ := reader.ReadString('\n')
	fArray = strings.Trim(fArray, "\r\n")
	fList := strings.Split(fArray, " ")

	var x []int
	for _, val := range xList {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		x = append(x, intVal)
	}

	var f []int
	for _, val := range fList {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		f = append(f, intVal)
	}

	var s []int
	for i, xi := range x {
		for fi := 0; fi < f[i]; fi++ {
			s = append(s, xi)
		}
	}

	for i := 1; i < len(s); i++ {
		for y := 0; y < len(s)-1; y++ {
			if s[y] > s[y+1] {
				tmp := s[y]
				s[y] = s[y+1]
				s[y+1] = tmp
			}
		}
	}

	var q1 float32
	var q3 float32

	if len(s)%2 == 0 {
		q1 = median(s[:len(s)/2])
		q3 = median(s[len(s)/2:])
	} else {
		var first []int
		var second []int
		half := len(s) / 2
		for i, val := range s {
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
	qRange := q3 - q1
	qr := fmt.Sprintf("%.1f", qRange)
	fmt.Println(qr)
}
