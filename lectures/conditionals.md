# Conditionals

A **conditional statement** allows us to change program control flow based on the truth value of a condition. They are a form of decision-based logic that some people use in their daily lives. For example, if the temperature is above 4°C, then wear sandals.

```python
temperature = 22
if temperature > 4:
    footwear = "sandals"
footwear # What's my footwear for today?
```

> [!note]
> [Indented code](../style-guide.md#indentation) following the `if` statement only runs when the condition is true!

## `print` function

While the Python console allows us to directly evaluate expressions like `footwear` and see the answer (`"sandals"`), Python Tutor doesn't work the same way. To report a value, we can call the `print` function, which displays values in human-readable form. What do you notice is different about the output when we print a value?

```python
print(footwear)
```

`print` is particularly helpful for showing multiple lines of text on the screen at once!

```python
print("You: How is the weather today?")
print("Me: It's", footwear, "weather!")
print("You: Are you sure it's " + footwear + " weather today?")
```

Calling `print()` (with empty parentheses) produces a blank line.

We'll learn more about functions in a future lesson: for now, we just need to be familiar with these different ways of calling `print` to show certain outputs.

## Booleans

To represent a concept like whether the temperature is above freezing, Python provides the `bool` data type that only has two possible values: `True` and `False`.

    22 > 4
    22 < 4
    22 == 4
    22 >= 22
    (22 > 4) and (5 < 6)
    (22 > 4) and (5 > 6)
    not (5 <= 6)
    not True

Booleans are values like numbers and text, so we can also assign them to variables.

```python
x = 22 < 4
x
```

## Practice: Sequential conditionals

Conditional statements can follow one after the other. How does Python evaluate this arithmetic program?

```python
x = 10
y = 5
if x > y:
    x = x - 4
    y = y + 4
if x < y:
    x = x + 1
    y = y - 1
x, y # What is the value of x and y?
```

## `if-else` statement

What happens if the temperature is right above freezing? It's no longer sandals weather!

```python
temperature = 1
if temperature > 4:
    footwear = "sandals"
footwear
```

> [!warning]
> The Python console keeps track of all variables, even ones defined in previously-run code snippets. **Restart Kernel...** to restart the Python console. Or, load Python Tutor using the code in `tutor.py`, which will only evaluate the last-run snippet.

To specify what to do when the condition is false, we can add an `else` case.

```python
temperature = 1
if temperature > 4:
    footwear = "sandals"
else:
    footwear = "sandals with socks"
footwear
```

## Practice: Nested conditionals

Conditional statements can be nested within each other to produce more complex logic. How does Python evaluate this program to report the absolute value?

```python
val = 22
if val < 0:
    result = -val
else:
    if val == 0:
        result = val
    else:
        if val > 0:
            result = val
        else:
            result = val
result # What's the absolute value of val?
```

How would you rewrite this program to simplify the control flow?

## `if-elif-else` statement

What if it's below freezing? We probably need close-toed shoes.

```python
temperature = -5
if temperature > 4:
    footwear = "sandals"
elif temperature >= 0:
    footwear = "sandals with socks"
else:
    footwear = "sneakers"
footwear
```

We can introduce as many `elif` cases as we like. Python will check cases from top to bottom and only run the first successful condition, or the `else` case if all other conditions failed. When does this code produce a different result from the previous code snippet?

```python
temperature = 0
if temperature >= 0:
    footwear = "sandals with socks"
elif temperature > 4:
    footwear = "sandals"
else:
    footwear = "sneakers"
footwear
```

## Practice: Control flow

Which statements will be printed when we run the following program?

```python
x = 5
y = 5
if x > 0:
    print("Statement 1")
elif y > 0:
    print("Statement 2")
else:
    print("Statement 3")
```
