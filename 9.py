import math

try:
    # Take a sentence from the user
    sentence = input("Enter a sentence: ")

    # Convert sentence into unique words
    words = set(sentence.split())

    # Print unique words in sorted order
    print("Unique Words:")
    for word in sorted(words):
        print(word)

    # Count unique words
    count = len(words)

    # Print count raised to power 2
    print("Total Unique Words:", count)
    print("Count Raised to Power 2:", math.pow(count, 2))

except Exception as e:
    print("Error:", e)