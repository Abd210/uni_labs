import math

#ex1
print("ex1: ")
for i in range(40,71):
    if i % 3 == 0:
      print(i)

#ex2
print("ex2: ")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Reversed order: {last_name} {first_name}")

#ex3
print("ex3: ")

n = int(input("Enter an integer: "))
sum_of_numbers = sum(range(1, n + 1))
print(f"The sum of all numbers  {n} is {sum_of_numbers}")

#ex4
print("ex4: ")

print("Loop through numbers and display 'Success':")
for i in range(5, 15):
    print("Success")

#ex5
# Define the string
string = "Welcome to the labe!"

# List of letters to count
letters_to_count = ['m', 'l', 'c', 'a', 'e']

# Loop through each letter, count its occurrences, and print the result
for letter in letters_to_count:
    count = string.lower().count(letter)
    print(f"The letter '{letter}' appears {count} time(s).")


#ex6
print("ex6: ")

n = int(input("Enter a number: "))
factorial = math.factorial(n)
print(f"The factorial of {n} is {factorial}")
print("\n")
    
#ex7
print("ex7: ")

num = int(input("Enter an integer: "))

if num > 100:
    result = (num / 2) + 20
else:
    result = (num * 3) - 200

print(f"Result: {result}")
print("\n")

# ex8
print("ex8: ")

user_input = input("Enter numbers separated by commas: ")
numbers_list = user_input.split(',')
numbers_tuple = tuple(numbers_list)

print(f"List: {numbers_list}")
print(f"Tuple: {numbers_tuple}")
print("\n")

# ex9
print("ex9: ")

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(f"The square of {i} is {i**2}")
