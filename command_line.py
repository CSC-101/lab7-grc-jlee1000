#Task 3
import sys
from typing import List
from convert import str_to_float

def process_arguments(args: List[str]) -> float:
    """Processes a list of command-line arguments, converting each to a float if possible,
    and returns the sum of all valid float values.
    Input: args (List[str]): A list of strings representing command-line arguments.
    Output: float: The sum of all valid floats in the argument list."""

    total = 0.0
    for arg in args:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total

if __name__ == "__main__":
    print(sys.argv)
