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

- `armstrong.py` — contains two implementations of the Armstrong check
  (`is_armstrong()`, loop-based, and `is_armstrong_recursive()`,
  recursion-based) plus a runnable program that checks a user-entered
  number with both and lists all Armstrong numbers from 1 to 1000.
- `test_armstrong.py` — unit tests for both implementations, including a
  test that they always agree with each other.

## How to run

```bash
python3 armstrong.py
```

You'll be prompted to enter a number:

```
Enter a number: 153
153 is an Armstrong number!
(recursive check agrees: 153 is an Armstrong number!)

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

### The recursive version

`is_armstrong_recursive()` does the same check, but instead of a
for-loop it uses a recursive helper, `_sum_of_digit_powers()`, to add
up the powered digits:

- **Base case:** no digits left to add → return `0`.
- **Recursive case:** raise the first digit to the power, then add
  the result of solving the same problem for the rest of the digits.

For `153` (power `3`): `1^3 + solve("53")` → `1^3 + (5^3 +
solve("3"))` → `1^3 + 5^3 + (3^3 + solve(""))` → `1^3 + 5^3 + 3^3 + 0`
→ `153`.

## Try it yourself

Some Armstrong numbers to test: `1`, `9`, `153`, `370`, `371`, `407`, `9474`.

## Running the tests

Unit tests use Python's built-in `unittest` module — no extra install
needed. From the project directory, run:

```bash
python3 -m unittest test_armstrong -v
```

Expected output:

```
test_known_armstrong_numbers ... ok
test_known_non_armstrong_numbers ... ok
test_returns_a_boolean ... ok
test_single_digit_numbers_are_armstrong ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
