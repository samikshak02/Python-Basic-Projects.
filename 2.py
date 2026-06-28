def analyze_string(a):

    if a == "":
        print("Empty string")
        return

    print("Length:", len(a))

    print("Reverse:", a[::-1])
    count = 0
    vowels = "aeiouAEIOU"
    for i in a:
        if i in vowels:
            count += 1

    print("Number of vowels:", count)

    print("Character with Positive and Negative Index:")

    n = len(a)
    for i in range(n):
        print("Positive Index:", i,
              "Negative Index:", i - n,
              "Character:", a[i])

text = input("Enter a string: ")
analyze_string(text)