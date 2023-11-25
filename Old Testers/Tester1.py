# update the function to return `word` with all instances of `letter` removed!
def remove_all_from_string(word, letter):
    
    return_word = word
    
    # loop until letter is not found
    while (True):
        
        # Find the letter needed in the word
        letter_loc = return_word.find(letter)
        
        # Check to see if no more letters that need to be removed are found
        # If so, leave the loop
        if (letter_loc == -1):
            break
        
        # If a letter is found, remove it
        return_word = return_word[:letter_loc] + return_word[letter_loc+1:]
    
    return return_word