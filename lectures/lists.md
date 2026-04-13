---
exports:
  - format: typst
    template: ./
    id: lists-handout
downloads:
  - id: lists-handout
    title: Handout
---

# Lists

A **list** is a data structure used to store an ordered sequence of **elements** (values).

- Each element in a list has an **index**.
- Indexing is zero-based, meaning counting starts with zero.
- Elements in a list do not have to be of the same type.

```python
a = [3, 1, 2 * 2, 1, 10 / 2, 10 - 1]
b = [5, 3, "hi"]
c = [4, "a", a]
d = [[1, 2], [3, 4], [5, 6]]
e = [] # An empty list
```

Retrieve information about a list and its elements using built-in list operators and list functions:

- `len(my_list)` returns the **length** of `my_list`. `len` also works for other sequence types like `str`.
- `my_list[index]` retrieves the element at the given `index` in `my_list`. Negative indexing counts from the end of the list: `my_list[-1]` retrives the last element.
- `my_list[start:end:step]` retrives a sublist or **slice** between the indices `start` (inclusive) and `end` (exclusive). It uses the same syntax rules as `range`.
- `x in my_list` evaluates to `True` if and only if `x` is in `my_list`, while `x not in my_list` evaluates to `True` if and only if `x` is not found.
- `my_list.index(x)` returns the index of the first occurrence of `x` in `my_list`. If `x` is not present, Python will raise a `ValueError`.
- `my_list.count(x)` returns the number of times `x` occurs in `my_list`.

## Practice: Slicing and dicing

For each expression below, what would Python display?

    a = [3, 12, 10, 7, 9, 7]
    a[0]
    a[5]
    a[6]
    a[-1]
    a[-2]
    a[1:3]
    a[2:5]
    a[:]
    a[0:len(a)]

Using `a = [2, 7, 3, 9, 4]`, write a Python expression to print `9 4 7`.

## Practice: Query this

For each expression below, what would Python display?

    a = [3, 12, 10, 7, 9, 7]
    9 in a
    16 in a
    a.index(7)
    a.index(16)
    a.count(7)
    a.count(16)

## Modifying list elements

There are many ways to modify the elements of a list. We can add elements to a list.

- `my_list.append(x)` adds item `x` at the end of `my_list`.
- `my_list.extend(L)` adds each of the elements in `my_list` `L` to the end of `my_list`.
- `my_list.insert(i, x)` inserts item `x` at index `i`.

> [!warning]
> When using `insert`, the inserted value does not replace the existing value; all following values are shifted to the right, and the length of the list grows by 1.

We can remove elements from a list.

- `my_list.remove(x)` removes the first occurrence of `x` and returns `None`.
- `my_list.pop(i)` removes and returns the element at the given index `i`, or the last element if `i` is not specified.

We can replace elements in a list.

- `my_list[i] = new_value` replaces the value currently stored at index `i` with `new_value`.
- `my_list[start:end] = new_sublist` replaces the given slice with the elements from `new_sublist`.

> [!warning]
> Replacing a slice with a longer or shorter sublist can change the total length of `my_list`!

We can rearrange list elements.

- `my_list.sort()` sorts elements in place, modifying `my_list`.
- `my_list.reverse()` reverses the order of elements in place, modifying `my_list`.

> [!note]
> Most of these list functions return `None`. The only exception is `pop`, which returns the element that was just removed.

## Practice: Insertion

What would Python display?

```python
lst = [1, 3, 5]
lst.insert(2, [4, 6])
lst[2]
```

## Practice: Removing and replacing

For each code snippet, explain each step in Python Tutor.

```python
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst.pop())
print(lst.pop(1))
lst.remove(3)
lst[3] = "blue"
lst[1:3] = [10, 11, 12]
```

```python
lst = [10, 12, 23, 54, 15]
lst.append(7)
lst.extend([8, 9, 3])
lst.insert(2, 2.75)
lst.remove(3)
print(lst.pop())
print(lst.pop(4))
lst[1:5] = [20, 21, 22]
lst2 = [4, 6, 8, 2, 0]
lst2.sort()
lst2.reverse()
lst3 = lst2
lst4 = lst2[:]
lst2[-1]= 17
```
