---
exports:
  - format: typst
    template: ./
    id: dictionaries-handout
downloads:
  - id: dictionaries-handout
    title: Handout
---

# Dictionaries

A **dictionary** is a data structure used to store mappings from unique **keys** to **values**.

- Unlike lists, dictionaries are not a sequence type: elements are not typically accessed by sequential index.
- Instead, given a key, you can look up its associated value. However, given a value, you cannot look up its key.
- **Keys** must be unique (no duplicate keys) and must be an immutable data type, such as `int`, `float`, or `str`.
- **Values** do not need to be unique and can be of any data type.

```python
fav_color = {"rea2000": "blue", "jamespw": "green", "lisaorii": "purple", "emmalu10": "gold"}
squares = {2: 4, 3: 9, 5: 25, -5: 25, -2: 4, -3: 9}
atomic_number = {"H": 1, "Fe": 26, "Au": 79}
food_price = {"Taco": 3.25, "Burrito": 7.5, "Chips": 2.5, "Guac": 4.75}
empty_dict = {} # An empty dictionary
```

Retrieve and modify information in a dictionary using square bracket syntax:

- `my_dict[key]` retrieves the value associated with the given `key`.
- `my_dict[key] = new_value` adds or updates a key-value pair in the dictionary.
- `del my_dict[key]` removes a key and its associated value from the dictionary.

> [!warning]
> Retrieving or removing a key that is not present in the dictionary will raise a `KeyError`. Use the `in` or `not in` keywords to determine whether a key is present in the dictionary.

## Practice: Spot the error

Given the dictionary `food_price = {"Taco": 3.25, "Burrito": 7.5, "Chips": 2.5, "Guac": 4.75}`, which statement will result in an error?

    print(food_price[2.5])
    food_price["Guac"] = 3
    del food_price["taco"]
    food_price[2.5] = "Chips"

## Iteration

By default, if we attempt to loop over a dictionary, we loop over only its keys in the order they were initially added to the dictionary.

```python
for uwnetid in fav_color:
    print(uwnetid, "fav color is", fav_color[uwnetid])
```

**Avoid iterating over a dictionary.** A very common mistake is to use a loop when you only needed to look up a single value. Only iterate over a dictionary if you need to modify or access the values associated with every key. To find a single person's favorite color, just look it up directly: `fav_color["rea2000"]`.

Dictionaries also have methods to retrieve collections of their keys, values, or key-value pairs:

- `my_dict.keys()` returns all the keys.
- `my_dict.values()` returns all the values.
- `my_dict.items()` returns all the `(key, value)` pairs, where the `key` is index 0 and `value` is index 1.

## Practice: Counting words

Write code that uses a dictionary to count how many times each unique word appears in the phrase below:

```python
phrase = "how much wood could a woodchuck chuck if a woodchuck could chuck wood"
```
