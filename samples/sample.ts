// TypeScript sample for Alabaster theme
// Demonstrates TypeScript-specific syntax highlighting

// Global constants with type annotations
const MAX_ITEMS: number = 100;
const API_KEY: string = "secret-key-123";
const IS_DEV: boolean = true;
const NOTHING: null = null;

// Type alias definition
type UserRole = "admin" | "user" | "guest";

// Interface definition
interface User {
  id: number;
  name: string;
  email: string;
  role: UserRole;
  isActive: boolean;
}

// Enum definition
enum Status {
  Pending = "PENDING",
  Active = "ACTIVE",
  Inactive = "INACTIVE"
}

// Generic type definition
type Result<T> = {
  data: T;
  error: string | null;
  timestamp: number;
};

// Global function with typed parameters
function processUser(user: User): Result<User> {
  // Comment explaining logic
  if (!user.isActive) {
    return {
      data: user,
      error: "User is not active",
      timestamp: Date.now()
    };
  }
  
  // Process active user
  return {
    data: user,
    error: null,
    timestamp: Date.now()
  };
}

// Generic function
function identity<T>(value: T): T {
  // Simple generic function
  return value;
}

// Class with TypeScript features
class UserService {
  private users: User[] = [];
  public readonly version = "1.0.0";
  
  constructor(private apiKey: string) {
    // Constructor with parameter property
  }
  
  // Method with promise return type
  async getUser(id: number): Promise<User | undefined> {
    // Async method implementation
    return this.users.find(u => u.id === id);
  }
  
  // Static method
  static validateEmail(email: string): boolean {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
}

// Decorator (commented as it needs experimental decorators)
// @deprecated
// function logMethod(target: any, key: string, descriptor: PropertyDescriptor) {
//   console.log(`Method ${key} was called`);
// }

// Union and intersection types
type StringOrNumber = string | number;
type HasName = { name: string };
type HasAge = { age: number };
type Person = HasName & HasAge;

// Literal types
const direction: "north" | "south" | "east" | "west" = "north";
const statusCode: 200 | 404 | 500 = 200;

// Tuple type
const coordinate: [number, number, number] = [10, 20, 30];

// Type assertions
const someValue: unknown = "this is a string";
const strLength: number = (someValue as string).length;

// Optional chaining and nullish coalescing
const user: User | null = null;
const userName = user?.name ?? "Anonymous";

// Const assertion
const CONFIG = {
  api: "https://api.example.com",
  timeout: 5000
} as const;

// Template literal types
type Greeting<T extends string> = `Hello, ${T}!`;
type WelcomeMessage = Greeting<"World">;

// Conditional types
type IsString<T> = T extends string ? true : false;
type Test1 = IsString<string>;  // true
type Test2 = IsString<number>;  // false

// Export types and values
export { User, UserRole, Status, UserService };
export type { Result };