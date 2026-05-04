# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 4

# ~~~ Begin Problem 1 ~~~
def get_last_pixel(pixel_grid):
    """
    Given a nested list of integers (representing pixel values), return the value of the pixel
    (integer) on the last row in the last column of the given pixel_grid.

    The pixel_grid will always contain at least one value.

    Arguments:
        pixel_grid: a nested list of lists

    Returns: An integer representing the last int in the pixel_grid
    """
    # Write your code for Problem 1 here!


# ~~~ End Problem 1 ~~~

assert get_last_pixel([[5, 2, 3], [1, 5, 4]]) == 4
assert get_last_pixel([[1, 3], [3, 4], [15, 16], [9, 2]]) == 2
assert get_last_pixel([[100, 50]]) == 50
assert get_last_pixel([[35]]) == 35
assert get_last_pixel([[10, 3], [20, 7], [30, 1], [40, -4]]) == -4
assert get_last_pixel([[10], [20], [30], [40]]) == 40
assert get_last_pixel([[1, 2, 3, 4], [8, 8, 6, 9]]) == 9


# ~~~ Begin Problem 2 ~~~
def sum_grid(pixel_grid):
    """
    Given a nested list of integers (representing pixel values), return the sum of all the values
    in the given pixel_grid.

    The pixel_grid will always contain at least one value.

    Arguments:
        pixel_grid: a nested list of lists

    Returns: An integer representing the sum of values in pixel_grid
    """
    # Write your code for Problem 2 here!


# ~~~ End Problem 2 ~~~

assert sum_grid([[5, 2, 3], [1, 5, 4]]) == 20
assert sum_grid([[1, 3], [3, 4], [15, 16], [9, 2]]) == 53
assert sum_grid([[100, 50]]) == 150
assert sum_grid([[35]]) == 35
assert sum_grid([[10, 3], [20, 7], [30, 1], [40, -4]]) == 107
assert sum_grid([[10], [20], [30], [40]]) == 100
assert sum_grid([[1, 2, 3, 4], [8, 8, 6, 9]]) == 41


# ~~~ Begin Problem 3 ~~~
def first_letter(filename):
    """
    Given a file name, return a string containing the first letter of each line in the file.

    Arguments:
        filename: a string representing a filename

    Returns: a string made up of the first letter of each line of the file in order
    """
    # Write your code for Problem 3 here!


# ~~~ End Problem 3 ~~~

assert first_letter("data/numbers.txt") == "ottffs"
assert first_letter("data/animals.txt") == "cspgcdchrm"
