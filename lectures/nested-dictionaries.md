---
exports:
  - format: typst
    template: ./
    id: nested-dictionaries-handout
downloads:
  - id: nested-dictionaries-handout
    title: Handout
---

# Nested Dictionaries

While dictionary keys must be an immutable data type, such as `int`, `float`, or `str`, dictionary values can be of any data type. Values do not need to be unique, and they can even be more complex data structures like lists. It is common to use a list as a value in a dictionary when you want to associate a single key with multiple pieces of data.

```python
class_rolls = {
    "CSE160": ["John", "Maria"],
    "CSE163": ["Anna", "Lin", "Ray"]
}

class_rolls["CSE160"][1]
```

You can also use lists to store multiple attributes for a single entity:

```python
students = {
    "John Doe": [1234567, "jdoe@uw.edu", "B"],
    "Maria Vera": [3456789, "mvera@uw.edu", "A"]
}

students["John Doe"][0]
```

Sometimes, using a list as a value can be confusing because you have to remember which index corresponds to which attribute (e.g., remembering that index 1 is the email address). We can swap the nested list out for a **nested dictionary**.

```python
students = {
    "John Doe": {
        "ID": 1234567,
        "email": "jdoe@uw.edu",
        "grade": "B"
    },
    "Maria Vera": {
        "ID": 3456789,
        "email": "mvera@uw.edu",
        "grade": "A"
    }
}

students["John Doe"]["email"]
```

To access a value inside a nested dictionary, chain the square bracket lookups: first the key for the outer dictionary, then the key for the inner dictionary.

## Practice: Student data

Given the nested `students` dictionary above, which statement will run without error?

    students[2]
    students["Lisa"] = 3
    students["Maria Vera"][1]
    students["John Doe"][ID] = 4567734

## Practice: Progress check

Given the following expanded `students` dictionary, write Python expressions to accomplish each of the tasks below:

```python
students = {
    "John Doe": {"ID": 1234567, "email": "jdoe@uw.edu", "grade": "B"},
    "Maria Vera": {"ID": 3456789, "email": "mvera@uw.edu", "grade": "A"},
    "Jun Li": {"ID": 5678912, "email": "jli@uw.edu", "grade": "B"}
}
```

1. Determine if `"Maria Vera"` is in this course.
1. Find Jun Li's email address.
1. Modify John Doe's grade.
1. Add a new student to the dictionary.
1. Create a list of all student email addresses.

## Practice: Cities and states

Write code to create a dictionary that maps state names to an inner dictionary. The inner dictionary should map city names to their populations.

```python
{
    "Washington": {"Seattle": 800000, "Olympia": 56000},
    "Oregon": {"Portland": 635000, "Salem": 180400},
    "Michigan": {"Detroit": 645700}
}
```

For extra practice:

1. Write this as a function that takes a filename (e.g., `"population.txt"`) as a parameter and returns the nested dictionary.
1. Given your nested dictionary, create a new (non-nested) dictionary that maps *only* cities to their populations.
1. Using this new dictionary, find the average population over all cities.
