# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 8

# ~~~ Begin Problem 1 ~~~
import csv


def most_populated_city(filename):
    """
    Reads a CSV file containing a header row with at least two columns: city and population. Assume
    the file has at least one city and populations are valid integers.

    Use csv.DictReader to read the file. Return the name of the city with the highest population.

    Arguments:
        filename: a string representing the path to a CSV file

    Returns: a string representing the name of the city with the highest population
    """
    # Write your code for Problem 1 here!


# ~~~ End Problem 1 ~~~

assert most_populated_city("data/cities.csv") == "Los Angeles"


# ~~~ Begin Problem 2 ~~~
from collections import defaultdict


def group_by_length(words):
    """
    Use collections.defaultdict to create and return a dictionary where each key is an integer
    representing a string length, and the corresponding value is a list of all words from the input
    list that have that exact length.

    Arguments:
        words: a list of strings

    Returns: a dictionary mapping an integer length to a list of strings
    """
    # Write your code for Problem 2 here!


# ~~~ End Problem 2 ~~~

assert group_by_length(["a", "at", "to", "cat", "dog", "elephant"]) == {
    1: ["a"],
    2: ["at", "to"],
    3: ["cat", "dog"],
    8: ["elephant"]
}
assert group_by_length([]) == {}
assert group_by_length(["hello", "world"]) == {5: ["hello", "world"]}


# ~~~ Begin Problem 3 ~~~
from dataclasses import dataclass


# Define a dataclass `Book` with three fields: `title` (str), `author` (str), and `pages` (int).


def get_long_books(books):
    """
    Given a list of Book objects, return a list of the titles of books that have 300 or more pages.

    Arguments:
        books: a list of Book objects

    Returns: a list of strings representing the titles of books with 300 or more pages
    """
    # Write your code for Problem 3 here!


# ~~~ End Problem 3 ~~~

books = [
    Book("The Hobbit", "J.R.R. Tolkien", 310),
    Book("1984", "George Orwell", 328),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 180),
    Book("Fahrenheit 451", "Ray Bradbury", 249)
]
assert get_long_books(books) == ["The Hobbit", "1984"]
assert get_long_books([]) == []
assert get_long_books([Book("Dune", "Frank Herbert", 896)]) == ["Dune"]
