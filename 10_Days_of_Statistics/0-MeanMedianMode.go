package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func mean(numList []int) float32 {
	var sum float32
	for i := 0; i < len(numList); i++ {
		sum += float32(numList[i])
	}
	return sum / float32(len(numList))
}

func mode(numList []int) int {
	m := make(map[int]int)
	for _, val := range numList {
		m[val]++
	}
	for i := 1; i < len(numList); i++ {
		for a := 0; a < len(numList)-1; a++ {
			if numList[a] > numList[a+1] {
				tmp := numList[a]
				numList[a] = numList[a+1]
				numList[a+1] = tmp
			}
		}
	}
	most := 0
	var mode int
	for _, val := range numList {
		if m[val] > most {
			most = m[val]
			mode = val
		}
	}
	return mode
}

func median(numList []int) float32 {
	//sort.Ints(numList)
	length := len(numList)
	half := (length / 2) - 1
	for i := 1; i < length; i++ {
		for a := 0; a < length-1; a++ {
			if numList[a] > numList[a+1] {
				tmp := numList[a]
				numList[a] = numList[a+1]
				numList[a+1] = tmp
			}
		}
	}
	if length%2 == 0 {
		return (float32(numList[half]) + float32(numList[half+1])) / 2
	}
	return float32(numList[half+1])
}

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	//numList := []int{64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060}
	reader := bufio.NewReader(os.Stdin)
	size, _ := reader.ReadString('\n')
	size = strings.Trim(size, "\r\n")
	s, err := strconv.Atoi(size)
	if err != nil {
		fmt.Println(err)
		return
	}
	array, _ := reader.ReadString('\n')
	//array := "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
	array = strings.Trim(array, "\r\n")
	list := strings.Split(array, " ")
	numList := []int{}
	for _, val := range list {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		numList = append(numList, intVal)
	}
	if s == len(numList) {
		mean := fmt.Sprintf("%.1f", mean(numList))
		median := fmt.Sprintf("%.1f", median(numList))
		mode := fmt.Sprintf("%d", mode(numList))
		fmt.Println(mean)
		fmt.Println(median)
		fmt.Println(mode)
	}
}
