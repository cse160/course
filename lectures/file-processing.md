---
exports:
  - format: typst
    template: ./
    id: file-processing-handout
downloads:
  - id: file-processing-handout
    title: Handout
---

# File Processing

A **file** is a collection of data stored in a structured format. We generally want to either read (load) data from a file or write (save) data to a file.

A file system is a hierarchical structure that organizes files using (nested) folders called **directories**. In most computer systems, files are stored in a specific directory with a unique file name. For example, the current `lectures` directory includes all the lectures for the course, each of which is represented by a `.md` (Markdown) file.

A **path** specifies a particular file in a particular directory. For example, the **absolute path** `~/COURSE_MATERIALS/lectures/file-processing.md` consists of:

- The `~` (tilde), which represents the current user's home directory.
- The subdirectory `COURSE_MATERIALS/lectures/` within the user's home directory.
- The file named `file-processing.md` within that subdirectory.

This uniquely identifies this file! But we could have also specified this as a **relative path** `./file-processing.md`, which consists of:

- The `.` (period), which represents the current directory.
- The file named `file-processing.md` within that directory.

We can even omit the `./` at the beginning leaving just the file name `file-processing.md`. This will also search for `file-processing.md` within the current directory.

## Reading files

To read a file in Python, first call the `open` function and specify the file path.

```python
f = open("data/file.fl")
```

To read the entire contents of the file into a single string:

```python
f.read()
```

> [!tip]
> `\n` is a **newline character**. Text editors like the one built into JupyterHub will automatically display the `\n` character as a newline.

Alternatively, to read the file one line at a time, we can iterate over the file object using a `for` loop:

```python
for line in f:
    print(line)
```

## Practice: Nominees

Write code that reads the contents of movie `nominees.txt` and evaluates to a list containing each movie name.

```{literalinclude} data/nominees.txt
```

## Writing files

To write a file from Python back to the computer file system, first call the `open` function with the `"w"` (write) mode argument:

```python
f = open("data/file.fl", "w")
f.write(string)
```

> [!warning]
> When in `"w"` (write) mode, the existing file contents are completely overwritten!

Alternatively, to append to content to the end of a file, call the `open` function with the `"a"` (append) mode argument:

```python
f = open("data/file.fl", "a")
f.write(string)
```

In append mode, existing file contents are not overwritten; new content is just added to the end.

## Closing files

We're not done yet! When you are finished working with a file, it's important to close it:

```python
f.close()
```

Changes to a file may not be fully implemented or saved until `close` is called. Furthermore, keeping a file open may prevent other applications from using or modifying the file.

Alternatively, we can use the `with` statement to automatically close resources at the end of the block:

```python
with open("data/file.fl") as f:
    print(f.read())
```

## Example: Writing in read mode

What happens if we try to write to a file opened in read mode?

```python
with open("data/file.fl") as f:
    print(f.read())
    f.write("New content :)")
```

## Practice: Rainfall

How rainy is Seattle? Let's analyze rainfall statistics collected by a sensor that can sometimes make mistakes and report negative rainfall.

```{literalinclude} data/rainfall.dat
```

Write a program to print a single line summarizing statistics about a rainfall data file:

- the sum total rainfall (only the positive integers),
- the number of positive integers, and
- the average rainfall.

If there are no positive integers in the file, print "No rain" instead of these three values. Use the `int` function to convert a string to an integer.
