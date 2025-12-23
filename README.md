<!--  



If you are able to read this, then you have accidentally opened the source code for this file instead of the file itself.

This is a Markdown (.md) file which allows for it to have more interesting formatting (as well as being easier to create).

Most text editors (likely including your IDE) are able to open them properly.

Try right clicking the file and clicking "Open Preview" or press Ctrl + Shift + V

If that doesn't work, scroll down and you will be able to read the file perfectly fine, just without proper formatting :(



-->
# Scrabble Word Checker Project 

One of the most useful things to do with Python is interact with large sets of data, this project is meant to give you a small introduction to that. While it doesn't use dicts, the Scrabble Dictionary makes for a fun way to practice many Python fundamentals for scraping data while still having a small enough size to brute force. Well, I guess "small" should be in quotes, because the Scrabble dictionary does include **178,691** unique words (at least the version neatly published as a txt by [Michael Barton](https://github.com/redbo/scrabble/blob/master/dictionary.txt#L178691)).

In this program, you are not permitted to use Python's built-in function *"in"* to detect if a word appears in an iterable. Python hardcodes this function in C, meaning that, even if there are faster ways to filter the data, using the *"in"* function will be faster. See [this video](https://www.youtube.com/watch?v=B_gb_K12viA) for a demonstration of just how much faster C is than Python.

The goal of this project is to develop a program that, as quickly and efficiently as possible, detects whether an input word is a legal word. To do this, you will need to accomplish 4 tasks:

### 1. Access the Scrabble Dictionary

In the *src/dictionary.txt* file located in this repository, there is a complete list of every single legal word for Scrabble. The first thing you will have to do is find some way to access the words out of the .txt and into a form readable by your Python program. 

---

### 2. Formatting the Scrabble Dictionary

The dictionary provided to you has been intentionally shuffled. So naturally, you'll need to find some way to sort it! Sorting the dictionary will certainly take quite a long time, so you will likely need to save your sorted version of the dictionary in order to make sure that you can access it without delay. Make sure to think about how you would like to save the data:

- Is there a file format that will allow for faster lookups?
- What order will be best for finding words later on?
- What method should I use for sorting the dictionary? How long will it take?

---

### 3. Parsing Input Data

All inputs will be passed into the function *is_word_valid* in the file titled *main.py*. Since Python does not enforce type annotations, there will be no rules as to how input data will be passed in. Make sure that your program knows how to properly check for invalid data types (the only valid type your program should accept is a String). All of the words in the dictionary are by default capitalized.

---

### 4. Finding the Input Word

The final step is the most important one. I won't give too much advice now, but I will encourage you to think about how efficient your program will be when you run it. The most naive approach to this problem is simply to check every single word in the dictionary, and see if any of them are equivalent to the input word. Doing this would have a worst case scenario of doing n checks. That being, checking every single entry. Think about what you can do to reduce the number of checks you must do as much as possible. 

# Bonus Challenge!

For an added challenge, assume that memory is limited and that you cannot load the entire file at once. This will require you to use a different file format besides .txt to properly solve the challenge. It will also likely make your program run much slower.

In order to beat this challenge, your program must run faster than a naive approach and also never load the entire file into memory at once. You can load small sections of it, though preferably those sections would be limited to less than a dozen lines.

# Test Cases

All of the test cases will come throuh VSCode's test cases. On the left side of the screen there is a beaker icon that is labeled *"Testing,"* when you click on it, it may ask you to configure Python Tests, configure them to use the /tests directory, unittest and files beginning with "test_."

The test cases will run your program directly by importing the *main/main.py* file then running the *is_word_valid* function within your program. Do not change the name of any files or directories. Do not modify the *src/dictionary.txt* file, as it is used in some of the test cases. 

If you want to make a new file, you can place it anywhere you want, just make sure you access it from the package directory.

To do tests of your own, place them within the *main* function within *main/main.py*. You can also place them outside of any function, but there is a good chance the built-in test cases will not work until you remove them.

# Benching

Once you finish the project, feel free to bench your program! In the *tests* directory, there is a file titled *bench.py* if you run this file, it will test your program against a random sample of the data and compare that to other implementations created in the *answers* directory as well as give you a time in seconds for how long your program took. Feel free to change the variables within the benching program to have different sized samples or different numbers of samples.

# Hints!

*Before you look at the hints, I would encourage you to make a full attempt at solving this problem.*

There are 3 tiers of hints. 

> 1. General Clues: 

These give nothing away about the solution, but simply contain a little advice to try to point you in the right direction.

> 2. Recommendations:

While they do not contain any actual code, these hints will recommend which methods will be most helpful to solving this problem. They will describe with moderate levels of detail what the methods are and how to implement them.

> 3. Pseudocode:

These hints are simply pseudocode versions of my preferred method of tackling the problem. 

And of course, if you are still stuck after looking through all of the hints, I have included my own solution in the *answers* folder of this repository.

---

### 1. Access the Scrabble Dictionary

- **General**

&nbsp;What built in methods does Python have to open and read txt files? What is the cost of looking through the entire dictionary? Are there any parts of the dictionary file that you will need to modify to avoid messing up your algorithm?

- **Recommendation**

&nbsp;Python has a method called *open* which allows you to read many different files. If you open the dictionary in reader mode, you can then use *readlines* to access all of the words in the file. 

