# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 3

# ~~~ Begin Problem 1 ~~~
"""
Write a function largest_sum(nums1, nums2) that takes two lists of integers and returns the largest
sum possible using one number from each list. You may assume that each list contains at least one
number.
"""
# Write your code for Problem 1 here!


# ~~~ End Problem 1 ~~~

assert largest_sum([1, 5, 3], [4, 2, 6]) == 11
assert largest_sum([-5, -2, -10], [-4, -1, -8]) == -3
assert largest_sum([-10, 5, 0], [-2, 8, -5]) == 13
assert largest_sum([7], [3]) == 10
assert largest_sum([4, 4, 1], [9, 2, 9, 0, -1]) == 13
assert largest_sum([7], [3, 2]) == 10

# ~~~ Begin Problem 2 ~~~
"""
Write a function clean(str), that takes a string and returns a new string containing only the
lowercase alphabetical letters from the original string. For example,

    clean("Hello!") should return "ello"
    clean("123 Kevin   ") should return "evin"
"""
# Write your code for Problem 2 here!


# ~~~ End Problem 2 ~~~

assert clean("Hello!") == "ello"
assert clean("123 Kevin   ") == "evin"
assert clean("123!?ABC") == ""
assert clean("helloworld") == "helloworld"
assert clean("     ") == ""
assert clean("") == ""
assert clean("a") == "a"
assert clean("Z") == ""
assert clean("a1B2c!D e") == "ace"

# ~~~ Begin Problem 3 ~~~
"""
Write a function word_list(words) that takes a list of words and returns a new list containing only
words whose cleaned versions are the same as their original version. For example,

    word_list(["AWEsome!", "helloworld", "python", "123"]) should return ["helloworld", "python"]

You may use the previously created function for this problem.
"""
# Write your code for Problem 3 here!


# ~~~ End Problem 3 ~~~

assert word_list(["AWEsome!", "helloworld", "python", "123"]) == ["helloworld", "python"]
assert word_list(["Hello World"]) == []
assert word_list(["Python", ""]) == [""]
assert word_list([]) == []
assert word_list(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
assert word_list(["123", "ABC", "hello!", "   "]) == []
assert word_list(["a", "B", "c", "1"]) == ["a", "c"]
original = ["keep", "Remove"]
result = word_list(original)
assert original == ["keep", "Remove"], "Return a new list instead of modifying the original!"
