# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 2

# ~~~ Begin Problem 1 ~~~
"""
Given a list of values and a target value, iterate through each value in the list and print "Target
found!" if that value matches the target. Each time the target is found, increment matches by 1.

It is possible for the target to appear multiple times in the list.
"""
values = [1, 3, 4, 7, 9, 4, 13, 2, 17]
target = 4

matches = 0

# Write your code for Problem 1 here!



# ~~~ End Problem 1 ~~~
print("~~~~~~~~~~~")

assert matches == 2, "'Target found!' should be printed twice."

# ~~~ Begin Problem 2 ~~~
"""
Given two lists of names, print every possible pair combination of one name from the names_A list
and another name from the names_B list. Each time a pair is printed, increment pairs_printed by 1.

Pairs should be printed in the form "___ and ___" where the blanks are two names. For example:

    Kevin and Suhas
"""
names_A = ["Kevin", "Brianna", "Katie"]
names_B = ["Suhas", "Tiernan", "Arona"]

pairs_printed = 0

# Write your code for Problem 2 here!



# ~~~ End Problem 2 ~~~
print("~~~~~~~~~~~")

assert pairs_printed == 9, "You should print 9 lines for this problem."

# ~~~ Begin Problem 3 ~~~
"""
Write a function letter_count(str, letter) that returns the number of times letter appears in str.
letter is case-sensitive.

Arguments:
    str: an String
    letter: a char

Returns: An integer representing the count of letter in str.

Examples:
- letter_count("hi", "h") returns 1
- letter_count("festival", "q") returns 0
- letter_count("astronomy", "o") returns 2
"""

# Write your code for Problem 3 here!



# ~~~ End Problem 3 ~~~
print("~~~~~~~~~~~")

assert letter_count("python", "y") == 1
assert letter_count("banana", "n") == 2
assert letter_count("banana", "a") == 3
assert letter_count("bookkeeper", "k") == 2
assert letter_count("flowers", "z") == 0
assert letter_count("7777 77", "7") == 6
assert letter_count("", " ") == 0
