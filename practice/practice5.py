# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 5

# ~~~ Begin Problem 1 ~~~
def num_lower_val(max_val, input_dict):
    '''
    Return the number of values in the dictionary that are lower than the
    given int. All values in the dictionary will be integers.

    Arguments:
        max_val: an integer
        input_dict: a dictionary with int values

    Returns: An integer representing the number of key-value pairs in the
    dictionary where the value is smaller than max_val
    '''
    # your solution code should start here
    


# ~~~ End Problem 1 ~~~

assert num_lower_val(5, {"one": 1, "two": 2, "three": 3}) == 3
assert num_lower_val(-5, {"one": 1, "two": 2, "three": 3}) == 0
assert num_lower_val(5, {"five": 5, "two": 2, "three": 3}) == 2
assert num_lower_val(21, {"panda": 20}) == 1
assert num_lower_val(18, {"panda": 20}) == 0
assert num_lower_val(2, {10: 1, 11: 1, 5: 1, 99: 1}) == 4
assert num_lower_val(6, {10: 7, 6: 25, 3: 1, 2: 2, 3: 1}) == 2
assert num_lower_val(1000, {1: 1001, 2: 999, 3: 1002}) == 1


# ~~~ Begin Problem 2 ~~~
def duck_dict(duck_names, duck_ages):
    '''
    Given a list of strings representing the names of ducks and
    a list of integers representing their ages, construct a dictionary
    containing a mapping of each duck's name to its corresponding age

    Arguments:
        duck_names: A list of strings
        duck_age: A list of ints where the int at index i
            represents the age of the duck from
            duck_names at index i

    Returns: An dictionary that maps the name of the ducks to their ages
    '''
    # your solution code should start here
    


# ~~~ End Problem 2 ~~~

assert duck_dict(["Bri"], [5]) == {"Bri": 5}
assert duck_dict(["Bri", "Kim"], [5, 6]) == {"Bri": 5, "Kim": 6}
assert duck_dict(["A", "B", "C"], [5, 8, 1]) == {"A": 5, "B": 8, "C": 1}
assert duck_dict(["A", "B", "C"], [1, 1, 1]) == {"A": 1, "B": 1, "C": 1}
assert duck_dict(["A1", "A2", "A3"],
                 [100, 15, 55]) == {"A1": 100, "A2": 15, "A3": 55}


# ~~~ Begin Problem 3 ~~~
def word_counts(filename):
    '''
    Given a file name, construct and return a dictionary where each key is an integer representing
    a line number and the value is the number of words on that line. For example, a file containing
    3 words on the first line, 7 words on the second, and 9 words on the third would return
    {1: 3, 2: 7, 3: 9}. The first character on each line of the file is the line number, and should
    not be included in the word count for that line. For reference, see the files used in the
    assert statements below in the 'data' folder.

    Arguments:
        filename: a string representing a filename

    Returns: a dictionary representing the number of words on each line of the given file
    '''
    # your solution code should start here
    


# ~~~ End Problem 3 ~~~

assert word_counts("data/story.txt") == {1: 3, 2: 7, 3: 9}
assert word_counts("data/alphabet.txt") == {1: 4, 2: 0, 3: 1, 4: 2, 5: 2, 6: 0}
