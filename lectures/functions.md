---
exports:
  - format: typst
    template: ./
    id: functions-handout
downloads:
  - id: functions-handout
    title: Handout
---

# Functions

Variables allow us to assign values, conditionals allow us to shape control flow, and loops allow us to repeat code. **Functions** allow us to _reuse_ code according to specified inputs. Functions compartmentalize code so it can be used, or "called," whenever we want. They help:

- Organize code
- Reuse code with different inputs
- Abstract away (hide) details

```python
def function_name(parameter):
    # function body
```

Key components of a function include:

- The `def` keyword followed by the function name
- Zero or more **parameters**: input variables for the function
- A colon at the end of the definition line followed by indented function body

To **call a function** (to use it), write its name followed by parentheses indicating the **arguments** that fill-in the parameters, such as `function_name(4)`.

## Return statements

`return` is a Python keyword that is used to output a value from a function.

```python
def function_name(parameter):
    # more function code belongs here
    return value

    print("Hey") # unreachable code
```

The `return` statement ends the function call and _returns_ control flow back to the caller. In the example above, the `print` statement is unreachable.

## Example: Hello

```python
def print_hello():
    print("Hello!")

print_hello()
```

## Example: Echo

```python
def print_hello():
    print("Hello!")
    return "Hello!"

print(print_hello())
```

## Practice: Divisibility

What would Python display?

```python
def is_divisible(a, b):
    # What is the remainder after dividing a by b?
    if a % b == 0:
        return True
    return False

print(is_divisible(9, 3))
```

## Example: Exclaim

```python
def exclaim(phrase):
    print(phrase + "!!!")

exclaim("Hi")
exclaim("Yayy")
```

## Example: Area of a circle

Functions can also have default arguments. If not specified by a function call, the parameter will use the default value.

```python
import math

def area(radius=1):
    return math.pi * (radius ** 2)

print(area(2))
print(area())
```

## Documentation strings

A function's **docstring** (documentation string) provides useful [documentation](../style-guide.md#documentation) about how to use the function.

```python
def function_name(parameter):
    """
    Documentation string content goes here!
    """
    # function body
```

> [!important]
> A good docstring should describe _what_ a function does (its inputs and outputs) rather than _how_ it does it (its internal implementation). If a docstring describes the internal logic, it will become outdated and misleading if you ever rewrite the code to be more efficient.

:::{error} Bad
:class: code-example

```python
def is_prime(n):
    """
    Checks if n is less than or equal to 1, returning False if so. Then loops
    from 2 up to n-1. If n modulo the loop variable is 0, returns False. If the
    loop finishes without returning False, returns True.
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```
:::

:::{hint} Good
:class: code-example

```python
def is_prime(n):
    """
    Determines whether a given integer is a prime number.

    Arguments:
        n: An integer to be checked.

    Returns:
        True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```
:::

## Practice: Is it even?

Write a function `is_even` that returns true [if and only if](https://en.wikipedia.org/wiki/If_and_only_if) the given number is even (false otherwise).
