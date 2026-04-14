---
exports:
  - format: typst
    template: ./
    id: nested-lists-handout
downloads:
  - id: nested-lists-handout
    title: Handout
---

# Nested Lists

A nested list is a list that contains other lists! Oftentimes, we'll visualize a 2D nested list using a grid.

```python
seating_chart = [
    ["Mike", "John", "Julio", "Elizabeth"],
    ["Angela", "Sophia", "Randy", "Maria"],
    ["Raul", "Pauline", "Rachel", "Monica"]
]
```

|       | **0**  | **1**   | **2**  | **3**     |
|------:|--------|---------|--------|-----------|
| **0** | Mike   | John    | Julio  | Elizabeth |
| **1** | Angela | Sophia  | Randy  | Maria     |
| **2** | Raul   | Pauline | Rachel | Monica    |

## Practice: Chained indexing

To access individual elements, we can chain indexing operations one after the other. What would Python display?

    seating_chart[1]
    seating_chart[1][1]
    seating_chart[2][3]
    seating_chart[2][3][4]

## Iteration

How do you iterate through a nested list to print out each name one at a time? One way is to loop over each inner list, one inner list at a time.

```python
for row in seating_chart:
    for student in row:
        print(student)
```

Another way is to loop over the indices of the outer list and then the indices of each inner list.

```python
for ri in range(len(seating_chart)):
    for ci in range(len(seating_chart[ri])):
        print(seating_chart[ri][ci])
```

When would you prefer to use one approach over the other?

## Example: Even more nested lists

We can nest lists as deeply as we need to.

```python
letters = [
    [["a", "b"], ["c", "d"], ["e", "f"]],
    [["g", "h"], ["i", "j"], ["k", "l"]]
]
```

    letters[0]
    letters[0][2]
    letters[1][2][0]

## Practice: Average temperature

First, write a **helper function** `average` that returns the average of a list of values.

```python
[23, 24, 25, 27, 26] # Average: 25.0
```

Then, write a function `weekly_averages` that takes a nested list of temperatures for each week and prints the average temperature each week.

```python
temperatures = [
    [23, 24, 25, 27, 26], # Average: 25.0
    [0, -1, 1, -3, -2],   # Average: -1.0
    [9, 10, 11, 12, 11]   # Average: 10.6
]
```

How does Python Tutor pass each inner list from `weekly_averages` to `average`?

## Practice: Form study groups

Write a function `form_groups` that takes a list and an `int` maximum `size_limit` and returns a nested list where the given list elements are divided into groups of at most the `size_limit`. For example:

    students = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    form_groups(students, 5)
    # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

    form_groups(students, 3)
    # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
