import difflib
from difflib import get_close_matches

# Using the get_close_matches method
my_list = get_close_matches(
    'mas',
    ['master','mask','duck','cow',
    'mass','massive','python','butter'],
    n = 4,
    cutoff = 0.6)

# print the list
print("Matching words:", my_list)