
    # A set in Python is basically a HashSet
    # That means it has O(1) puts and gets
    # And it is hard coded in C making it blazing fast
    # It does go against the spirit of the project however, 
    # Because we are not actually searching through the dictionary
    # And it requires loading all of the dictionary into memory twice
dictionary = set()

with open("src/dictionary.txt", "r") as reader:
    [dictionary.add(word.strip().lower()) for word in reader.readlines()]
        

def is_word_valid(input_data):
    return type(input_data) == str and input_data.strip().lower() in dictionary