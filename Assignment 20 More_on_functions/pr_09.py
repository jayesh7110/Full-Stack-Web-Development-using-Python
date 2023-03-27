# Write a python program to create a function to check whether a string is a pangram
# or not.

def is_pangram(phrase):
    # Create an empty set to store the unique lowercase characters
    unique_chars = set()

    # Iterate over each character in the phrase
    for char in phrase.lower():
        # If the character is a lowercase letter, add it to the set
        if char.isalpha() and char not in unique_chars:
            unique_chars.add(char)

    # Check if the set of unique characters has length 26 (i.e. all letters are present)
    return len(unique_chars) == 26


phrase = "Python programming language" #"The quick brown fox jumps over the lazy dog"
if is_pangram(phrase):
    print("The phrase is a pangram")
else:
    print("The phrase is not a pangram")