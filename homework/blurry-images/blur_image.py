# Name ..
# CSE 160
# Homework 3: Image Blurring
# Description:

import os
from utils import (read_image, write_image, parse_args,
                   csv_line_to_pixels, write_grid)


def get_pixel_at(pixel_grid, i, j):
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def average_of_surrounding(pixel_grid, i, j):
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def blur(pixel_grid):
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def read_grid(file_path):
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def main():
    input_file = parse_args()

    path_without_extension, extension = os.path.splitext(input_file)
    input_filename = os.path.basename(path_without_extension)

    if extension == ".csv":
        input_grid = read_grid(input_file)
    else:
        input_grid = read_image(input_file)

        if input_grid is None:
            exit()

    # Blur the image
    ...  # REPLACE THIS LINE WITH YOUR CODE TO CALL THE BLUR FUNCTION

    output_image_filename = input_filename + '_blurry.png'
    output_grid_filename = input_filename + '_blurry_grid.txt'

    # Write the blurred image and grid to files
    ...  # REPLACE THIS LINE WITH YOUR CODE TO WRITE THE BLURRED IMAGE
    ...  # REPLACE THIS LINE WITH YOUR CODE TO WRITE THE BLURRED GRID


if __name__ == "__main__":
    print("Welcome to the CSE 160 Image Blurring program!")
    main()
    print("Program done.")


###
# Collaboration and Sources
###

# ... Write your answer here, as comments (lines starting with "#").
