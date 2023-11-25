import difflib
from difflib import Differ

import re

# defining the strings
str_1 = "They would like to order a soft drink"
str_2 = "They would like to order a corn pizza"

# Using the splitlines function
lines_str1 = str_1.splitlines()
lines_str2 = str_2.splitlines()

# Using the Differ() and compare() function
dif = difflib.Differ()
my_diff = dif.compare(lines_str1, lines_str2)

# Print the results
print("First String:", str_1)
print("Second String:", str_2)
print("Difference between the Strings")
print('\n'.join(my_diff))

#split string with 2 delimiters
my_str = 'one,two-three,four'
my_list = re.split(r',|-|:|(', my_str)
# split on comma or hyphen
print(my_list)