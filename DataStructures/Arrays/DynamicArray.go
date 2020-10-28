package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

func dynamicArray(n int32, queries [][]int32) []int32 {
	// Write your code here
	seqList := make([][]int32, n)
	var lastAnswer int32 = 0
	var results []int32

	for _, q := range queries {
		x := q[1]
		y := q[2]
		//fmt.Println(q)
		if q[0] == 2 {
			seq := (x ^ lastAnswer) % n
			e := y % int32(len(seqList[seq]))
			lastAnswer = seqList[seq][e]
			results = append(results, lastAnswer)
			//fmt.Println(lastAnswer)
		} else {
			seq := (x ^ lastAnswer) % n
			seqList[seq] = append(seqList[seq], y)
		}
		//fmt.Println(seqList, lastAnswer)
	}
	//fmt.Println(seqList)
	return results
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)
	/*
	   stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	   checkError(err)

	   defer stdout.Close()

	   writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)
	*/
	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	qTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	q := int32(qTemp)

	var queries [][]int32
	for i := 0; i < int(q); i++ {
		queriesRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var queriesRow []int32
		for _, queriesRowItem := range queriesRowTemp {
			queriesItemTemp, err := strconv.ParseInt(queriesRowItem, 10, 64)
			checkError(err)
			queriesItem := int32(queriesItemTemp)
			queriesRow = append(queriesRow, queriesItem)
		}

		if len(queriesRow) != 3 {
			panic("Bad input")
		}

		queries = append(queries, queriesRow)
	}

	result := dynamicArray(n, queries)
	fmt.Println(result)
	/*
		    for i, resultItem := range result {
		        fmt.Fprintf(writer, "%d", resultItem)

		        if i != len(result) - 1 {
		            fmt.Fprintf(writer, "\n")
		        }
		    }

		    fmt.Fprintf(writer, "\n")

			writer.Flush()
	*/
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
