# This version has all of the best algorithms for finding the proper word
# It utilizes binary search and limits the search range by filtering for
# Only the section of the dictionary that contains the same length word
# As the input

with open("answers/sorted_length.txt", "r") as reader:
    all_words = [word.strip().lower() for word in reader]

def is_word_valid(input_data):

        # Start off by checking for basic things that will automatically disqualify an input

    if type(input_data) != str: # <- if it is not a string, return False
        return False
    
    n = len(input_data)

    if n < 2 or n > 15: # <- if it's length is too big or small, return False
        return False
    
        # Properly parse the input into a valid string
    
    in_string = input_data.strip().lower()
    
        # Get the upper and lower bounds 

    lower = int(all_words[n - 1])

    upper = int(all_words[n])
    
    mid = (upper + lower) // 2


        # Binary search for the input string until we either find it or fail to find it

    while mid != upper and mid != lower and upper > lower:

            # If mid is the word, return True
        if all_words[mid] == in_string:
            return True
        elif all_words[mid] > in_string: # If mid is too high, lower the upper range
            upper = mid
        else:
            lower = mid # If it is too low, increase the lower range
        
        mid = (upper + lower) // 2 # Update mid 
    
    return all_words[mid] == in_string