// Package main demonstrates Alabaster theme highlighting for Go
package main

import (
	"fmt"
	"math"
)

// Global constants should be highlighted
const (
	MaxRetries = 3
	Pi         = 3.14159
	Debug      = true
)

// Global variable definitions
var (
	counter  = 0
	version  = "1.0.0"
	isActive = false
)

// User represents a simple user structure
type User struct {
	Name    string
	Age     int
	IsAdmin bool
}

// Global function definition
func calculateArea(radius float64) float64 {
	// Comments explain the logic
	if radius <= 0 {
		return 0.0
	}
	
	// Using constants in calculations
	return Pi * math.Pow(radius, 2)
}

// Method on User type
func (u User) Greet() string {
	// String literals should be highlighted
	return fmt.Sprintf("Hello, my name is %s", u.Name)
}

func main() {
	// Various string types
	singleQuoted := `Raw string literal`
	doubleQuoted := "Regular string"
	formatted := fmt.Sprintf("Formatted: %d", 42)
	
	// Numeric constants
	integer := 42
	floating := 3.14
	hex := 0xFF
	binary := 0b1010
	
	// Boolean constants
	isTrue := true
	isFalse := false
	
	// Nil is a constant
	var nothing interface{} = nil
	
	// Creating instances
	user := User{
		Name:    "Alice",
		Age:     30,
		IsAdmin: true,
	}
	
	// Control flow
	for i := 0; i < MaxRetries; i++ {
		if i%2 == 0 {
			continue
		} else {
			break
		}
	}
	
	// Using functions
	area := calculateArea(5.0)
	greeting := user.Greet()
	
	// Print results
	fmt.Println(area, greeting, nothing)
}