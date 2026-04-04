# DNA Analysis

In this homework, we will write a program to analyze data in a real-world scenario.

By the end of this assignment, students will feel more comfortable:

1. Writing Python code using loops, conditionals, functions, and string manipulation.
1. Running Python programs with command line arguments from the JupyterHub console.
1. Interpreting program specifications involving a complicated real-world scenario.

## Background

DNA is made up of a sequence of nucleotides. Each nucleotide is adenine (A), cytosine (C), guanine (G), or thymine (T). You will use, modify, and extend a program to compute the **GC content of DNA data**: the percentage of nucleotides that are either G or C. What can we do with [GC content](http://en.wikipedia.org/wiki/GC-content)?

- GC content can identify the location of genes within DNA, and can identify types of genes. Genes tend to have higher GC content than other parts of the DNA. Genes with longer coding regions have even higher GC content.
- Regions of DNA with higher GC content require higher temperatures for certain chemical reactions, such as when copying/duplicating the DNA.
- GC content can be used in determining classification of species.

Here are the first eight lines of one of our sample DNA data files:

```{literalinclude} data/sample_6.fastq
:lines: 1-8
```

**The nucleotide data is in the second line, the sixth line, the tenth line, etc.** To calculate GC content, you will be looking for the percentage of letters appearing on these lines that are G or C. Your program will not use the rest of the file, which provides information about the sequencer and the sequencing process that created the nucleotide data.

> [!important]
> The code we've provided already reads the appropriate lines of the file into a string for your program to process. However, knowing this file format will be helpful if you need to read the data files later while debugging your program.

## Command line arguments

For this homework assignment, we will specify a **command line argument** when we run our Python file. This acts as an input to our Python program, allowing us to specify the name of the data file we want to read from.

> [!warning]
> Do not modify any code in `utils.py` or lines 16, 51, or 54 of `dna_analysis.py`.

When writing code that analyzes data, it is important to test your program so that you can be confident the output is correct. One way to do this is by comparing the output of your code to output produced in some other way, such as by hand or by a different program. We have provided a small test file for this purpose: `test-small.fastq`. This file is small enough that you can easily read it and calculate the GC content by hand. Then, you can use this file as input to your program to verify that it provides the correct answer for this file.

```{literalinclude} data/test-small.fastq
```

From an attached Python console, run `dna_analysis.py` on this sample data file by entering the following command in the terminal, which specifies the **relative file path** to `test-small.fastq`:

```ipython
%run dna_analysis.py data/test-small.fastq
```

The program should print:

    GC-content: 0.3

## Running test files

Now, try running the DNA analysis on each of the 6 other sample data files provided by executing 6 commands such as:

```ipython
%run dna_analysis.py data/sample_1.fastq
```

> [!tip]
> While your cursor is in the console, the <kbd>↑</kbd> (up arrow) key will retrieve the last-run code.

Run your program on different data files by changing `sample_1.fastq` to a different sample data file name in the command above. It might take a minute or so to run since these are large data files.

We have provided expected output files for the other `test-*.fastq` files in the `expected_output` directory:

> [!warning]
> If your GC content does not match the expected output exactly, that's OK for now. You won't get the exact answer until you finish problem 4.

## Formatting

By the end of the assignment, `dna_analysis.py` must produce output of the exact form:

    GC-content: ____
    AT-content: ____
    G count: ____
    C count: ____
    A count: ____
    T count: ____
    Sum of G+C+A+T counts: ____
    Total count: ____
    Length of nucleotides: ____
    AT/GC Ratio: ____
    GC Classification: ____
    Is suitable for nanotech: ____

## Problem 1: Remove some lines

Run `dna_analysis.py` on `test-small.fastq` like you did for Problem 0. Be sure to take note of what output appears in the terminal. Then comment out the line `gc_count = 0` by putting a `#` at the start of the line. Save the file and then run it again in the terminal. **In `answers.txt`, explain what happened, and why it happened.**

Now, restore the line to its original state by removing the `#` that you added. What would happen if you commented out the line `nucleotides = filename_to_string(file_name)` instead? **Explain what happens and why in `answers.txt`.**

## Problem 2: Compute AT content

Modify your program so that, in addition to computing and printing the GC ratio, it also computes and prints the **AT content**: the percentage of nucleotides that are A or T. There are two ways to compute the AT content:

1. Copy the existing loop that examines each nucleotide and modify it. You will now have two loops, one of which computes the GC count and one of which computes the AT count.
1. Add more statements into the existing loop, so that one loop computes both the GC count and the AT count.

You may use whichever approach you prefer. Check your work by manually computing the AT content for `test-small.fastq` before comparing it to the output of running your program on `test-small.fastq`. **Run your program on `sample_1.fastq`. Copy and paste the relevant line of output into `answers.txt`.**

## Problem 3: Count nucleotides

> [!tip]
> Feel free to modify the code we have given you if another structure of `if` statements makes more sense to you. Avoid looping through the data more times than you need to as this could cause your code to run very slowly.

Modify your program so that it also computes and prints the number of A nucleotides, the number of T nucleotides, the number of G nucleotides, and the number of C nucleotides. When doing this, **add at most one extra loop to your program**. You can solve this part without adding any new loops at all by reusing an existing loop.

Check your work by manually computing the results for file `test-small.fastq` before comparing them to the output of running your program on `test-small.fastq`. **Run your program on `sample_1.fastq`. Copy and paste the relevant lines of output into `answers.txt` (the lines that indicate the G count, C count, A count, and T count).**

## Problem 4: Check the data

> [!important]
> This problem illustrates a common programming challenge: unexpected output. Discrepancies usually stem from either a **logic bug** in the code or an **incorrect assumption** about the data structure. To identify the root cause, you should isolate the issue by testing small snippets of code against specific portions of your data.

Modify `dna_analysis.py` so that it will calculate and print the following variables:

- `sum_counts`: the sum of the A count, the C count, the G count, and the T count
- `total_count`: the total number of nucleotides
- `len_nuc`: the length of the nucleotides string variable using `len(nucleotides)`.

Then run `dna_analysis.py` on each of the 11 `.fastq` files provided. As you run these files, you'll notice that at least one of these quantities will be different from the other two for at least one `.fastq` file. **In `answers.txt`, state which `.fastq` file(s) and which quantities produce different results. Also write a short paragraph that explains why these differ.**

If all the three quantities you measured are the same, then it would not matter which one you used in the denominator when computing the GC content. However, you saw that the three quantities are not all the same. **In answers.txt, state which of these quantities should be used in the denominator and which should not, and why.**

If your program incorrectly computed the GC content, which should be equal to $\frac{G+C}{A+C+G+T}$ then state that fact in `answers.txt`. Go back and correct your program, and also **update any incorrect answers elsewhere in `answers.txt`. It is fine to change the code we provided you if needed.**

> [!note]
> If you are unsure if you are calculating things correctly, now would be a good time to validate your `dna_analysis.py` program's output against the `expected_output` using [Diffchecker](https://www.diffchecker.com/). Double check trailing spaces! Your output will be missing the last two lines until you complete the following problems. But the GC content, AT content, and individual counts should be correct now.

## Problem 5: Compute the AT/GC ratio

Sometimes, biologists use the **AT/GC ratio**, which is defined as $\frac{A + T}{G + C}$. Modify your program so that it also computes the AT/GC ratio. Check your work by manually computing the results for file `test-small.fastq`. Compare them to the output of running your program on `test-small.fastq`.

**Run your program on `sample_1.fastq`. Copy and paste the relevant line(s) of output into `answers.txt` on the line that indicates the AT/GC ratio.**

## Problem 6: Categorize organisms

GC content can be used to categorize microorganisms. Complete the `classify` function, which should return a string `"high"`, `"medium"`, or `"low"` based on the organism's GC content:

- `"high"` for GC content strictly above 58%.
- `"moderate"` for GC content between 58% (inclusive) and 35% (inclusive).
- `"low"` for GC content strictly below 35%.

Biologists can use GC content for classifying species, for determining the melting temperature of DNA, for identifying suitability for DNA nanotechnology, etc. Here are some examples:

- The GC content of Streptomyces coelicolor A3(2) is 72%: `"high"`.
- The GC content of Yeast (Saccharomyces cerevisiae) is 38%: `"moderate"`.
- The GC content of Thale Cress (Arabidopsis thaliana) is 35%: `"moderate"`.
- The GC content of Plasmodium falciparum is 20%: `"low"`.

Test that your program works on some data files with known outputs. The `test-small.fastq` file has low GC content. We have provided four other test files whose names explain their GC content: `test-moderate-gc-1.fastq`, `test-moderate-gc-2.fastq`, `test-high-gc-1.fastq`, `test-high-gc-2.fastq`.

The `classify` function appears near the top of `dna_analysis.py`, just before where the main program begins. Replace the assignment statement at the top of the function.

```{literalinclude} dna_analysis.py
:start-at: def classify(gc_content):
:end-at: return classification
```

**Once you have filled in the body of the `classify` function, call the function from your main program in the appropriate place and use the string it returns to print out a message that matches what is expected.** For example, ensure your output for `test-moderate-gc-1.fastq` matches `test-moderate-gc-1-expected.txt` exactly using [Diffchecker](https://diffchecker.com/).

After your program works for all the test files, run it on `sample_1.fastq`. **Copy and paste just the relevant line of output from your program into `answers.txt`** (the line that indicates the GC classification).

## Problem 6a: Nanotech

Modify the `nano_suitable` function to return whether or not the GC content is suitable for use in DNA nanotechnology. The decision should be made as follows:

- If the GC content is greater than 50% and less than 60%, `nano_suitable` should return `True`.
- Otherwise, `nano_suitable` should return `False`.

The `nano_suitable` function appears underneath the `classify` function, just before where the main program begins.

```{literalinclude} dna_analysis.py
:start-at: def nano_suitable(gc_content):
:end-at: return True
```

As with `classify`, check the `expected_output` files with [Diffchecker](https://diffchecker.com/).

## Code quality

Run our linter (automated code style checker) in the Python console with the expression `!flake8`. Edit the file and save your changes after addressing all reported issues. A successful `!flake8` run will print nothing when there are no linting issues to report.

```ipython
!flake8
```

Then, review our [style guide](../../style-guide.md), paying particular attention to:

- [Variable names](../../style-guide.md#variable-names)
- Whitespace
  - [Indentation](../../style-guide.md/#indentation)
  - [Blank lines](../../style-guide.md/#blank-lines)
  - [Between operators](../../style-guide.md/#between-operators)
  - [Function calls](../../style-guide.md/#function-calls)
- [Line length](../../style-guide.md#line-length)
- Logical refactoring
  - [Conditional logic](../../style-guide.md#conditional-logic)
- Program design
  - [Fit and finish](../../style-guide.md#fit-and-finish)

## Collaboration

If you discuss an assignment with one or more classmates, **you must specify with whom you collaborated in a comment at the bottom of your submission**. You may discuss with as many classmates as you like, but you must cite all of them in your work. Note that you may not collaborate in a way that is prohibited, even if you cite the collaboration.

**At the bottom of both your `dna_analysis.py` and `answers.txt` files**, state which students or other people (besides the course staff) helped you with the assignment, or that no one did.

## Submission

Remove any assert statements before submitting to gradescope. Submit `dna_analysis.py` and `answers.txt` on Gradescope under the assignment **Homework: DNA Analysis**.
