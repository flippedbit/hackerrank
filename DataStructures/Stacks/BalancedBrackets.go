package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func push(s *[]rune, r rune) {
	*s = append(*s, r)
}

func pop(s *[]rune) {
	*s = (*s)[:len((*s))-1]
}

func check(s []rune, r rune) bool {
	if len(s) > 0 {
		e := s[len(s)-1]
		if e == '[' && r == ']' {
			return true
		} else if e == '{' && r == '}' {
			return true
		} else if e == '(' && r == ')' {
			return true
		} else {
			return false
		}
	} else {
		return false
	}
}

// Complete the isBalanced function below.
func isBalanced(s string) string {
	if len(s)%2 != 0 {
		return "NO"
	}
	var stack []rune
	var e bool
	for _, r := range s {
		if r == '[' || r == '{' || r == '(' {
			push(&stack, r)
		} else if r == ']' || r == '}' || r == ')' {
			e = true
			if check(stack, r) == false {
				return "NO"
			} else {
				pop(&stack)
			}
		} else {
			continue
		}
	}
	if e && len(stack) == 0 {
		return "YES"
	} else {
		return "NO"
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)
	/*
		stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
		checkError(err)

		defer stdout.Close()

		writer := bufio.NewWriterSize(stdout, 1024*1024)
	*/
	writer := bufio.NewWriterSize(os.Stdout, 1024*1024)

	tTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	t := int32(tTemp)

	for tItr := 0; tItr < int(t); tItr++ {
		s := readLine(reader)

		result := isBalanced(s)

		fmt.Fprintf(writer, "%s\n", result)
	}

	writer.Flush()
}

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
