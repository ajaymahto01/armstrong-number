# Armstrong Number Checker

A simple Python script that checks whether a number is an **Armstrong number**
(also called a narcissistic number).

## What is an Armstrong number?

A number is an Armstrong number if the sum of its own digits, each raised to
the power of the total number of digits, equals the number itself.

**Example:** `153` has 3 digits.

```
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```

Since the result equals the original number, `153` is an Armstrong number.

## Files

- `armstrong.py` — contains the `is_armstrong()` function and a runnable
  program that checks a user-entered number and lists all Armstrong numbers
  from 1 to 1000.

## How to run

```bash
python3 armstrong.py
```

You'll be prompted to enter a number:

```
Enter a number: 153
153 is an Armstrong number!

Armstrong numbers between 1 and 1000:
1 2 3 4 5 6 7 8 9 153 370 371 407
```

## How it works

1. Convert the number to a string to loop over its digits.
2. Count the digits — this is the power to raise each digit to.
3. Raise each digit to that power and sum the results.
4. Compare the sum to the original number — if they match, it's an
   Armstrong number.

See the docstring on `is_armstrong()` in `armstrong.py` for the same
explanation alongside the code.

## Try it yourself

Some Armstrong numbers to test: `1`, `9`, `153`, `370`, `371`, `407`, `9474`.
