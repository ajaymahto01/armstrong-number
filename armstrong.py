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


# ---- Main program ----
if __name__ == "__main__":
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Check the number and print the result
    if is_armstrong(num):
        print(f"{num} is an Armstrong number!")
    else:
        print(f"{num} is NOT an Armstrong number.")

    # Bonus: print all Armstrong numbers between 1 and 1000
    print("\nArmstrong numbers between 1 and 1000:")
    for n in range(1, 1001):
        if is_armstrong(n):
            print(n, end=" ")
