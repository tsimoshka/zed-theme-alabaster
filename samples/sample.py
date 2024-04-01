# imports
import math
import re
from datetime import datetime
from typing import Any, Callable, Dict, List

# constants
PI: float = 3.1416

# Regular expressions with escape symbols
pattern: str = r"\d+"  # Matches all decimal digits

# decorator with arguments
def decorator_name(arg1: str, arg2: str) -> Callable[[Any], Any]:
    """
    This is a decorator function with arguments
    """
    def real_decorator(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
        def wrapper(*args: Any, **kwargs: Any) -> None:
            print(f"Decorated with \"{arg1}\", {arg2}")
            function(*args, **kwargs)
        return wrapper
    return real_decorator

# warning
print

# class definition
class SampleClass:
    """
    This is a simple sample class
    """
    class_variable: str = "I'm a class var"

    def __init__(self, instance_var: str) -> None:
        self.instance_var = instance_var # instance variable

    # instance method with keyword arguments
    def instance_method(self, a: int, b: int) -> int:
        """
        This is an instance method with a, b as arguments
        """
        return a + b

    @classmethod
    def class_method(cls) -> str:
        """
        This is a class method
        """
        return cls.class_variable

# function definition
def sample_func() -> None:
    """
    This is a sample function
    """
    # control structures, exception handling and loop
    for i in range(10):
        try:
            if i == 5:
                raise ValueError("It's 5")
            else:
                print(f"Number is {i}")
        except ValueError as e:
            print(e)

# async function definition
async def sample_async_func() -> None:
    """
    This is an asynchronous function
    """
    # asynchronous functionality
    pass

# decorators with arguments
@decorator_name(arg1='arg1_val', arg2='arg2_val')
def decorated_func() -> None:
    """
    This is a decorated function
    """
    pass

# multi-line strings
multiline_str: str = """
This is a
multiline string
"""

# Escaping symbols in strings
escaped_str: str = "Hello\\nWorld"

# dict comprehensions
x: Dict[int, int] = {i: i ** 2 for i in range(10)}

# a sample one liner list comprehension
y: List[int] = [i ** 2 for i in range(10) if i % 2 == 0]

# lambda function
z: Callable[[int], int] = lambda x: x * x

# a sample usage of imported function
print(math.sqrt(PI))

# Regular expression match
re_match = re.search(pattern, "123abc456")
print(f"Match found: {re_match.group()}")

# calling a class method
print(SampleClass.class_method())

# calling a method with keyword argument
sample: SampleClass = SampleClass('instance_var_val')
print(sample.instance_method(a=5, b=10))

# the dunder-name variable
if __name__ == "__main__":
    sample_func()
