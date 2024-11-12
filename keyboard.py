from typing import List
from convert import str_to_float

#Task 2
def gather_numbers() -> List[float]:
    """Continuously prompts the user for input until "done" is entered.
    Converts valid numerical inputs to floats and returns them in a list.
    Input: list[float]: A list of valid float numbers entered by the user.
    """
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")

        if user_input.lower() == "done":
            break

        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
        else:
            print(f"'{user_input}' is not a valid number. Please try again.")

    return numbers


if __name__ == "__main__":
    gathered_numbers = gather_numbers()
    print(f"Sum of numbers: {sum(gathered_numbers)}")

