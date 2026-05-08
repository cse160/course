---
exports:
  - format: typst
    template: ./
    id: objects-handout
downloads:
  - id: objects-handout
    title: Handout
---

# Objects

Python provides many ways to manage program complexity. Rather than creating variables to represent every single element, elements can be organized into a hierarchy of lists and dictionaries. Rather than copy-pasting similar pieces of code across your project, program logic can be organized into functions to enable reuse. But what if you need to organize data and program logic into a single unit? **Objects** combine data structures with your own functions that can operate on them.

- A **class** is a blueprint, template, or general outline for objects.
- An **Object** or **instance** is a specific realization of that class.

We define a class using the `class` keyword. By convention, class names are capitalized with no underscores in between each word.

```python
class ClassName:
    class_var = 42

    def __init__(self, parameter):
        self.instance_var = parameter

    # ... other methods ...
```

- `class ClassName:` defines the class blueprint. Everything inside the class must be indented.
- `def __init__(self, parameter):` is a special method (function) that is automatically called when a new object is created.
- `self` is a special variable that refers to the specific object (instance) being created or modified.
- `self.instance_var` is an **instance variable**. Its value is unique to each specific instance of the class.
- `class_var = 42` is a **class variable**. Its value is shared across all instances of the class.
- Functions defined inside a class (like `__init__`) are called **methods**.

Creating an instance of a class is called **instantiation**.

    my_object = ClassName(18)

Class and instance variables (aka attributes or fields) can be accessed using dot notation.

    my_object.instance_var
    my_object.class_var
    ClassName.class_var

## Practice: Pokemon

Consider this `Pokemon` class.

```python
class Pokemon:
    hp = 20  # Class variable shared by all Pokemon instances

    def __init__(self, name, kind):
        self.name = name     # Instance variable
        self.type = kind     # Instance variable


# Creating specific Pokemon instances
charmander = Pokemon("Charmander", "Fire")
piplup = Pokemon("Piplup", "Water")
```

Does `charmander.hp += 40` work? What is `piplup.hp` afterwards?

```python
charmander.hp += 40
piplup.hp
```

## Practice: Evolving Pokemon

Pokemon can evolve!

```python
class Pokemon:
    hp = 20

    def __init__(self, name):
        self.name = name

    def evolve(self):
        self.hp *= 2

    def evolve_all(self):
        Pokemon.hp *= 3


eevee = Pokemon("Eevee")
bulbasaur = Pokemon("Bulbasaur")

eevee.evolve()
eevee.evolve_all()
```

What is the value of `bulbasaur.hp` afterwards?

## Practice: University

Define a `University` class with the following attributes and methods:

- `name`: a string
- `mascot`: a string
- `enrollment`: an integer
- `depts`: a list of strings
- `welcome(self)`: prints "`mascot` welcomes you to `name`"
- `add_dept(self, new_dept)`: appends `new_dept` to the `depts` list.

## Nested objects

Just as we can have nested structures, objects can also contain other objects! For example, instead of storing a list of strings for the departments in our `University` class, we could populate it with a list of `Department` objects:

```python
class Department:
    def __init__(self, name):
        self.name = name


cse = Department("Computer Science & Engineering")
bio = Department("Biology")
info = Department("School of Information")

# Our depts list now stores custom objects instead of strings
uw.depts = [cse, bio, info]
```

## Dunder Methods

**Dunder** (double underscore) methods serve special purposes in Python.

- `__init__(self, ...)` initializes the instance variables. Called automatically when creating a new instance.
- `__str__(self)` returns a human-readable string representation of the object. Called by `str` and `print`.
- `__repr__(self)` returns a Python-interpretable string representation of the object. It's displayed by the Python console.
- `__eq__(self, other)` returns `True` if and only if `self` and `other` are considered equivalent.

How would you add dunder methods to each of the above classes?
