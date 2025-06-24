#!/bin/bash
# Bash sample for Alabaster theme
# Comments should be highlighted according to the theme

# Global constants
readonly MAX_RETRIES=3
readonly VERSION="1.0.0"
readonly DEBUG=true
readonly NULL_VALUE=""

# Global variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURRENT_DATE=$(date +"%Y-%m-%d")
COUNTER=0

# Function definitions
calculate_sum() {
    # Function comment
    local num1=$1
    local num2=$2
    
    # Arithmetic operation
    local result=$((num1 + num2))
    echo "$result"
}

# Function with string manipulation
process_string() {
    local input="$1"
    
    # Various string operations
    echo "Length: ${#input}"
    echo "Uppercase: ${input^^}"
    echo "Lowercase: ${input,,}"
    echo "Substring: ${input:0:5}"
    echo "Replace: ${input/old/new}"
}

# Main script logic
main() {
    # String variables with different quotes
    local single_quoted='Single quoted string'
    local double_quoted="Double quoted string with $VERSION"
    local command_sub="Today is $(date)"
    local backtick_sub="Current dir: `pwd`"
    
    # Numeric constants
    local integer=42
    local negative=-17
    local hex=0xFF
    local octal=0755
    
    # Boolean-like values (bash doesn't have true booleans)
    local is_true=1
    local is_false=0
    
    # Arrays
    local fruits=("apple" "banana" "cherry")
    local numbers=(1 2 3 4 5)
    
    # Associative array (requires bash 4+)
    declare -A colors
    colors["red"]="#FF0000"
    colors["green"]="#00FF00"
    colors["blue"]="#0000FF"
    
    # Here document
    cat <<EOF
This is a here document.
It can contain multiple lines.
Variables like $VERSION are expanded.
EOF
    
    # Here document with literal text
    cat <<'LITERAL'
This is a literal here document.
Variables like $VERSION are NOT expanded.
Special characters like $ and \ are preserved.
LITERAL
    
    # Conditional statements
    if [[ $DEBUG == true ]]; then
        echo "Debug mode is enabled"
    elif [[ $COUNTER -gt 10 ]]; then
        echo "Counter is greater than 10"
    else
        echo "Normal mode"
    fi
    
    # Case statement
    case "$1" in
        start)
            echo "Starting service..."
            ;;
        stop)
            echo "Stopping service..."
            ;;
        restart|reload)
            echo "Restarting service..."
            ;;
        *)
            echo "Usage: $0 {start|stop|restart|reload}"
            exit 1
            ;;
    esac
    
    # Loops
    for fruit in "${fruits[@]}"; do
        echo "Fruit: $fruit"
    done
    
    for ((i=0; i<5; i++)); do
        echo "Number: $i"
    done
    
    while [[ $COUNTER -lt $MAX_RETRIES ]]; do
        echo "Attempt $((COUNTER + 1)) of $MAX_RETRIES"
        ((COUNTER++))
    done
    
    # Command substitution and pipes
    local file_count=$(ls -1 | wc -l)
    local current_user=$(whoami)
    
    # File operations
    if [[ -f "/etc/passwd" ]]; then
        echo "File exists"
    fi
    
    if [[ -d "$HOME" ]]; then
        echo "Directory exists"
    fi
    
    # String comparisons
    if [[ "$single_quoted" == "$double_quoted" ]]; then
        echo "Strings are equal"
    fi
    
    if [[ -z "$NULL_VALUE" ]]; then
        echo "String is empty"
    fi
    
    # Numeric comparisons
    if ((integer > 40)); then
        echo "Integer is greater than 40"
    fi
    
    # Regular expressions
    if [[ "$double_quoted" =~ ^Double.*string$ ]]; then
        echo "Pattern matches"
    fi
    
    # Process substitution
    diff <(echo "line1") <(echo "line2")
    
    # Redirection
    echo "Standard output" > output.txt
    echo "Append to file" >> output.txt
    echo "Standard error" 2> error.txt
    echo "Both outputs" &> combined.txt
    
    # Background jobs
    sleep 5 &
    local bg_pid=$!
    
    # Trap signals
    trap 'echo "Cleaning up..."; exit' INT TERM
    
    # Export variables
    export PATH="$PATH:/usr/local/bin"
    export CUSTOM_VAR="custom value"
    
    # Source other scripts
    # source ./config.sh
    # . ./another_script.sh
    
    # Exit codes
    return 0
}

# Special variables
echo "Script name: $0"
echo "First argument: $1"
echo "All arguments: $@"
echo "Number of arguments: $#"
echo "Last exit code: $?"
echo "Current PID: $$"
echo "Last background PID: $!"

# Call main function with all arguments
main "$@"