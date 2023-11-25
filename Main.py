import difflib
from difflib import SequenceMatcher
import re

# Generated with ChatGPT
# Replaces words with a '-'
# For example, the String "Hello, my name is: (Jason)" would become "-, - - -: (-)"
# We do this to detect plagarism where the variable names are changed and instead look at the roots of the code
def replace_words_with_dash(input_string):
    pattern = re.compile(r'\b\w+\b')
    result_string = pattern.sub('-', input_string)
    return result_string

# Filters out junk lines and potential plagarism tricks:
# Ignores both short (#) and long comments (''')
# Ignores empty lines
# Replaces all words with "-"
# This eliminates the possibility of someone simply changing the wording of a piece of code and tricking the similarity tester
def process_lines(lines_list):

    in_long_comment = False

    processed_lines = []

    # Loop through every line in the file and filter out junk
    for l in range(len(lines_list)):
        line = lines_list[l].strip()

        # Ignore any long comments indicated by '''
        # These are on multiple lines, so they must be detected and remembered
        if line == "'''":
            in_long_comment = not(in_long_comment)
            continue
        
        if in_long_comment:
            continue

        # Filter out any empty lines or commented lines
        if line == '' or line[0] == '#':
            continue
        
        # Replaces all words with a "-"
        line = replace_words_with_dash(line)

        # Add any non-filtered lines back into the return variable
        processed_lines.append(line)
    
    return processed_lines

# Returns a ratio between 1.0 and 0.0
# 1.0 signifies that the two files are identical
# 0.0 signifies that the two files are completely different
def get_file_similarity_ratio(file_1, file_2):

    # Load the String data from each file into a variable
    file_1_str = open(file_1, "r").read().splitlines()
    file_2_str = open(file_2, "r").read().splitlines()

    # Filter out junk data
    file_1_processed = process_lines(file_1_str)
    file_2_processed = process_lines(file_2_str)

    # use the Sequencematcher() function to assess similarities
    my_seq = SequenceMatcher(a = file_1_processed, b = file_2_processed)

    return my_seq.ratio()

def assess_similarity_ratio(ratio):
    if ratio == 1:
        return "Extremely High Risk of Plagarism"
    elif ratio >= 0.5:
        return "High Risk of Plagarism"
    return "Low Risk of Plagarism"

# Original 1 vs. Original 2
# Score: 
print("Original 1 vs. Original 2")
ratio = get_file_similarity_ratio("Test1Original.py", "Test2Original.py")
print("Ratio:", ratio)
print("Danger Level:", assess_similarity_ratio(ratio))

# Original 1 vs. New Names 1
# Score: 
print("Original 1 vs. New Names 1")
ratio = get_file_similarity_ratio("Test1Original.py", "Test1NewNames.py")
print("Ratio:", ratio)
print("Danger Level:", assess_similarity_ratio(ratio))

# Original 1 vs. ChatGpt 1
# Score: 
print("Original 1 vs. ChatGpt 1")
ratio = get_file_similarity_ratio("Test1Original.py", "Test1ChatGPT.py")
print("Ratio:", ratio)
print("Danger Level:", assess_similarity_ratio(ratio))