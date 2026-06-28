square = lambda x: x * x

try:
    # Store squares of numbers from 1 to 20
    squares = []

    for i in range(1, 21):
        squares.append(square(i))

    print("Squares:", squares)

    # Print only even squares
    print("Even Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num)

except Exception as e:
    print("Error:", e)

