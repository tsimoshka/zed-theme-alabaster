// Rust sample for Alabaster theme
// Comments should be highlighted

// Import statements
use std::collections::HashMap;
use std::io::{self, Write};

// Global constants
const MAX_SIZE: usize = 1000;
const PI: f64 = 3.14159;
const DEBUG: bool = true;

// Static variable
static COUNTER: std::sync::atomic::AtomicUsize = std::sync::atomic::AtomicUsize::new(0);

// Type alias
type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// Struct definition
#[derive(Debug, Clone)]
struct Circle {
    radius: f64,
    name: String,
}

// Enum definition
enum Status {
    Active,
    Inactive,
    Pending(String),
    Error { code: i32, message: String },
}

// Trait definition
trait Shape {
    fn area(&self) -> f64;
    fn perimeter(&self) -> f64;
}

// Implementation block
impl Circle {
    // Associated function (constructor)
    fn new(radius: f64, name: String) -> Self {
        Circle { radius, name }
    }
    
    // Method
    fn diameter(&self) -> f64 {
        self.radius * 2.0
    }
}

// Trait implementation
impl Shape for Circle {
    fn area(&self) -> f64 {
        // Using constant in calculation
        PI * self.radius.powi(2)
    }
    
    fn perimeter(&self) -> f64 {
        2.0 * PI * self.radius
    }
}

// Generic function
fn identity<T>(value: T) -> T {
    value
}

// Function with lifetime parameters
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

// Main function
fn main() -> Result<()> {
    // String literals
    let single_quoted = 'A'; // Character literal
    let double_quoted = "Hello, World!";
    let raw_string = r#"This is a "raw" string"#;
    let byte_string = b"byte string";
    
    // Numeric literals
    let integer = 42;
    let float = 3.14;
    let hex = 0xFF;
    let binary = 0b1010;
    let octal = 0o755;
    
    // Boolean literals
    let is_true = true;
    let is_false = false;
    
    // Creating instances
    let circle = Circle::new(5.0, String::from("My Circle"));
    
    // Using traits
    println!("Area: {}", circle.area());
    
    // Pattern matching
    let status = Status::Active;
    match status {
        Status::Active => println!("Active"),
        Status::Inactive => println!("Inactive"),
        Status::Pending(msg) => println!("Pending: {}", msg),
        Status::Error { code, message } => println!("Error {}: {}", code, message),
    }
    
    // Closures
    let add = |a: i32, b: i32| -> i32 { a + b };
    let result = add(10, 20);
    
    // Vector and array literals
    let vec = vec![1, 2, 3, 4, 5];
    let array = [1, 2, 3, 4, 5];
    
    // Option and Result types
    let some_value: Option<i32> = Some(42);
    let none_value: Option<i32> = None;
    
    // Error handling
    let file_result: Result<String> = Ok("Success".to_string());
    
    // Loops and control flow
    for i in 0..10 {
        if i % 2 == 0 {
            continue;
        } else if i > 5 {
            break;
        }
    }
    
    // Macro usage
    println!("Debug: {:?}", circle);
    eprintln!("Error message");
    
    Ok(())
}

// Unit tests
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_circle_area() {
        let circle = Circle::new(1.0, "Test".to_string());
        assert_eq!(circle.area(), PI);
    }
}