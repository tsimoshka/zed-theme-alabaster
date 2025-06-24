// JavaScript sample for Alabaster theme
// Comments should be highlighted according to the theme

// Global constants
const MAX_SIZE = 1000;
const PI = 3.14159;
const DEBUG = true;
const NULL_VALUE = null;
const UNDEFINED_VALUE = undefined;

// Global function definition
function calculateArea(radius) {
  // Comment inside function
  if (radius <= 0) {
    return 0;
  }
  
  const area = PI * Math.pow(radius, 2);
  return area;
}

// Arrow function
const greet = (name) => {
  // Template literal string
  return `Hello, ${name}!`;
};

// Class definition
class Circle {
  constructor(radius) {
    // Instance properties with constants
    this.radius = radius;
    this.diameter = radius * 2;
  }
  
  // Method definition
  getCircumference() {
    // Regular string
    console.log("Calculating circumference...");
    return 2 * PI * this.radius;
  }
}

// Object literal with various value types
const config = {
  name: "Sample App",
  version: "1.0.0",
  port: 3000,
  isProduction: false,
  features: ["auth", "api", "ui"],
  regex: /[a-z]+/gi,
  symbol: Symbol("id")
};

// Various string types
const singleQuoted = 'Single quoted string';
const doubleQuoted = "Double quoted string";
const multiline = `This is a
multiline template
literal string`;

// Number constants
const integer = 42;
const float = 3.14;
const hex = 0xFF;
const binary = 0b1010;
const octal = 0o755;
const exponential = 1.5e10;

// Boolean constants
const isTrue = true;
const isFalse = false;

// Special values
const nothing = null;
const notDefined = undefined;
const notANumber = NaN;
const infinite = Infinity;

// Using async/await
async function fetchData() {
  try {
    // Simulating async operation
    const result = await Promise.resolve("data");
    return result;
  } catch (error) {
    console.error("Error:", error);
  }
}

// Array and object destructuring
const [first, second] = [1, 2];
const { name, version } = config;

// Control flow
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  } else {
    break;
  }
}

// Export statement
export { calculateArea, Circle, config };