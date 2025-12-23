# This is an advancement from the previous one by replacing the SQL 
# Database with a binary file. Often times the fastest way to read
# Or write data is just to do it directly in the binary. That makes
# This a lot faster than the SQL database. It will still be slower
# Then some of the previous versions that load the entire dictionary
# Into RAM.

reader = open("answers/sorted.bin", "rb") # Opens binary file at import in order to prepare for reading
    # Note: This does not load all of the data from the file, just a pointer that can look into the file

def _get_word_from_index(index: int) -> str:

        # We loaded each word as being 16 bytes, so now we seek to the proper position
    reader.seek(index * 16)
    return reader.read(16).rstrip(b'\0').decode("utf-8") # Then only read the 16 bytes of the word


def is_word_valid(input_data):

        # Start off by checking for basic things that will automatically disqualify an input

    if type(input_data) != str: # <- if it is not a string, return False
        return False
    
    n = len(input_data)

    if n < 2 or n > 15: # <- if it's length is too big or small, return False
        return False
    
        # Properly parse the input into a valid string
    
    in_string = input_data.lower()
    
        # Get the upper and lower bounds 

    lower = int(_get_word_from_index(n - 1))

    upper = int(_get_word_from_index(n))
    
    mid = (upper + lower) // 2


        # Binary search for the input string until we either find it or fail to find it

    while mid != upper and mid != lower and upper > lower:

            # Grab the word from the database
        found = _get_word_from_index(mid)

            # If it is the word, return True
        if found == in_string:
            return True
        elif found > in_string: # If it is too high, lower the upper range
            upper = mid
        else:
            lower = mid # If it is too low, increase the lower range
        
        mid = (upper + lower) // 2 # Update mid 
    
    return _get_word_from_index(mid) == in_string