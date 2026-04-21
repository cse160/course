---
exports:
  - format: typst
    template: ./
    id: more-file-processing-handout
downloads:
  - id: more-file-processing-handout
    title: Handout
---

# More File Processing

Sometimes, just reading the file contents isn't enough. To extract useful data, we might need to process the file contents by removing whitespace or parsing data.

## Removing whitespace

Earlier, when we read `file.fl`:

```{literalinclude} data/file.fl
```

The first line ended with a `\n` newline character, which is present in the output of both `f.read()` and looping over `f`.

```python
contents = 'Hello!\nI am a file :)'
```

To remove leading and trailing whitespace, call `strip`. When a parameter is specified, it will remove any leading or trailing characters matching any character from the given string.

    " hello     ".strip()
    "22he22llo222".strip("2")
    contents.strip()

## Practice: Nominees sans `\n`

Write code to read the `nominees.txt` again, but this time return a list of all the movie names without any trailing (or leading) newline characters.

## Parsing data

What if we have multiple data values present on the same line? Data programmers frequently work with a text file format called **comma-separated values** (CSV):

```csv
1, 2, 5, 0
```

To parse individual values from this line, we can read the file line-by-line and then `split` each string on the given character (or whitespace by default).

    "1, 2, 5, 0".split(",")
    "hi CSE 160 \n".split()

After we've parsed the CSV file, how do we handle any leftover spaces after each extracted data value?

## Practice: Menu items

```{literalinclude} data/menu.txt
```

```python
new_items = ["Chips", "Guac"]
prices = [2.50, 4.75]
```

Given a list of items and their prices in `menu.txt` as well as a list of `new_items` and a list of `prices` for those new items:

1. Add the new menu items to the end of the `menu.txt` file in the same format.
1. Display the total price of all items across the entire, updated menu.

## Practice: Temperatures

```{literalinclude} data/temps.dat
```

Write code that reads the contents of `temps.dat` and evaluates to a nested list of temperatures for each week.
