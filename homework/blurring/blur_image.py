# Name ..
# CSE 160
# Blurring
# Description:

import os
from utils import read_image, write_image, parse_args, csv_line_to_pixels, write_grid  # noqa: F401


def get_pixel_at(pixel_grid, i, j):
    """

    >>> test_grid = [
    ...     [1, 2, 3, 4, 5, 6],
    ...     [0, 2, 4, 6, 8, 10],
    ...     [3, 4, 5, 6, 7, 8],
    ... ]
    >>> get_pixel_at(test_grid, 0, 0)
    1
    >>> get_pixel_at(test_grid, -1, 0)
    0
    >>> get_pixel_at(test_grid, 0, -1)
    0
    >>> get_pixel_at(test_grid, -1, -1)
    0
    >>> get_pixel_at(test_grid, 2, 5)
    8
    >>> get_pixel_at(test_grid, 3, 5)
    0
    >>> get_pixel_at(test_grid, 2, 6)
    0
    >>> get_pixel_at(test_grid, 3, 6)
    0
    >>> get_pixel_at(test_grid, 1, 3)
    6
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def average_of_surrounding(pixel_grid, i, j):
    """

    >>> test_grid = [
    ...     [1, 2, 3, 4, 5, 6],
    ...     [0, 2, 4, 6, 8, 10],
    ...     [3, 4, 5, 6, 7, 8],
    ... ]
    >>> average_of_surrounding(test_grid, 0, 0)
    0
    >>> average_of_surrounding(test_grid, 2, 5)
    3
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def blur(pixel_grid):
    """

    >>> test_grid = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ... ]
    >>> blur(test_grid)
    [[1, 2, 1], [3, 5, 3], [2, 4, 3]]
    >>> test_grid == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    True
    >>> test_grid = [
    ...     [1,  1,  1,  1,  1,  1],
    ...     [1,  1,  1,  1,  1,  1],
    ...     [1,  1,  1,  1,  1,  1],
    ...     [1,  1,  1,  1,  1,  1],
    ... ]
    >>> blur(test_grid)
    [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def read_grid(file_path):
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


input_file = parse_args()
if not input_file:
    import doctest
    doctest.testmod()
else:
    print("Welcome to the CSE 160 Image Blurring program!")

    path_without_extension, extension = os.path.splitext(input_file)

    if extension == ".csv":
        input_grid = read_grid(input_file)
    else:
        input_grid = read_image(input_file)

        if input_grid is None:
            exit()

    # Blur the image
    ...  # REPLACE THIS LINE WITH YOUR CODE TO CALL THE BLUR FUNCTION

    # input_filename = os.path.basename(path_without_extension)
    # output_image_filename = input_filename + '_blurry.png'
    # output_grid_filename = input_filename + '_blurry_grid.csv'

    # Write the blurred image and grid to files
    ...  # REPLACE THIS LINE WITH YOUR CODE TO WRITE THE BLURRED IMAGE
    ...  # REPLACE THIS LINE WITH YOUR CODE TO WRITE THE BLURRED GRID

    print("Program done.")


###
# Collaboration and Sources
###

# ... Write your answer here, as comments (lines starting with "#").
