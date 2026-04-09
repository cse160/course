---
exports:
  - format: typst
    template: ./lectures/
    id: reference-handout
downloads:
  - id: reference-handout
    title: Handout
---

# Reference

## Conditionals

[`if` statements](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements) runs the indented block depending on the [truth value of the condition](https://docs.python.org/3/library/stdtypes.html#truth-value-testing). `if` statements can be followed by `elif` statements and up to one final `else` statement.

```python
if condition1:
    print("if condition1 was True")
elif condition2:
    print("elif condition2 was True")
elif condition3:
    print("elif condition3 was True")
else:
    print("elif condition3 was False")
```

## Loops

[`for` statements](https://docs.python.org/3.13/tutorial/controlflow.html#for-statements) iterate over sequences.

```python
for i in sequence:
    print(i)
```

If you don't already have a sequence of elements to loop over, [the `range()` function](https://docs.python.org/3.13/tutorial/controlflow.html#the-range-function) defines a sequence of integers `[start, start + step * 1, ..., start + step * i]` until the `stop` value is reached. If not specified, `start` is zero.

```python
range([start,] stop [, step])
```

## Functions

[Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions) allow us to write code once and reuse the code by calling it later.

```python
def function_here(input_things):
    """Description of function goes here"""
    manipulated_input = input_things * 2
    return manipulated_input
```

## Lists

[Lists](https://docs.python.org/3.13/tutorial/introduction.html#lists) are mutable sequences defined by square brackets.

```python
my_list = []      # empty list
my_list.append(2) # [2]
my_list.append(4) # [2, 4]
my_list.append(8) # [2, 4, 8]
print(my_list[0]) # access the first element of a list
```

### Assigning elements

List elements can be assigned and reassigned singly:

```python
my_list = [1, 2, 3, 4]    # [1, 2, 3, 4]
my_list[3] = "at index 3" # [1, 2, 3, 'at index 3']
```

Or as a slice:

```python
my_list[1:3] = ["at index 1", "at index 2"]
# [1, 'at index 1', 'at index 2', 'at index 3']
```

### Slicing

Slicing create a new list from a range of elements in the original list. The `start` index is inclusive while the `end` index is exclusive.

```python
new_list = original_list[start:end:step]
```

### `in` operator

The `in` operator evaluates to `True` if the `val` is in `my_list`, and `False` if it is not.

```python
contains = val in my_list
```

### Methods

The `index` method returns the index of the first occurrence of `val` in `my_list`. It will raise an error if `val` is not in `my_list`.

```python
i = my_list.index(val)
```

The `count` method returns the number of times a `val` appears in `my_list`.

```python
num_vals = my_list.count(val)
```

The `remove` method removes the first occurrence of a `val` from `my_list`.

```python
my_list.remove(val)
```

The `pop` method removes and returns the `i`-th element from `my_list`. If `i` is not given, then it will remove and return the last element by default.

```python
val = my_list.pop(i)
last = my_list.pop()
```

The `append` method adds a `val` to the end of `my_list`.

```python
my_list.append(val)
```

The `insert` method adds a `val` at index `i` in `my_list`.

```python
my_list.insert(i, val)
```

The `extend` method adds all the elements from `sequence` to the end of `my_list`.

```python
my_list.extend(sequence)
```

## Sets

[Sets](https://docs.python.org/3.13/tutorial/datastructures.html#sets) are a useful alternative to a list when you need an unordered collection of unique elements.

```python
my_data = set() # creates an empty set
some_data = set([1, 2, 3, "some", "stuff"])
other_data = {"one_pt", "another_pt"}
```

### `add` method

The `add` method adds a value to a set. Keep in mind that sets don't keep track of the order of elements and will ensure there are no duplicate elements.

```python
books = set([]) # creates an empty set
books.add("Quidditch Through the Ages")
print(books)    # this prints: {'Quidditch Through the Ages'}
```

### Removing elements

There are several ways to remove an element from a set.

```python
my_plan = {"eat", "sleep", "study", "play", "work"}

my_plan.pop()  # will choose and remove one ARBITRARY element
print(my_plan) # might print: set(['sleep', 'work', 'study', 'eat'])

my_plan.remove("work") # would run even if 'work' not in set
print(my_plan)         # might print: set(['sleep', 'study', 'eat'])

my_plan = my_plan - {"sleep"} # would run even if 'sleep' not in set
print(my_plan)                # might print: set(['study', 'eat'])

my_plan.remove("eat") # would be a KeyError if 'eat' wasn't in set
print(my_plan)        # might print: set(['study'])
```

### Comparing sets

As with lists, the `in` operator evaluates whether an element is present in a set.

```python
"Star Wars" in books                  # evaluates to False
"Quidditch Through the Ages" in books # evaluates to True
```

The `|` (vertical pipe, below the <kbd>backspace</kbd> key) is the **union** operator: update your current set by adding the new elements from other sets.

```python
data = set([1, 2, 3, 4])
other_data = {3, 4, 5, 6}
data |= other_data # same as: data = data | other_data
print(data)        # this yields the output: {1, 2, 3, 4, 5, 6}
```

The `&` (ampersand, on the <kbd>7</kbd> key) is the **intersection** operator: identify what elements sets have in common.

```python
my_music = {"classical", "rock", "jazz"}
cafe_music = {"jazz", "blues", "hipster"}
shared_music = my_music & cafe_music
print(shared_music) # this prints: {'jazz'}
```

The `-` (hyphen) is the **difference** operator: identify what elements are not in one set when compared to another.

```python
my_music = {"classical", "rock", "jazz"}
cafe_music = {"jazz", "blues", "hipster"}

unique_to_me = my_music - cafe_music
print(unique_to_me)   # this prints: {'classical', 'rock'}

unique_to_cafe = cafe_music - my_music
print(unique_to_cafe) # this prints: {'blues', 'hipster'}
```

## Dictionaries

A [dictionary](https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries) is an unordered mapping of keys to values.

- Keys must be **unique**: no duplicate keys.
- Keys must be **immutable**: `int`, `float`, and `string` types are OK as keys but not `list`, `set`, or `dict` types.
- Dictionaries are mutable, so key-value mappings can be added, removed, or replaced.

```python
empty_dict = {}
days_dict = {"su": 18, "sa": 20, "m": 17}
dict_of_lists = {
  "Sounders": [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
  "Seahawks": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  "Mariners": [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
}
```

### Accessing keys and values

Values stored in a dictionary can be retrieved by their key.

```python
print(days_dict["su"]) # prints 18
```

But trying to access a key that is not present will raise an error.

```python
print(days_dict["tu"]) # raises KeyError: 'tu'
```

The `get` method covers this case by providing a default value to return when the key is not present.

```python
print(days_dict.get("tu", 0)) # prints 0
print(days_dict.get("m", 0))  # prints 17
```

As with lists and sets, we can test if a key is `in` a dictionary.

```python
"tu" in days_dict # evaluates to False
"m" in days_dict  # evaluates to True
```

### Adding mappings

To add to a dictionary, assign to a key that does not exist.

```python
days_dict["tu"] = 8
# {'su': 18, 'tu': 8, 'sa': 20, 'm': 17}
```

Or use the `update` method.

```python
days_dict.update({"w": 10, "th": 7, "f": 26})
# {'su': 18, 'm': 17, 'tu': 8, 'f': 26, 'w': 10, 'sa': 20, 'th': 7}
```

### Updating mappings

Assigning to a key already in a dictionary changes the existing mapping.

```python
days_dict["su"] = 17
# {'su': 17, 'm': 17, 'tu': 8, 'f': 26, 'w': 10, 'sa': 20, 'th': 7}

days_dict["sa"] += 2
# {'su': 17, 'm': 17, 'tu': 8, 'f': 26, 'w': 10, 'sa': 22, 'th': 7}
```

### Removing mappings

The `del` statement can remove a mapping from a dictionary.

```python
del days_dict["su"]
# {'m': 17, 'tu': 8, 'f': 26, 'w': 10, 'sa': 22, 'th': 7}
```

### Iteration

When neither `keys()` nor `values()` is specified, we will iterate over the keys.

```python
for day in days_dict.keys(): # not necessary to specify .keys()
  print(day, days_dict[day])
# Prints on newlines: sa 22, m 17, tu 8, w 10, th 7, f 26
```

Use the `values()` method to iterate through just the values of a dictionary.

```python
for count in days_dict.values():
  print(count)
# Prints on newlines: 22, 17, 8, 10, 7, 26
```

Use the `items()` method to iterate through key-value pairs at the same time.

```python
for day, count in days_dict.items():
  print(day, count)
# Prints on newlines: sa 22, m 17, tu 8, w 10, th 7, f 26
```

## Tuples

[Tuples](https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences) are immutable ordered sequences of values. You can create new tuples and access individual elements but cannot change the elements in an existing tuple.

Tuples are defined by separating elements with commas. They'll commonly appear within parentheses to avoid ambiguity. Access elements of a tuple in the same way you access elements of a list.

```python
my_tuple = (1, "two", 3)
print(my_tuple[0]) # Prints: 1
print(my_tuple[1]) # Prints: two
print(my_tuple[2]) # Prints: 3
```

## Sorting

There are two ways to sort a list. For either way, you can provide methods for comparison, key finding, and specify whether the sort should be reversed.

### `list.sort` method

The [`list.sort`](https://docs.python.org/3.13/tutorial/datastructures.html#more-on-lists) method sorts the existing list and returns `None`.

```python
my_list = [100, 200, 0, -100]
my_list.sort()             # my_list: [-100, 0, 100, 200]
my_list.sort(reverse=True) # my_list: [200, 100, 0, -100]
```

### `sorted` function

The [`sorted`](https://docs.python.org/3.13/library/functions.html#sorted) function returns a new copy of the given list with all its elements rearranged into sorted order. Unlike the `list.sort` method, this function doesn't modify the original list. The following example sorts a list of tuples by each tuple's index-1 element.

```python
from operator import itemgetter

students = [("jane", "B"), ("john", "A"), ("dave", "B")]
sorted_by_letter = sorted(students, key=itemgetter(1))
print(students)
# [('jane', 'B'), ('john', 'A'), ('dave', 'B')]
print(sorted_by_letter)
# [('john', 'A'), ('jane', 'B'), ('dave', 'B')]
```

In the case of a tie, the original order between equivalent elements is maintained. In this case that means `'jane'` comes before `'dave'` because `'jane'` comes before `'dave'` in the original order. This behavior is called a "stable" sort. Not all sorting algorithms are stable, but Python's `list.sort` method and `sorted` functions are both stable.

### `itemgetter`

The [`itemgetter` function](https://docs.python.org/3.13/library/operator.html#operator.itemgetter) returns _another_ function. It's commonly used to define different ways to sort nested data structures.

```python
from operator import itemgetter

student_score = ("Robert", 8)
get_name = itemgetter(0)  # get_name now refers to itemgetter(0)
get_score = itemgetter(1) # get_score now refers to itemgetter(1)
name = get_name(student_score)   # name is now 'Robert'
score = get_score(student_score) # score is now 8

student_scores = [("Robert", 8), ("Alice", 9), ("Tina", 7)]
# sort the list of student scores by student name
sorted_by_name = sorted(student_scores, key=get_name)
print(sorted_by_name)
# Prints: [('Alice', 9), ('Robert', 8), ('Tina', 7)]

# sort the list of student scores by student name, but in reverse
reverse_by_name = sorted(student_scores, key=get_name, reverse=True)
print(reverse_by_name)
# Prints: [('Tina', 7), ('Robert', 8), ('Alice', 9)]

# sort the list of student scores by the students' scores
sorted_by_score = sorted(student_scores, key=itemgetter(1))
# OR sorted_by_score = sorted(student_scores, key=get_score)
print(sorted_by_score)
# Prints: [('Tina', 7), ('Robert', 8), ('Alice', 9)]

# sort by letter grade, and then by numeric score if there is a tie
students = [("jane", "B", 12), ("john", "A", 15), ("dave", "B", 10)]
sorted_by_letter_then_score = sorted(students, key=itemgetter(1, 2))
print(sorted_by_letter_then_score)
# Prints: [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

## Classes

[Classes](https://docs.python.org/3.13/tutorial/classes.html#a-first-look-at-classes) provide a way to bundle data and functionality together.

```python
class MyClass:
    def __init__(self [, args]):
        # Initializes the object

    def method(self [, args]):
        # Provides functionality
```

To use classes, create (instantiate) an object and call its methods. The `self` parameter is automatically and implicitly provided.

```python
my_object = MyClass()
my_object.method([args])
```
