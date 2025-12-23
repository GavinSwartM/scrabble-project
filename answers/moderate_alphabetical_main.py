# This is a nice simple solution that requires putting the whole 
# Dictionary into RAM. It uses binary search to filter through
# The dictionary in log(n) time. This is the way that most
# Search algorithms work behind-the-scenes, including Python's
# Built-in "in" function

with open("answers/sorted_alphabetical.txt", "r") as reader:
    all_words = [word.strip().lower() for word in reader]

def is_word_valid(input_data):

        # Check input type
    if type(input_data) != str:
        return False
    
        # Initialize binary search variables
    upper = len(all_words)

    lower = 0

    mid = (upper + lower) // 2

        # Loop through the sorted data while narrowing our search range to where the word should be
    while mid != lower and mid != upper and upper > lower:

            # If we found the word, return True
        if all_words[mid] == input_data.strip().lower():
            return True
        
            # If the word we found was too low in the alphabet
        elif all_words[mid] > input_data.strip().lower():
            upper = mid # Reduce the upper limit
        
        else: 
            lower = mid # Else, increase the lower limit
        
        mid = (upper + lower) // 2
    
        # If we break out of the loop, we have either 1 or 0 more indices to check, 
    return all_words[mid] == input_data.strip().lower() # Check mid one more time in case we have one more index to check