# Blurring

In this homework, we will modify and extend a program to blur a black and white image.

By the end of this assignment, students will feel more comfortable:

1. Writing Python code using functions, lists, and conditional statements.
1. Writing Python code to read and write files.
1. Processing large, 2-dimensional nested lists with loops.

## Background

One type of data that may not immediately seem manipulatable with Python is image data. Yet, that is exactly what you will do in this assignment! Large quantities of image data are collected every day: telescopes gather images of distant galaxies, satellites take photos of the Earth's surface, your car license plate is photographed as you cross the 520 bridge, and video cameras collect footage as you enter a bank.

How are images typically represented in a computer? **Grayscale images** are represented by a rectangular grid of pixels where each pixel is an integer value from 0 to 255 where 0 is black and 255 is white. Each value in the rectangular grid represents one pixel in the image.

## Blurring filter

One way to process images is by adding filters. Blurring is a type of image filter. Blurring can be used to reduce the level of noise in an image and prepare it for further processing. Most images are stored in a computer as large rectangular grids of pixels. For example, consider the pixel grid:

     1    5   61
     4    3    2
    10   11  100

To **blur an image**, we can return a new grid with pixels that represent the average of each pixel and its 8 surrounding pixels. To calculate the average of the center pixel (with value `3`), add all 8 surrounding pixels to the center pixel and then divide the sum by 9: $$\frac{1 + 5 + 61 + 4 + 3 + 2 + 10 + 11 + 100}{9} = \frac{197}{9} = 21$$

> [!important]
> Instead of using `/` (true division), our Python program will use `//` (floor division) to ensure the resulting blurred pixel is a whole number between 0 and 255.

We then repeat this process for every pixel in the grid. For any pixel where its 8 surrounding pixels fall outside the edge of the image, treat missing values as 0. For the top right corner pixel (with value `61`): $$\frac{0 + 0 + 0 + 5 + 61 + 0 + 3 + 2 + 0}{9} = \frac{71}{9} = 7$$

For each following example pixel grid, predict the blurred result and check your answer.

1. ```
   1    2    3
   4    5    6
   7    8    9
   ```

   :::{dropdown} What is the blurred result?
   ```
   1    2    1
   3    5    3
   2    4    3
   ```
   :::

1. ```
   1  1  1  1  1  1
   1  1  1  1  1  1
   1  1  1  1  1  1
   1  1  1  1  1  1
   ```

   :::{dropdown} What is the blurred result?
   ```
   0  0  0  0  0  0
   0  1  1  1  1  0
   0  1  1  1  1  0
   0  0  0  0  0  0
   ```
   :::

1. ```
   10  10  10  10
   10  10  10  10
   10  10  10  10
   10  10  10  10
   10  10  10  10
   ```

   :::{dropdown} What is the blurred result?
   ```
   4   6   6   4
   6  10  10   6
   6  10  10   6
   6  10  10   6
   4   6   6   4
   ```
   :::

## Pixel grids

**Pixel grids** can be represented using a nested list of integers where the outer list represents each row of the grid with the same length. Then, each inner list (the contents of each row) stores integers for each pixel value. For example, consider the following pixel grid:

     1    5   61
     4    3    2
    10   11  100

This grid would be represented by the following Python list:

```python
[[1, 5, 61], [4, 3, 2], [10, 11, 100]]
```

Here is another example pixel grid:

     1   2   3   4   5
     6   7   8   9  10
    11  12  13  14  15

:::{dropdown} What is the Python representation for it?
```python
[[1, 2, 3, 4, 5 ], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
```
:::

If this list is assigned to the variable `grid`, access the top left corner pixel (with value `1`) with `grid[0][0]`. Access the bottom right corner pixel (with value `15`) with `grid[2][4]`.

## Running the program

From an attached Python console, blur `Husky.png` with the following command:

```ipython
%run blur_image.py images/Husky.png
```

The starter code will print the following output without actually blurring the image:

    Welcome to the CSE 160 Image Blurring program!
    Reading image images/Husky.png
    Program done.

Once you have finished this assignment, you will see two new (or updated) files in the current directory:

- `Husky_blurry.png`, which is a blurred version of the original `Husky.png` file.
- `Husky_blurry_grid.csv`, a CSV file containing the integer values of the blurred grid to make it easier to debug your program.

> [!tip]
> By default, JupyterHub opens CSV files in a spreadsheet-like tabular view. To view the text directly, right-click the file in the file browser and select **Open With | Editor**.

`blur_image.py` is split into a number of functions, each with a specific role. Each problem in this assignment corresponds roughly to one of the functions. We'll work from the bottom up, starting at the individual pixel level before working on the high-level algorithm to blur an entire image. This creates a hierarchy of function calls: `get_pixel_at` will be called by `average_of_surrounding`, which is in turn called by `blur`, which is finally called at the bottom of the program.

