---
exports:
  - format: typst
    template: ./
    id: tuples-and-sorting-handout
downloads:
  - id: tuples-and-sorting-handout
    title: Handout
---

# Tuples and Sorting

Lists, strings, and tuples are all ordered sequences. However, unlike lists, a **tuple** is an immutable sequence: a sequence that cannot be changed after it has been created.

## Tuples

Tuples are defined by the `,` (comma) operator. But commas are used in many places in Python. To resolve ambiguity, use `()` (parentheses) to indicate a sequence of comma-separated elements belong in a tuple, just like how `[]` (square brackets) indicate a sequence of comma-separated elements belong in a list.

```python
w = (4, 7, 9)
x = ("once", "upon", "a", "time")
y = ()  # An empty tuple

# Parentheses can make things clearer but are often not needed:
z = "kevinl", "blue"
```

> [!warning]
> To create a tuple with exactly *one* item, you must include a trailing comma. Otherwise, Python evaluates it as a regular expression in parentheses.
>
> ```python
> z = 19,   # A tuple containing one item
> num = 19  # num is just an integer!
> ```

Retrieve elements from a tuple using standard sequence operations:

    w = (4, 7, 9)
    w[0], w[1], w[2]
    len(w)

    x = ("once", "upon", "a", "time")
    x[4]

## Practice: w, x, y, z

Given the tuples `w = (4, 7, 9)` and `x = ("once", "upon", "a", "time")`, which statement will result in an error?

    y = w[2]
    x[3][2]
    z = ([1, 2], [3, 4])
    w[1] = 35

## Tuples in the wild

The `dict.items()` function returns a sequence of key-value pairs represented as tuples: `(key, value)`.

```python
fav_color = {"rea2000": "blue", "jamespw": "green", "emmalu10": "gold"}

for uwnetid, color in fav_color.items():
    print("favorite color of", uwnetid, "is:", color)
```

Tuples are commonly used to return multiple values from a single function call. The returned tuple can then be **unpacked** into separate variables.

```python
def read_data(fname):
    data = []
    label = []
    # ... code that populates the two lists ...
    return data, label

data, label = read_data("data/mnist.csv")
```

## Reference semantics

Understanding mutability requires differentiating between variables (names) and the objects they refer to in memory.

**Assigning a variable** changes the variable's value. It does not mutate (modify) the original object.

```python
size = 6
lst2 = lst1
```

**Mutating an object** mutates (modifies) the object's internal state, so any variable referencing that object will also see the change.

```python
lst1[2] = 5
lst1.append(12)
```

Of the three ordered sequence types (lists, strings, and tuples), only lists are mutable.

## Practice: Tracing memory

Trace the following code in Python Tutor. What will `lst1`, `lst2`, and `lst3` evaluate to at the end of the execution?

```python
lst1 = [7, 8, 9]
lst2 = ["e1", "e2"]

lst3 = lst2
lst2 = lst1

lst1[2] = 5
lst1.append(12)
```

## Sorting

Python provides two ways to sort data: the `sort()` method and the `sorted()` built-in function.

- `list.sort()` is a method that sorts the given list **in-place**. It modifies the original list and returns `None`. It can only be used on lists.
- `sorted(itr)` is a built-in function that takes an iterable (like a list, string, tuple, or dictionary keys) and returns a **new sorted list**. It leaves the original iterable unchanged.

```python
quote = "with great power there must also come great responsibility".split()
```

    sorted(quote)
    quote

    quote.sort()
    quote

Sometimes the default sorting behavior (alphabetical for strings, numerical for numbers) is not what you need. You can customize the sorting criteria using a **sort key**. This function is called on each element to determine the value that will be used for comparisons.

```python
names = ["Isaac Newton", "Ada Lovelace", "Fig Newton", "Grace Hopper"]
sorted(names, key=len)
```

```python
def last_name(name):
    return name.split()[1]

sorted(names, key=last_name)
```

> [!note]
> If there is a tie between elements based on the sort key, Python preserves their original relative ordering.

## `itemgetter`

When working with tuples or dictionaries, writing custom functions just to extract a specific index or key can be tedious. Python's `operator` module provides `itemgetter`, a convenient tool for creating functions that extract specific elements. For example, consider the following students and their favorite numbers.

```python
fav_number = [("Ann", 7), ("Raul", 6), ("Ted", 4), ("Lisa", 6)]
```

One way is to define a function that returns just the number in each pair and pass it as the sort key.

```python
def get_second(pair):
    return pair[1]

sorted(fav_number, key=get_second)
```

Another way is to use `itemgetter`.

```python
from operator import itemgetter

sorted(fav_number, key=itemgetter(1))
```

`itemgetter` can even index into dictionaries too!

```python
fav_number = [
    {"name": "Robert", "number": 8},
    {"name": "Alice", "number": 9},
    {"name": "Tina", "number": 7}
]

sorted(fav_number, key=itemgetter("number"))
```

## Multiple sorting criteria

To sort by multiple criteria (e.g., sort by number, and sort by name only if there's a tie), pass multiple arguments to `itemgetter`. Order matters: put the most important criterion first!

```python
fav_number = [("Robert", 8), ("Alice", 9), ("Tina", 10), ("James", 8)]

sorted(fav_number, key=itemgetter(1, 0))
```

Since Python preserves the order of ties, an alternative approach is to sort by the least important criterion first before proceeding to the most important criterion last:

```python
sorted_by_name = sorted(fav_number, key=itemgetter(0))
sorted_by_number_then_name = sorted(sorted_by_name, key=itemgetter(1))
```
