# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 6

# ~~~ Begin Problem 1 ~~~
from math import sqrt


def hypotenuses(sides):
    """
    Given a list of tuples, where each tuple represents the two legs of a right triangle, return a
    list of the lengths of each triangle's hypotenuse.

    Arguments:
        sides: a list of 2-item tuples representing the two perpendicular legs of a right triangle

    Returns: a list of the lengths of the triangle's hypotenuse from the given sides
    """
    # Write your code for Problem 1 here!
    # Call sqrt(a**2 + b**2) to compute the hypotenuse length given the two legs a and b


# ~~~ End Problem 1 ~~~

assert hypotenuses([]) == []
assert hypotenuses([(3, 4), (6, 8), (5, 12)]) == [5.0, 10.0, 13.0]
assert hypotenuses([(9, 12)]) == [15.0]


# ~~~ Begin Problem 2 ~~~
def highest_score(scores):
    """
    Given a dictionary where the keys are player names and the values are their scores, return a
    tuple containing the highest scoring player's name and their score. You can assume that there
    is at least one player represented in the dictionary.

    In the case of a tie, return the player who was first encountered.

    Arguments:
        scores: a dictionary with string keys representing player names
                and integer values representing their scores

    Returns: a tuple in the form of (name, score)
    """
    # Write your code for Problem 2 here!


# ~~~ End Problem 2 ~~~

assert highest_score({'Kevin': 30712, 'Arona': 87320, 'Arpan': 19927}) == ('Arona', 87320)
assert highest_score({'Sara': 73612}) == ('Sara', 73612)


# ~~~ Begin Problem 3 ~~~
def modify(list_a, list_b, target):
    """
    Adds the contents of list_b to the end of list_a and removes the first occurence of target from
    the resulting list_a. Finally, sorts the resulting list. Modifies list_a in-place.

    Assumes that target always exists in at least one of the provided lists.

    Arguments:
        list_a: a list of integers to modify
        list_b: a list of integers
        target: an integer that should be removed from the resulting list

    Returns: nothing
    """
    # Write your code for Problem 3 here!


# ~~~ End Problem 3 ~~~

test_list = [3, 8, 2]
assert modify(test_list, [7, 1, 9], 2) is None
assert test_list == [1, 3, 7, 8, 9]
