package main

// programs start running in package `main`

import (
	"fmt"
	"math"
	"math/cmplx"
	"math/rand"
	"time"
)

// functions
// `x, y int` : when two or more consecutive named parameters share a type,
// omit the type from all but the last
func add(x, y int) int {
	return x + y
}

func sub(x int, y int) int {
	return x - y
}

// multiple results
func swap(x, y string) (string, string) {
	return y, x
}

func printTypeValue[T any](v T) {
	fmt.Printf("type: %T , value: %v\n", v, v)
}

// variables
var (
	// variables
	i int
	s string
	c bool
	f float64
	// variables with initializers
	z1 bool      = false
	z2 uint64    = 1<<64 - 1
	z3 complex64 = complex64(cmplx.Sqrt(-5 + 12i))
)

const (
	Pi             = 3.14
	StatusOK       = "200"
	StatusNotFound = "404"
	StatusError    = "500"
	Big            = 1 << 100
	Small          = Big >> 99
)

func printConst() {
	printTypeValue(Pi)
	printTypeValue(StatusOK)
	printTypeValue(StatusError)
	printTypeValue(StatusNotFound)
	printTypeValue(Big * 0.1)
	printTypeValue(Small)
}

func printBasicTypes() {
	var (
		// basic types
		// variables declared without an explicit initial value are given their __zero__ value.
		// `0` for numeric types
		// `false` for the boolean type and
		// ""(the empty string) for strings
		v1  bool
		v2  string
		v3  int
		v4  int8
		v5  int16
		v6  int32
		v7  int64
		v8  uint
		v9  uint8
		v10 uint16
		v11 uint32
		v12 uint64
		v13 uintptr
		v14 byte
		v15 rune
		v16 float32
		v17 float64
		v18 complex64
		v19 complex128
	)
	printTypeValue(v1)
	printTypeValue(v2)
	printTypeValue(v3)
	printTypeValue(v4)
	printTypeValue(v5)
	printTypeValue(v6)
	printTypeValue(v7)
	printTypeValue(v8)
	printTypeValue(v9)
	printTypeValue(v10)
	printTypeValue(v11)
	printTypeValue(v12)
	printTypeValue(v13)
	printTypeValue(v14)
	printTypeValue(v15)
	printTypeValue(v16)
	printTypeValue(v17)
	printTypeValue(v18)
	printTypeValue(v19)
}

func forStatement() {
	sum := 0
	// basic `for` loop has three separated by semicolons:
	//   the init statement(optional): executed before first iteration
	//   the condition expression: evaluated before every iteration
	//   the post statement(optional): executed at the end of every iteration
	for i := 0; i < 10; i++ {
		sum += i
	}
	printTypeValue(sum)

	sum = 1
	// same as `while` statement in other languages
	for sum < 1000 {
		sum += sum
	}
	printTypeValue(sum)
	if sum > 1024 {
		fmt.Println("More than 1024")
	} else {
		fmt.Println("Equal or less than 1024")
	}

	sum = 3
	for {
		sum += sum
		if sum > 1000 {
			break
		}
	}
	printTypeValue(sum)

	if sum > 1024 {
		fmt.Println("More than 1024")
	} else {
		fmt.Println("Equal or less than 1024")
	}
}

func main() {
	fmt.Println("Hello World!")
	fmt.Println("The time is", time.Now())
	// `math.Pi` is an exported name with a capital letter
	fmt.Println(math.Pi)
	fmt.Println()

	fmt.Println("My favorite number is ", rand.Intn(100))
	fmt.Println()

	fmt.Printf("Now you have %g problems.\n", math.Sqrt(4))
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
	fmt.Printf("Now you have %G problems.\n", math.Sqrt(9))
	fmt.Printf("Now you have %G problems.\n", math.Sqrt(10))
	fmt.Println()

	// type conversions
	fmt.Printf("%g + %g = %g\n", float32(43), float32(23), float32(add(43, 23)))

	fmt.Printf("%d + %d = %d\n", 43, 23, add(43, 23))
	fmt.Printf("%d - %d = %d\n", 43, 23, sub(43, 23))
	fmt.Println()

	var a1, a2 = "hello", "world"
	fmt.Println(a1, a2)
	fmt.Println(swap(a1, a2))
	a1, a2 = swap(a1, a2)
	fmt.Println(a1, a2)
	fmt.Println()

	// short vairable declarations
	k := 34
	fmt.Printf("%v, %v, %v, %v, %v\n", i, s, c, f, k)
	fmt.Printf("%d, %q, %t, %g, %b\n", i, s, c, f, k)
	fmt.Println()

	fmt.Printf("Type: %T Value: %v\n", z1, z1)
	fmt.Printf("Type: %T Value: %v\n", z2, z2)
	fmt.Printf("Type: %T Value: %v\n", z3, z3)
	fmt.Println()

	// type inference
	k1 := -33
	k2 := 33.3
	k3 := 0.333 + 0.4i
	printTypeValue(k1)
	printTypeValue(k2)
	printTypeValue(k3)
	fmt.Println()

	printBasicTypes()
	fmt.Println()

	printConst()

	fmt.Println()
	forStatement()

}
