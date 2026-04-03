---
exports:
  - format: typst
    template: ./
    id: loops-handout
downloads:
  - id: loops-handout
    title: Handout
---

# Loops

What if we want to repeat the same code multiple times? We can either:

1. Type out or copy all the code however many times we want it to run. This is very tedious and makes it difficult to fix mistakes.
1. Write the code for only one iteration and have Python repeat it. This is much faster and easier to spot or correct mistakes!

A **`for` loop** allows us to repeat a block of code a specific number of times or iterate over a sequence of items.

```python
for i in range(10):
    # Loop body gets repeated
    print(i)
print("Done") # Outside of loop
```

Let's break down the components of this statement:

- `for` is the **keyword** that signals the start of the loop.
- `i` represents the **loop variable name**, which you can change. Its value is updated each time through the loop.
- `range(10)` is the sequence that **controls the loop**.
- `print(i)` is the **loop body**: the code that gets run once for each iteration of the loop.

## `range` function

`range` is a built-in function (like `print`) that produces a sequence of integers. It can be called with 1 argument, 2 arguments, or 3 arguments.

    range(5)
    range(2, 5)
    range(1, 11, 2)

## Practice: Range

Which `range` call will produce the numbers 10, 20, 30, 40, 50, 60, 70, 80, 90, 100?

    range(100)
    range(10, 100)
    range(10, 110)
    range(10, 100, 10)
    range(10, 110, 10)

## Practice: Rangefinding

Write code that uses a `for` loop to print:

    -4
    14
    32
    50
    68
    86

## Accumulator pattern

We can accumulate (sum, multiply, etc.) values while going through a `for` loop. For example, to sum the numbers from 0 to 4:

```python
total = 0
for i in range(5):
    total = total + i
print("The sum is:", total)
```

## Practice: Totals

What is the output of the following loop?

```python
total = 10
for number in range(1, total // 2):
    total = total - number
    print(total)
```

> [!note]
> The `//` (floor division) operator in Python divides a number but drops any remainder, leaving the result an `int` (integer).

## Practice: Squares

Write code that uses a `for` loop to print the numbers 1 through 10 squared:

    1
    4
    9
    16
    25
    36
    49
    64
    81
    10

As an extra challenge, modify your code so that it does not need to use the `*` multiplication operator. Do you notice any patterns between adjacent numbers?

## Looping over lists and strings

If `range` produces a sequence of numbers, can we just specify the numbers ourselves?

A **list** allows us to specify a sequence of values manually using square brackets `[]`.

```python
for i in [10, 13, 7]:
    print(i)
print("Done")
```

It turns out we can iterate over a lot of things! We can iterate over lists of strings.

```python
print("Some CSE 160 TAs:")
for name in ["Brianna", "Katie", "Suhas"]:
    print(name)
```

We can even iterate over the individual characters in a single string.

```python
for letter in "Kevin":
    print(letter)
```
