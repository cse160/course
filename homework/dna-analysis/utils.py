# Utility Functions - DO NOT MODIFY THIS FILE!

# The sys module supports reading files, command-line arguments, etc.
import sys


# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """
    Read all lines from the DNA data file containing nucleotides and return it as a single string.

    dna_filename: the name of a file in DNA data file format: starting with the second line, every
        fourth line contains nucleotides.
    """
    # Creates a file object from which data can be read.
    input_file = open(dna_filename)

    # String containing all nucleotides that have been read from the file so
    # far.
    seq = ""

    # The current line number (= the number of lines read so far).
    linenum = 0

    for line in input_file:
        linenum = linenum + 1
        # if we are on the 2nd, 6th, 10th line...
        if linenum % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line

    input_file.close()
    return seq


def filename_from_arguments():
    # Check if the user provided an argument
    if len(sys.argv) < 2:
        print("You must supply a file name as an argument when running this program.")
        sys.exit(2)

    # Save the 1st argument provided by the user, as a string.
    # Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
    filename = sys.argv[1]

    return filename
