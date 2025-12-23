
    # Read through all of the words in the dictionary
with open("src/dictionary.txt", "r") as reader:
    all_words = reader.readlines()

    # Sort them
all_words.sort()

    # Write to file
with open("answers/sorted_alphabetical.txt", "w") as writer:
    writer.writelines(all_words)