from typing import ((Optional))

#Task 1
def str_to_float(input_str: str) -> Optional[float]:
    """Converts a string to a float, if possible. If the conversion fails, returns None.
    Input: input_str (str): The string to convert to a float.
    Output: Optional[float]: The float value if conversion is successful, or None if it fails."""
    try:
        return float(input_str)
    except ValueError:
        return None

