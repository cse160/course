# Name: ...
# CSE 160
# Spring 2026
# Programming Practice 1


# ~~~ Begin Problem 1 ~~~
"""
Print the following three lines of output, paying close attention to spacing and punctuation:

Welcome to CSE 160!
Data Programming
Quarter: 26sp

Note: You *must* use the variable named quarter when printing the final line of output. Your code
should work even if the value of quarter is changed!
"""

quarter = "26sp"

# Write your code for Problem 1 here!



# ~~~ End Problem 1 ~~~
print("~~~~~~~~~~~")

# ~~~ Begin Problem 2 ~~~
"""
Fill-in the missing conditions below to check that rating is a number between 0 and 10.

- If the number is above 10, print "Error: rating above 10!".
- If the number is below 0, print "Error: rating below 0!".
- Otherwise, print "Success: valid rating entered!".

Replace the ... (ellipsis) in the code below.
"""

# Write your code for Problem 2 here!
rating = -1
if ...:
    print("Error: rating above 10!")
elif ...:
    print("Error: rating below 0!")
else:
    print("Success: valid rating entered!")


# ~~~ End Problem 2 ~~~
print("~~~~~~~~~~~")

# ~~~ Begin Problem 3 ~~~
"""
Given an variable called num_times with an integer value, write a for loop that will count from 1
to num_times, printing out each number as it is counted.

Also define a variable named total_sum, which should keep track of the sum of the counted numbers
seen so far. After the loop finishes, total_sum should be equal to the sum of all integers from 1
to num_times.

REMEMBER: Your code should work even if we change the value of num_times !

== EXAMPLE #1 ==
num_times = 2

OUTPUT:
1
2

== EXAMPLE #2 ==
num_times = 4

OUTPUT:
1
2
3
4

"""

num_times = 5

# Write your code for Problem 3 here!



# DON'T EDIT THE CODE BELOW
assert "total_sum" in locals(), "Make sure to define a variable called total_sum"
assert total_sum > num_times, "Make sure total_sum sums together all of the counted numbers"

# ~~~ End Problem 3 ~~~
