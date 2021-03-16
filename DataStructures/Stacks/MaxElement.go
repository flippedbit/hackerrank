package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func pop(a *[]int) {
	s := *a
	//fmt.Println("pop:", *a, (*a)[len(s)-1])
	s = s[:len(s)-1]
	*a = s
}

func push(a *[]int, i int) {
	//fmt.Println("push: ", i, *a)
	*a = append(*a, i)
}

func max(a []int) int {
	var max int
	for _, i := range a {
		if max < i {
			max = i
		}
	}
	return max
}

/*
func readLine(r *bufio.Reader) string {
	s, err := r.ReadString('\n')
	if err == io.EOF {
		return ""
	} else if err != nil {
		panic(err)
	}
	return strings.Trim(s, "\n")
}
*/
func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func parseQuery(s []string) []int {
	var i []int
	for _, q := range s {
		if q != "" {
			v, e := strconv.Atoi(q)
			if e != nil {
				panic(e)
			}
			i = append(i, v)
		}
	}
	return i
}

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	reader := bufio.NewReader(os.Stdin)
	qCnt, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	var stack []int
	var results []int
	for i := 0; i < int(qCnt); i++ {
		q := strings.Split(readLine(reader), " ")
		queries := parseQuery(q)
		//fmt.Println(queries)
		if len(queries) > 0 {
			if queries[0] == 1 {
				push(&stack, queries[1])
			} else if queries[0] == 2 {
				pop(&stack)
			} else if queries[0] == 3 {
				results = append(results, max(stack))
			} else {
				results = append(results, max(stack))
			}
		}
	}
	//fmt.Println(stack)
	for _, a := range results {
		fmt.Println(a)
	}
}
