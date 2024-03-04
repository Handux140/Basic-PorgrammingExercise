# Input a number
number = int(input("Enter a number: "))

# Check if the number is even and greater than 10
if number % 2 == 0 and number > 10:
    print(f"The number {number} is even and greater than 10.")
else:
    print(f"The number {number} is not even or not greater than 10.")
