# Name: ...
# CSE 160
# Spring 2026
# DNA Analysis

# This program reads in DNA sequencer output and computes statistics, such as the GC content, AT
# content, nucleotide counts, etc.

# Code comments have been added to explain the Python code. If we were to distribute this program
# to others, the code is sufficiently self-explanatory: code comments are not recommended at all!

# We're using some utility functions from the utils.py file we wrote to read DNA data files.
from utils import filename_to_string, filename_from_arguments


# Function to return GC Classification
def classify(gc_content):
    """
    Returns a string representing GC content classification: "low", "moderate", or "high".

    gc_content: a number representing the GC content
    """

    # This statement is a placeholder. Replace it with your code (more than one line) that sets
    # classification to the correct value based on gc_content. Then, delete this comment.
    classification = "high"

    # YOUR CODE GOES HERE

    return classification


def nano_suitable(gc_content):
    """
    Returns a boolean representing if the given GC content is suitable for DNA nanotechnology.

    gc_content: a number representing the GC content
    """
    # YOUR CODE GOES HERE
    return True


# Main program begins here

# Check that a filename has been provided as the second argument
filename = filename_from_arguments()

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(filename)

# Compute DNA sequence statistics

# YOUR CODE GOES BELOW THIS POINT

# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0

for base in nucleotides:
    total_count = total_count + 1

    # OK to change this code!
    if base == "C" or base == "G":
        gc_count = gc_count + 1

gc_content = gc_count / total_count
print("GC-content:", gc_content)


# You can add more assertions here to validate properties. The given message will only display when
# the assertion fails.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
