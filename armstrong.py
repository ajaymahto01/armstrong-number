# Armstrong Number Checker
# An Armstrong number (also called a narcissistic number) is a number that
# equals the sum of its own digits, each raised to the power of the total
# number of digits.
# Example: 153 has 3 digits -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 ✔


def is_armstrong(number):
    """
    Check whether `number` is an Armstrong number.

    Algorithm:
    1. Find how many digits the number has (call it n).
    2. Raise each individual digit to the power of n.
    3. Add up all those powered digits.
    4. If that sum equals the original number, it's an Armstrong number.

    Example: 153 -> n=3 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 -> True
    """
    # Convert the number to a string so we can loop through each digit easily
    digits = str(number)

    # Count how many digits the number has (this is our power)
    power = len(digits)

    # This will hold the running total of digit^power
    total = 0

    # Loop through every digit in the number
    for digit in digits:
        total += int(digit) ** power

    # If the sum equals the original number, it's an Armstrong number
    return total == number


def _sum_of_digit_powers(digits, power):
    """
    Recursively add up each digit in `digits` raised to `power`.

    Base case: no digits left -> nothing to add, so return 0.
    Recursive case: take the power of the first digit, then add the
    result of solving the same problem for the rest of the digits.
    """
    if digits == "":
        return 0
    first_digit = int(digits[0])
    remaining_digits = digits[1:]
    return first_digit ** power + _sum_of_digit_powers(
        remaining_digits, power
    )


def is_armstrong_recursive(number):
    """
    Check whether `number` is an Armstrong number, using recursion
    to add up the powered digits instead of a for-loop.

    Example: 153 -> n=3 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 -> True
    """
    digits = str(number)
    power = len(digits)
    return _sum_of_digit_powers(digits, power) == number


# ---- Main program ----
if __name__ == "__main__":
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Check the number and print the result (loop-based version)
    if is_armstrong(num):
        print(f"{num} is an Armstrong number!")
    else:
        print(f"{num} is NOT an Armstrong number.")

    # Same check, but using the recursive version instead
    if is_armstrong_recursive(num):
        print(f"(recursive check agrees: {num} is an Armstrong number!)")
    else:
        print(f"(recursive check agrees: {num} is NOT an Armstrong number.)")

    # Bonus: print all Armstrong numbers between 1 and 1000
    print("\nArmstrong numbers between 1 and 1000:")
    for n in range(1, 1001):
        if is_armstrong(n):
            print(n, end=" ")
