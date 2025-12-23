# This is the most naive approach to tackling this problem, 
# It simply checks every single word after verifying that the input is a string

def is_word_valid(input_data):

    if type(input_data) != str:
        return False
    
    with open("src/dictionary.txt", "r") as reader:
        for word in reader.readlines():
            if word.strip().lower() == input_data.strip().lower():
                return True
    
    return False