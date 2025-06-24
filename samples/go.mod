// Module declaration comment
module github.com/user/alabaster-test

// Go version requirement
go 1.21

// Dependencies section
require (
	// Direct dependencies with version strings
	github.com/gorilla/mux v1.8.0
	github.com/stretchr/testify v1.8.4
	golang.org/x/tools v0.14.0
)

// Indirect dependencies
require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

// Replace directives
replace (
	// Local replacement
	github.com/old/package => ./local/package
	// Version replacement
	github.com/broken/lib v1.0.0 => github.com/fixed/lib v1.0.1
)

// Exclude specific versions
exclude (
	github.com/bad/package v0.1.0
	github.com/bad/package v0.2.0
)