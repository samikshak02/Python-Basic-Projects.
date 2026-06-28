import random
import math

# Create an empty set
numbers = set()

# Take 10 numbers from the user
while len(numbers) < 10:
    try:
        num = int(input("Enter a number: "))
        numbers.add(num)
    except ValueError:
        print("Please enter a valid number.")

# Convert set to tuple
num_tuple = tuple(numbers)

print("Tuple:", num_tuple)

try:
    # Pick 3 random numbers
    random_numbers = random.sample(num_tuple, 3)
    print("3 Random Numbers:", random_numbers)

    # Find square root of sum
    total = sum(num_tuple)
    print("Sum:", total)
    print("Square Root:", math.sqrt(total))

except ValueError:
    print("Not enough numbers to pick 3 random values.")

except Exception as e:
    print("Error:", e)