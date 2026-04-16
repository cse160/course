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
file = open("file-processing.md")
```

To read the entire contents of the file into a single string:

```python
file.read()
```

Alternatively, to read the file one line at a time, we can iterate over the file object using a `for` loop:

```python
for line in file:
    print(line)
```

## Writing files

To write a file from Python back to the computer file system, first call the `open` function with the `"w"` (write) mode argument:

```python
file = open("file-processing.md", "w")
file.write(string)
```

> [!warning]
> When in `"w"` (write) mode, the existing file contents are completely overwritten!

Alternatively, to append to content to the end of a file, call the `open` function with the `"a"` (append) mode argument:

```python
file = open("file-processing.md", "a")
file.write(string)
```

In append mode, existing file contents are not overwritten; new content is just added to the end.

## Closing files

We're not done yet! When you are finished working with a file, it's important to close it:

```python
file.close()
```

Changes to a file may not be fully implemented or saved until `close` is called. Furthermore, keeping a file open may prevent other applications from using or modifying the file.

## Example: Writing in read mode

What happens if we try to write to a file opened in read mode?

```python
f = open("file-processing.md", "r")
print(f.read())
f.write("New content :)")
f.close()
```

## Newline Characters

When writing to a file, we need to specify every character to be written including line breaks. `\n` is a **newline character**.

```python
f = open("test.txt", "w")
f.write("New content!\n")
f.write("Scratch that.")
f.close()
```

## Example: Reading twice

What happens if you call `read` multiple times on the same opened file?

```python
f = open("file-processing.md", "r")
print(f.read())
print(f.read())
f.close()
```
