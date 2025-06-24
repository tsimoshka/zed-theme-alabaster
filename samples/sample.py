# This is a comment that explains the purpose of this module
# According to Alabaster, comments should be highlighted

from typing import Optional, List, Dict, Union, Tuple, Any, Protocol
from abc import ABC, abstractmethod

# Global constant definitions with type annotations
MAX_SIZE: int = 1000
PI: float = 3.14159
DEBUG: bool = True
NONE_VALUE: None = None
DEFAULT_NAME: str = "Unnamed"

# Protocol definition (structural subtyping)
class Drawable(Protocol):
    """Protocol for drawable objects."""
    def draw(self) -> str: ...

# Abstract base class
class Shape(ABC):
    """Abstract base class for all shapes."""
    
    def __init__(self, name: str) -> None:
        self.name: str = name
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

# Global function definition with type annotations
def calculate_area(radius: float) -> float:
    """Calculate the area of a circle."""
    # Comments inside functions should also be highlighted
    if radius <= 0:
        return 0.0
    
    area: float = PI * radius ** 2
    return area

# Class with inheritance and type annotations
class Circle(Shape):
    """A Circle class that inherits from Shape."""
    
    def __init__(self, radius: float, name: str = "Circle") -> None:
        # Call parent constructor
        super().__init__(name)
        # Instance attributes with type annotations
        self.radius: float = radius
        self.diameter: float = radius * 2.0
    
    def area(self) -> float:
        """Calculate circle area."""
        return PI * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle perimeter (circumference)."""
        return 2 * PI * self.radius
    
    def get_info(self) -> Dict[str, Union[str, float]]:
        # String literals should be highlighted
        print("Getting circle information...")
        return {
            "name": self.name,
            "radius": self.radius,
            "area": self.area(),
            "perimeter": self.perimeter()
        }

# Another derived class
class Rectangle(Shape):
    """A Rectangle class that inherits from Shape."""
    
    def __init__(self, width: float, height: float, name: str = "Rectangle") -> None:
        super().__init__(name)
        self.width: float = width
        self.height: float = height
    
    def area(self) -> float:
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

# Generic function with type variables
def get_shapes_info(shapes: List[Shape]) -> List[Dict[str, Any]]:
    """Get information about multiple shapes."""
    result: List[Dict[str, Any]] = []
    for shape in shapes:
        info: Dict[str, Any] = {
            "type": type(shape).__name__,
            "name": shape.name,
            "area": shape.area(),
            "perimeter": shape.perimeter()
        }
        result.append(info)
    return result

# Function with optional and default parameters
def create_shape(shape_type: str, 
                dimensions: Tuple[float, ...],
                name: Optional[str] = None) -> Optional[Shape]:
    """Factory function to create shapes."""
    if shape_type == "circle" and len(dimensions) == 1:
        return Circle(dimensions[0], name or "Circle")
    elif shape_type == "rectangle" and len(dimensions) == 2:
        return Rectangle(dimensions[0], dimensions[1], name or "Rectangle")
    return None

# Using the defined elements
if __name__ == "__main__":
    # Various string types with annotations
    single_quoted: str = 'Hello, World!'
    double_quoted: str = "Python sample for Alabaster theme"
    multiline: str = """This is a
    multiline string
    for testing"""
    
    # Numbers and boolean constants with annotations
    integer_num: int = 42
    float_num: float = 3.14
    hex_num: int = 0xFF
    binary_num: int = 0b1010
    is_valid: bool = True
    is_empty: bool = False
    
    # Complex type annotations
    numbers: List[int] = [1, 2, 3, 4, 5]
    mapping: Dict[str, float] = {"pi": 3.14, "e": 2.718}
    mixed: Tuple[int, str, bool] = (42, "answer", True)
    
    # Creating objects with type annotations
    shapes: List[Shape] = [
        Circle(5.0, "Small Circle"),
        Rectangle(10.0, 20.0, "Large Rectangle"),
        Circle(15.0, "Big Circle")
    ]
    
    # Using polymorphism
    for shape in shapes:
        area: float = shape.area()
        perimeter: float = shape.perimeter()
        print(f"{shape.name}: area={area}, perimeter={perimeter}")
    
    # Optional types
    maybe_shape: Optional[Shape] = create_shape("circle", (10.0,))
    nothing: Optional[Shape] = None
    
    # Union types
    value: Union[int, str] = 42
    value = "forty-two"
    
    # Any type
    anything: Any = 123
    anything = "string"
    anything = [1, 2, 3]