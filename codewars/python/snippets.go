package main

import (
	"fmt"
)

func BouncingBall(h, bounce, window float64) int {
	if (h <= 0) || (window >= h) || (bounce <= 0) || (bounce >= 1) {
		return -1 // your code
	}
	for j := 0; h > window; {
		j++
		h *= bounce
		if h > window {
			j++
		} else {
			return j
		}
	}
	return -1
}
package main

import "fmt"

func create2DArray(n int) [][]int {
    // Erstelle ein 2D-Array mit n Zeilen und n Spalten, gefüllt mit Nullen
    array := make([][]int, n)
    for i := range array {
        array[i] = make([]int, n)
    }
    return array
}

// https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/go
// Multiplication table


func MultiplicationTable(size int) [][]int {
	// Implement me! :)
}

func main() {
    n := 3 // Beispielwert für n
    result := create2DArray(n)
    
    // Ausgabe des erstellten 2D-Arrays
    for _, row := range result {
        fmt.Println(row)
    }
}

