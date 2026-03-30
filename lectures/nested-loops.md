---
exports:
  - format: typst
    template: ./
    id: nested-loops-handout
downloads:
  - id: nested-loops-handout
    title: Handout
---

# Nested Loops

We've now seen a few ways to use loops.

1. ```python
   for _ in range(6):
       print("Hi!")
   ```
1. ```python
   for i in range(5, 0, -1):
       print(i)
   ```
1. ```python
   for x in ["Hi", "Ciao", "Hola"]:
       print(x)
   ```
1. ```python
   for c in "Go Huskies!":
       print(c)
   ```

> [!note]
> In the first example, `_` (underscore) is a valid variable name! We tend to use it to indicate that the variable is a placeholder that won't be useful.

What if we wanted to keep track of two counts at the same time? The solution is to put a `for` loop inside another `for` loop.

```python
for i in range(1, 5):
    print(i, "Times Table")
    for j in range(1, 5):
        print(i, "x", j, "=", i * j)
```

## Practice: Counting prints

How many times is "CSE 160" printed?

```python
for i in range(2, 8, 2):
    for j in range(5):
        print("CSE 160")
```

## Example: Pairing elements

Nested loops can be used to pair every department string from the outer loop with every course number from the inner loop.

```python
for dept in ["CSE", "BIO", "INFO"]:
    for num in [180, 331, 480]:
        print(dept, num)
```

## Example: Seeing stars

Outer loop variables can be accessed within the inner loop, not only to pair-up elements but even to setup the inner loop.

```python
for i in range(5):
    line = ""
    for j in range(i):
        line += "*"
    print(line)
```

> [!note]
> The shortcut `line += "*"` used in the body of the inner loop is equivalent to `line = line + "*"`.

## Practice: Seeing stars in reverse

Modify the preceding code snippet (repeated below) to print the rows of stars in reverse order: the last printed line should become the first one and so forth.

```python
for i in range(5):
    line = ""
    for j in range(i):
        line += "*"
    print(line)
```

## Practice: Dotted lines

Write code that uses `for` loops to print the output:

    ....1
    ...2.
    ..3..
    .4...
    5....
