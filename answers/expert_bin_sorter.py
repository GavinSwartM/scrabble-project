    # Scrape Words from word list
with open("src/dictionary.txt", "r") as r:
    all_words = r.readlines()

counts: list[int] = []

words_by_length: list[list[str]] = []

sorted_words: list[str] = []

    # Increases the count for a certain index
def iter(index: int):
    while len(counts) <= index:
        counts.append(0)
    counts[index] += 1

    # Adds a word to the specified bucket for that length of word
def add_to_bucket(word: str, index: int):
    while len(words_by_length) <= index:
        words_by_length.append([])
    words_by_length[index].append(word)

    # Loop through each word
for word in all_words:
    word = word.strip().lower() # Remove any white space and make lower case
    n = len(word)

    iter(n)
    add_to_bucket(word, n)  # Iterate that length's count and add it to its bucket


    # Sort each bucket and add the sorted version to an overall list
for bucket in words_by_length:
    bucket.sort()
    sorted_words += bucket


n = len(counts)

leading_rows = [n + counts[0]]

    # Make a leading row of cumulative counts to show index of first word of that length 
for i in range(1, n):
    leading_rows.append(counts[i] + leading_rows[i - 1])


    # Convert to binary file

MAX_WORD_BYTES = 16

with open("sorted.bin", "wb") as writer:

    for line in leading_rows:
        writer.write(str(line).encode('utf-8').ljust(MAX_WORD_BYTES, b'\0'))

    for line in sorted_words:
        writer.write(str(line).encode('utf-8').ljust(MAX_WORD_BYTES, b'\0'))

writer.close()