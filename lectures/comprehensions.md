---
exports:
  - format: typst
    template: ./
    id: comprehensions-handout
downloads:
  - id: comprehensions-handout
    title: Handout
---

# Comprehensions

A **comprehension** is a concise way to create and describe a data structure (like a list or a dictionary). You can think of a comprehension as a clean, efficient shorthand for a standard `for` loop that builds up a collection.

There are three ways to define a list of squared numbers:

1. Explicitly writing out the whole list
   ```python
   squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   ```

1. Writing a loop, adding each result to a list
   ```python
   squares = []
   for i in range(11):
       squares.append(i * i)
   ```

1. Writing a list comprehension
   ```python
   squares = [i * i for i in range(11)]
   ```

## List comprehensions

The general form of a **list comprehension** is `result = [<expression> for <item> in <sequence>]`. For example:

    tens = [x * 10 for x in range(1, 11)]
    hundreds = [i * 10 for i in tens]
    letters = [x for x in "snow"]

## Example: Advanced expressions

The `<expression>` part of a comprehension can be anything, including a function call or a method.

    abs_list = [abs(x) for x in range(-5, 6)]
    word_list = ["  happy  ", " Wednesday   ", "folks "]
    no_spaces = [word.strip() for word in word_list]

## Example: List comprehensions

Let's list comprehensions for each of the following tasks.

1. A list comprehension of the **cubes** of the first 10 natural numbers: `[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]`
1. A list comprehension of the **powers of 2** (2⁰ through 2¹⁰): `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]`
1. Given a list of strings `colors = ["red", "blue", "purple", "gold", "orange"]`, a list comprehension of their lengths: `[3, 4, 6, 4, 6]`.

## Comprehensions with conditionals

You can add an `if` statement to the end of a comprehension to filter which items are included in the new list. The general form is `result = [<expression> for <item> in <sequence> if <condition>]`.

    big_vals = [x for x in input_list if x > 10]
    sq_over_ten = [x * x for x in range(11) if x * x > 10]

## Practice: Even elements

Given an input list `nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]`, write a list comprehension to produce a list of only the even numbers: `[4, 2, 6]`.

## Dictionary comprehensions

**Dictionary comprehensions** are like list comprehensions but for creating dictionaries. The general form is `result = {<key>: <value> for <item> in <sequence> if <condition>}`.

    squares = {i: i * i for i in range(10)}
    cubes = {x: x ** 3 for x in range(1, 11)}
    powers = {i: 2 ** i for i in range(11)}

## Practice: Color lengths

Given the list `colors = ["red", "blue", "purple", "gold"]`, write a dictionary comprehension mapping from the color string to its length: `{"red": 3, "blue": 4, "purple": 6, "gold": 4}`.

## Practice: Squares of even elements

Given the list `nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]`, write a dictionary comprehension mapping the even numbers to their squares: `{2: 4, 4: 16, 6: 36}`.
