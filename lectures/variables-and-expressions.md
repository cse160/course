---
exports:
  - format: typst
    template: ./
    id: variables-and-expressions-handout
downloads:
  - id: variables-and-expressions-handout
    title: Handout
---

# Variables and Expressions

Variables and expressions are the building blocks of data programming.

## Expressions

An **expression** is a combination of values, variables, or even other expressions that produce a single **value** or result. From a science perspective, expressions are like research questions. We can calculate the answer to the following _arithmetic expressions_.

    100 + 60
    80 * 2
    44 / 2
    2 ** 3
    3 * 4 + 5 * 6

The process of answering these questions is called **evaluation**. Python evaluates an expression (a question) to produce a value (an answer). With more complicated expressions, the order of operations might become unclear, so we can use parentheses to indicate precedence.

    (12 - 2) / 5 * 3

## Numbers and text

Every value has a type. **Types** represent specific forms of data with specific ways for using and combining them.

`100` and `60` are examples of the `int` data type used to represent integers. We can add two `int` values using the `+` operator. The result of dividing two `int` values can be an `int` or a `float` (decimals, or real numbers).

    100 + 60
    100 / 60

What about text? The `str` type represents text enclosed by either `'` (single quotes) or `"` (double quotes). Adding two `str` values with the `+` operator concatenates the strings.

    "cse160"
    "cse" + '160'
    "100" + 60
    "" # empty string

> [!note]
> The `#` (hash) indicates the rest of the line is a comment not for Python to run.

What happens if we try to add a `str` and an `int`?

    "cse" + 160

## Variables

A **variable** is a container for storing values. We assign values to variables using **assignment statements**.

    x = 5
    y = 34
    z = 100 + 60

In Python, variable names follow some rules.

- Variable names must start with a letter, not a digit or special character.
- Variable names are case sensitive, so `Total` is different from `total`.
- Variable names should follow our standard Python [style guidelines](../style-guide.md#variable-names).

An assignment statement is executed through a two-step process:

1. Evaluating the expression on the right-hand side to a value
1. Storing that value in the variable shown on the left-hand side

Expressions can also refer to previously-assigned variables. In the following code snippet, what is stored in `x`, `y`, and `z`?

    x = 5
    y = 10 + 10
    z = x + 1

## Python Tutor

In the previous example, it wasn't too hard to keep track of all three variables. But the more complicated programs we'll run into in the future will require a more careful analysis of how Python evaluates programs. What are the values of `first` and `second` at the end of the following snippet?

```python
first = 8
second = 19
first = first + second
second = first - second
first = first - second
```

After running the snippet, copy-paste the code in `tutor.py` into your Python console and run it to load [Python Tutor](https://pythontutor.com/), a free online tool for visualizing program evaluation.

> [!important]
> **Before each step, predict what will happen next.** If the prediction doesn't match reality, explain how your thinking differed from Python's evaluation. By practicing predicting what happens next, you're developing your reading and debugging skills!

Let's try another example that will teach us a bit more about how variables and assignment statements work. What are the values of `a`, `b`, and `c` at the end of the following snippet?

```python
a = 5
b = 10
c = b
a = a + 1
b = b - 1
c = c + a
```