&nbsp;Make sure that you use *strip* to get rid of the \n characters that will appear at the end of each line of the file. The \n characters will mess with the length of the word and mess up your checks for if two words are equal.

- **Pseudocode**

```Python
new_list = list()

with open("src/dictionary.txt", "r") as reader
    for each line in reader.readlines:  
        add line.strip() to new_list
```

---

### 2. Formatting the Scrabble Dictionary

- **General**

&nbsp;How can you store the data to most optimally retrieve it later? Is there any way that you can order the words so that when you look back through the list, you have a general idea of where certain words should be? What metadata does a String have besides the characters that make it up?

- **Recommendation**

&nbsp;The secret behind this part is realizing that Strings have a natural ordering. If you sort the list in alphabetical order, it will be much easier to find words. This means that as you travel down the list, each word will be "larger" than all words before it and "smaller" than all words after it.

&nbsp;Another important note is that, even before you do any searching, you know one thing about the input data: how long the word is. This means that if it is in the list, it will match up with another word that is the same length. If you separate the list into different sections for how long the word is, you will massively cut down your sample size.

&nbsp;If you are trying to tackle the bonus challenge, you will not be able to use a .txt. The fastest way to store the data in a way that allows for line specific reading is to store it directly as a binary file. This means that you will need to specifiy how long (in bytes) each word is going to be, then also find a way to navigate through that without looking at the file.

- **Pseudocode**

```Python
all_words = #see earlier

all_words.sort() # <-- Sorts the list alphabetically

writer = open("sorted.txt", "w")

for word in all_words:
    writer.write(word + "\n")
```

```Python
counts = [0, 0, 0, ..., 0] # <-- Track how many times each sized word appears

buckets = [[], [], [], ..., []] # <-- Separate the sorted list by word size

for word in all_words:
    counts[len(word)] += 1
    buckets[len(word)].append(word)

for each bucket: 
    bucket.sort()
```

For the Bonus Challenge:
```Python
lines = # see earlier

writer = open("sorted.bin", "wb")

for line in lines:
    writer.write(line.encode('utf-8').ljust(NUM_BYTES, b'\0'))
    # What this does, is encodes the word into a specific format (in which all characters will be 1 byte) then it fills any extra space with the null character.

reader = open("sorted.bin", "rb")

reader.seek(index * NUM_BYTES)
reader.read(NUM_BYTES).rstrip(b'\0').decode('utf-8')
# This does the exact same thing in reverse, it navigates the file pointer to the right spot in the file, reads the number of bytes it needs to, then scrapes out all of the null characters
```

---

### 3. Parsing Input Data

- **General**

&nbsp;What data types do we need to reject? How can we check the type of the parameter to make sure it matches? There is a way we can form the input data to make sure that we don't mess anything up. What can we do to the input data to make sure it matches what we expect from it?

- **Recommendation**

&nbsp;Python has a method called *type* that will return the type of a variable. This can be used to ensure that the type of the parameter is actually a String.

&nbsp;We can also use the *strip* method again as well as the *lower* method to make sure that the entire input data is just valid characters (abcde...). 

&nbsp;Also remember that we are looking at valid Scrabble words. There is a minimum length required for a word to be a word, and there is also a maximum length that no word will be longer than.

- **Pseudocode**

```Python
if type(input_data) == str:
    #Is Valid String!

input_data.strip()

input_data.lower()

if 2 <= len(input_data) <= MAX_LENGTH:
    #Is Valid String!
```

---

### 4. Finding the Input Word

- **General**

&nbsp;How many ways are there to search through a set of data? Are there any algorithms that can be used that will make this faster than checking all n entries? 

&nbsp;The most powerful search algorithm that exists within Computer Science is using *Binary Search* to only check log(n) entries.

- **Recommendation**

&nbsp;Binary Search is the best way to solve this problem. This is how all of Python's built-in search methods work. Binary Search works by checking the middle value between two extremes (the highest value an entry could be and the lowest). It then adjusts its upper and lower bounds based on if the middle value was too high or too low.

&nbsp;To use Binary Search, you need to first have a sorted dictionary, then assign upper and lower bounds (start off with them just at 0 and the dictionary length). From there, check the middle entry, if the middle entry is too low, increase the lower bound to be the index of the middle entry, if the middle entry is too high, decrease the upper bound to be the middle entry.

> Binary Search 
> ---
>
> **midpoint < input:**&nbsp;&nbsp; lower = midpoint
>  
> **midpoint > input:**&nbsp;&nbsp; upper = midpoint
>
>**midpoint = input:**&nbsp;&nbsp; return midpoint
>
> Repeat until midpoint is the same as upper or lower, then check the midpoint one last time before returning False.

&nbsp;This [article by GeeksforGeeks](https://www.geeksforgeeks.org/dsa/binary-search/) explains Binary Search well with many examples. 

- **Pseudocode**

```Python
sorted_words = #see earlier

upper = len(sorted_words)

lower = 0

mid = upper + lower / 2

while mid != upper or lower:

    if sorted_words[mid] == in_string:
        return True
    
    elif sorted_words[mid] < in_string:
        lower = mid
    
    else:
        upper = mid

    mid = upper + lower / 2

return sorted_words[mid] == in_string

```
<!-- Created by Gavin Swart 20205 -->