# Practical

In this homework, we will write a program that prints square roots, fractions, triangular numbers, factorials, and the approximate value of $e$.

By the end of this assignment, students will feel more comfortable:

1. Writing Python code using variables and loops to solve arithmetic problems.
1. Running Python programs using the interactive Python console in JupyterHub.
1. Printing results to match a specification, including whitespace.

> [!important]
> This homework assignment asks you to print answers to 6 problems. **In between each problem, print a single blank line.**

## Problem 1: Roots

Write code that calls `math.sqrt` to print the roots of the quadratic equation: $$3x^2 - 5.86x + 2.5408 = 0$$

You will need to use the [quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation) to solve for the roots: $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

> [!tip]
> If you need to use a particular value more than once, be sure to store it in a variable!

Print the two possible values for $x$ such that they replace the `____` (blanks) in the template below **in ascending order**: the smaller root should appear before the larger root.

    Problem 1 solution follows:
    Root 1: ____
    Root 2: ____

## Problem 2: Reciprocals

Write code that uses a `for` loop to print the fractions: $$\frac{1}{2}, \frac{1}{3}, ..., \frac{1}{10}$$

As in problem 1, print values such that they replace the `____` (blanks) in the template below.

    Problem 2 solution follows:
    1/2: ____
    1/3: ____
    1/4: ____
    1/5: ____
    1/6: ____
    1/7: ____
    1/8: ____
    1/9: ____
    1/10: ____

## Problem 3: Triangular numbers

Write code that prints the 10th [triangular number](https://en.wikipedia.org/wiki/Triangular_number) in two ways:

1. Using a `for` loop over a [`range`](http://docs.python.org/3.13/library/functions.html#func-range) to add the integers from 1 through 10.
1. Using a mathematical formula: $$\frac{N(N + 1)}{2}$$

The `main.py` file includes some sample code that to help you get started. Replace the `...` (ellipsis) placeholders with your own code. The code should calculate the 11th, 12th, etc. triangular number by changing the variable `n` for any integer greater than 0.

```{literalinclude} main.py
:start-at: n = 10
:end-at: print("Triangular number", n, "via formula:", n * (n + 1) / 2)
```
As in problem 1 and 2, print values such that they replace the `____` (blanks) in the template.

    Problem 3 solution follows:
    Triangular number 10 via loop: ____
    Triangular number 10 via formula: ____

## Problem 4: Factorial

Write code that uses a `for` loop to print $10!$, the [factorial](https://en.wikipedia.org/wiki/Factorial) of 10. The factorial of a number, $n$, is given by $1 \times 2 \times 3 \times \cdots \times n$

As in problem 3, the code should correctly calculate any factorial just by changing a variable.

    Problem 4 solution follows:
    10!: ____

## Problem 5: Multiple factorials

Write code that uses a **nested** `for` loop to print the first 10 factorials in descending order: $10!, 9!, ..., 1!$

The first line of code should begin by assigning a variable `num_lines` to `10`. Then the rest of the code should print the following output.

    Problem 5 solution follows:
    10!: 3628800
    9!: 362880
    8!: 40320
    7!: 5040
    6!: 720
    5!: 120
    4!: 24
    3!: 6
    2!: 2
    1!: 1

As in problems 3 and 4, the code should work for any number just by changing `num_lines`.

## Problem 6: Approximating $e$

Write code that uses a **nested** `for` loop to compute the value $$1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + ... + \frac{1}{10!}$$

    Problem 6 solution follows:
    e: ____

> [!tip]
> Start by copy-pasting your code for problem 5 into the space for problem 6. Rather than printing the factorials, we can add their reciprocals to a running total before printing the final result. Where in the code should we add 1 to the result?

As in problems 3 through 5, the code should work for any number of fractions to add.

## Code quality

Run our linter (automated code style checker) in the Python console with the expression `!flake8`. Edit the file and save your changes after addressing all reported issues. A successful `!flake8` run will print nothing when there are no linting issues to report.

```ipython
!flake8
```

Then, review our [style guide](../../style-guide.md), paying particular attention to:

- [Variable names](../../style-guide.md/#variable-names)
- Whitespace
  - [Indentation](../../style-guide.md/#indentation)
  - [Blank lines](../../style-guide.md/#blank-lines)
  - [Between operators](../../style-guide.md/#between-operators)
- [Line length](../../style-guide.md/#line-length)
- Program design
  - [Fit and finish](../../style-guide.md#fit-and-finish)

## Collaboration

If you discuss an assignment with one or more classmates, **you must specify with whom you collaborated in a comment at the bottom of your submission**. You may discuss with as many classmates as you like, but you must cite all of them in your work. Note that you may not collaborate in a way that is prohibited, even if you cite the collaboration.

**At the bottom of both your `dna_analysis.py` and `answers.txt` files**, state which students or other people (besides the course staff) helped you with the assignment, or that no one did.

## Submission

See the `output.txt` file for a complete example of the expected output with `____` (blanks) instead of actual values. To help you compare, copy-paste the contents of the expected output into the left pane of [Diffchecker](https://www.diffchecker.com/) and your output into the right pane.

To submit: from JupyterHub, open your `main.py` file, select  **File | Download**, and submit your downloaded `main.py` file on Gradescope under the assignment **Homework: Practical**.
