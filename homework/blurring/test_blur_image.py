# Test program for blur_image.py

import copy
import os
from io import StringIO
from blur_image import get_pixel_at, average_of_surrounding, blur, csv_line_to_pixels, read_grid


def test_get_pixel_at():
    """Tests for get_pixel_at."""

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8],
    ]

    tests = {
        (0, 0): 1,
        (-1, 0): 0,
        (0, -1): 0,
        (-1, -1): 0,
        (2, 5): 8,
        (3, 5): 0,
        (2, 6): 0,
        (3, 6): 0,
        (1, 3): 6,
    }

    try:
        for (i, j), expected in tests.items():
            pixel = get_pixel_at(test_grid, i, j)
            assert pixel == expected, (
                "[get_pixel_at] Test Error:\n"
                "    Expected pixel value: " + str(expected) + "\n"
                "    Actual pixel value: " + str(pixel)
            )
    except AssertionError as e:
        # Print a user-friendly error message (i.e., sans traceback)
        print(e)
        exit(1)

    print("All tests passed for get_pixel_at!")


def test_average_of_surrounding():
    """Tests for average_of_surrounding."""

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8],
    ]

    tests = {
        (0, 0): 0,
        (2, 5): 3,
    }

    try:
        for (i, j), expected in tests.items():
            pixel = average_of_surrounding(test_grid, i, j)
            assert pixel == expected, (
                "[average_of_surrounding] Test Error:\n"
                "    Expected average value: " + str(expected) + "\n"
                "    Actual average value: " + str(pixel)
            )
    except AssertionError as e:
        # Print a user-friendly error message (i.e., sans traceback)
        print(e)
        exit(1)

    print("All tests passed for average_of_surrounding!")


def test_blur():
    """Tests for blur."""

    test_grid = [
        [1,    2,    3],
        [4,    5,    6],
        [7,    8,    9],
    ]
    test_grid_copy = copy.deepcopy(test_grid)

    expected = [
        [1,    2,    1],
        [3,    5,    3],
        [2,    4,    3],
    ]
    blurred_grid = blur(test_grid)

    try:
        assert type(blurred_grid) is list, (
            "[blur] Test Error:\n"
            "    Expected blur to return a list\n"
            "    Actual: " + str(type(blurred_grid))
        )

        assert test_grid == test_grid_copy, (
            "[blur] Test Error:\n"
            "    Expected blur to not modify the original grid\n"
            "    Original grid: " + str(test_grid_copy) + "\n"
            "    Actual: " + str(test_grid)
        )

        assert blurred_grid == expected, (
            "[blur] Test Error:\n"
            "    Expected: " + str(expected) + "\n"
            "    Actual: " + str(blurred_grid)
        )

        test_grid = [
            [1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1],
        ]

        expected = [
            [0,  0,  0,  0,  0,  0],
            [0,  1,  1,  1,  1,  0],
            [0,  1,  1,  1,  1,  0],
            [0,  0,  0,  0,  0,  0],
        ]

        blurred_grid = blur(test_grid)
        assert blurred_grid == expected, (
            "[blur] Test Error:\n"
            "    Expected: " + str(expected) + "\n"
            "    Actual: " + str(blurred_grid)
        )
    except AssertionError as e:
        # Print a user-friendly error message (i.e., sans traceback)
        print(e)
        exit(1)

    print("All tests passed for blur!")


def test_csv_line_to_pixels():
    """Tests for csv_line_to_pixel."""

    tests = {
        # Basic positive integers, no spaces
        "1,2,3,4,5,6": [1, 2, 3, 4, 5, 6],

        # Still positive, but varying spacing
        "  6,        7, 8,9": [6, 7, 8, 9],

        # Mix of negative, positive, and zero
        "0,-1,2,3,-4,5": [0, -1, 2, 3, -4, 5],

        # Mixed-length numbers
        "0,100,2000,30000,400000": [0, 100, 2000, 30000, 400000],
    }

    try:
        for test_line, expected in tests.items():
            pixels = csv_line_to_pixels(test_line)
            assert pixels == expected, (
                "[csv_line_to_pixel] Test Error:\n"
                "    Expected pixel list: " + str(expected) + "\n"
                "    Actual pixel list: " + str(pixels)
            )
    except AssertionError as e:
        # Print a user-friendly error message (i.e., sans traceback)
        print(e)
        exit(1)

    print("All tests passed for csv_line_to_pixels!")


def test_read_grid():
    def stringio_to_fd(s):
        r, w = os.pipe()
        os.write(w, s.getvalue().encode())
        os.close(w)
        return r

    input_data = StringIO()
    input_data.write("0, 0, 0, 0\n")
    input_data.write("0, 0, 0, 0\n")
    input_data.write("0, 0, 0, 0\n")
    input_data.write("0, 0, 0, 0\n")

    expected_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    input_fd = stringio_to_fd(input_data)

    actual_grid = read_grid(input_fd)
    try:
        assert actual_grid == expected_grid, (
            "[read_grid] Test Error:\n"
            "    Expected grid: " + str(expected_grid) + "\n"
            "    Actual grid: " + str(actual_grid)
        )
    except AssertionError as e:
        # Print a user-friendly error message (i.e., sans traceback)
        print(e)
        exit(1)

    print("All tests passed for read_grid!")


if __name__ == "__main__":
    test_get_pixel_at()
    test_average_of_surrounding()
    test_blur()
    test_csv_line_to_pixels()
    test_read_grid()
    print("All tests passed!")
