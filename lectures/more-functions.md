---
exports:
  - format: typst
    template: ./
    id: more-functions-handout
downloads:
  - id: more-functions-handout
    title: Handout
---

# More Functions

What happens when we call a function?

```python
def my_function(a, b):
    c = a * b
    if c % 2 == 0:
        return c - a
        d = 1 / 0
    return 2 / 0

result = my_function(10 / 5, 3)
```

Here is a summary of the steps taken when a function call evaluates:

1. Evaluate the function name and arguments.
1. Create a new frame to assign argument values to parameters.
1. Evaluate the function body.
1. At a return statement, evaluate the expression. If no return is encountered, return `None`.

## Practice: Mystery

What would Python display?

```python
def mystery(a, b):
    return a * b

mystery(mystery(2, 6), 3)
```

## Practice: Tacos

What would Python display?

```python
def food():
    print("Tacos :)")

print(food())
```

## Variable scope

The scope of a variable is the area of code in which the variable is defined. In Python, there are two scopes:

- **Local scope**: Variables (including parameters) defined inside a function body. The value of the variable is accessible only within the function.
- **Global scope**: Everything else. The value of the variable is accessible anywhere in the program (including inside functions).

## Practice: Variable-ception

What would Python display?

```python
x = False

def my_function(x):
    print(x)

my_function(True)
x
```

## Practice: Slippery scope

What would Python display?

```python
x = 1
y = 2

def func1(x):
    y = 1
    return x + y

def func2(x):
    x = 5
    x = func1(x)
    return x + y

x = func2(x)
x
```