## Problem 1: Reading individual pixels

Document, doctest, and implement the function `get_pixel_at` that takes a `pixel_grid`, `i`, and `j` and returns the value in the `pixel_grid` at row `i` and column `j`. If there is no row `i` or no column `j` in the `pixel_grid`, return `0`. For example, consider the pixel grid:

```python
[[1, 5, 61], [4, 3, 2], [10, 11, 100]]
```

- `get_pixel_at(pixel_grid, 0, 2)` returns `61`: the value at row 0 and column 2.
- `get_pixel_at(pixel_grid, 3, 3)` returns `0`: the coordinates (3, 3) are out of bounds.

This function can be done in as few as 2 or 3 lines of code (not including mandatory docstring), but we've also seen good solutions that are between 6 to 10 lines of program logic. Remember that all functions need to be documented in your own words and include all the given examples as doctests.

> [!tip]
> `%run blur_image.py` without specifying a file will run all the doctests in the file.

When all doctests for `get_pixel_at` pass, you're ready to move on to the next problem.

## Problem 2: Averaging a pixel

Document, doctest, and implement the function `average_of_surrounding` that takes a `pixel_grid`, `i`, and `j` and returns the average of the values of the specified pixel and its 8 surrounding pixels. Remember to use `//` (integer division). This function **must** call the `get_pixel_at` function. For example, consider the pixel grid:

```python
[[1, 5, 61], [4, 3, 2], [10, 11, 100]]
```

- `average_of_surrounding(pixel_grid, 1, 1)` returns `21`.
- `average_of_surrounding(pixel_grid, 0, 2)` returns `7`.

This function can be done in about 5 or 6 lines of program logic but longer implementations can be good too.

When all doctests for `average_of_surrounding` pass, you're ready to move on to the next problem.

## Problem 3: Blurring a pixel grid

Document, doctest, and implement the function `blur` that takes a `pixel_grid` and returns a **new**, blurry pixel grid of the same size and shape. For example, consider the pixel grid:

```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

`blur` returns a new, blurred grid:

```python
[[1, 2, 1], [3, 5, 3], [2, 4, 3]]
```

We recommend starting with an empty list and appending new values to the list to create your new grid. Other approaches like copying the input list values are likely to result in tricky bugs. This function can be done in 8 to 15 lines of program logic but longer implementations can be good too.

When all doctests for `blur` pass, you're ready to move on to the next problem.

## Problem 4: Reading from CSV files

Document, doctest, and implement the function `read_grid` that takes a `file_path` and returns a pixel grid from the file contents. This function **must** call the `csv_line_to_pixels` function imported from `utils` at the top. For example, consider `test_grids/small_grid.csv`:

```{literalinclude} test_grids/small_grid.csv
```

`read_grid("test_grids/small_grid.csv")` returns:

```python
[[0, 0, 0], [0, 9, 0], [0, 0, 0]]
```

This function can be done in 5 to 8 lines of program logic but longer implementations can be good too.

When all doctests for `read_grid` pass, you're ready to move on to the next problem.

## Problem 5: Program entry point

At this point, running `blur_image.py` still doesn't actually do anything because we need to call the functions we defined earlier! Implement the CSE 160 Image Blurring program, which will do three things:

1. Generate a pixel grid based on a file name specified as a commandline argument. **This has already been done for you**.
1. Call the `blur` function.
1. Call `write_image` and `write_grid` (already imported from `utils.py`) to write the `output_image_filename` and the `output_grid_filename`.

## Code quality

Run our linter (automated code style checker) in the Python console with the expression `!flake8`. Edit the file and save your changes after addressing all reported issues. A successful `!flake8` run will print nothing when there are no linting issues to report.

```ipython
!flake8
```

Then, review our [style guide](../../style-guide.md), paying particular attention to:

- [Variable names](../../style-guide.md#variable-names)
- [Documentation](../../style-guide.md#documentation)
- Logical refactoring
  - [Loop zen](../../style-guide.md#loop-zen)
- Program design
  - [Fit and finish](../../style-guide.md#fit-and-finish)

> [!important]
> All functions must include doctests for the given examples.

## Collaboration

If you discuss an assignment with one or more classmates, **you must specify with whom you collaborated in a comment at the bottom of your submission**. You may discuss with as many classmates as you like, but you must cite all of them in your work. Note that you may not collaborate in a way that is prohibited, even if you cite the collaboration.

**At the bottom of your `blur_image.py` file**, state which students or other people (besides the course staff) helped you with the assignment, or that no one did.

## Submission

Remove any assert statements before submitting to gradescope. Submit `blur_image.py` on Gradescope under the assignment **Homework: Blurring**.
