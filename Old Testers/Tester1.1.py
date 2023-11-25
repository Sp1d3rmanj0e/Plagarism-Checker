# Change all words to a diff word
def ASSignment_3(word, letter):
    
    variable_2 = word
    
    # it keeps going until its correct
    while (True):
        
        # find what is missing
        gabalaba = variable_2.find(letter)
        
        # sees if it is done
        # if it is it stops
        if (gabalaba == -1):
            break
        
        # remove it if the letter is wrong
        variable_2 = variable_2[:gabalaba] + variable_2[gabalaba+1:]
    
    return variable_2