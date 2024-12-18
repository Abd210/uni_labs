import math
import random
from datetime import datetime

# 1
def display_current_datetime():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%B %d, %Y %H:%M:%S")
    print("Current date and time:", formatted_date)

# 2
def circle_area():
    radius = int(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

# 3
def random_number_from_list():
    numbers = [10, 20, 30, 40, 50]
    random_number = random.choice(numbers)
    print("random number:", random_number)

# 4
def shuffle_list():
    elements = [1, 2, 3, 4, 5]
    random.shuffle(elements)
    print("Shuffled list:", elements)

# 5
def gcd_and_lcm():
    num1 = int(input("put first number: "))
    num2 = int(input("put second number: "))
    gcd = math.gcd(num1, num2)
    lcm = abs(num1 * num2) // gcd
    print(f"The GCD of {num1} and {num2} is: {gcd}")
    print(f"The LCM of {num1} and {num2} is: {lcm}")

# 6
def factorial():
    number = int(input("put a  number to compute  factorial: "))
    factorial_result = math.factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")

# 7
def week_number_of_date():
    date_input = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.strptime(date_input, "%Y-%m-%d")
    week_number = date.isocalendar()[1]
    print(f"The week number for the date {date_input} is: {week_number}")

# 8
def distance_between_points():
    x1, y1 = map(float, input("coordinates  first point (x1, y1): ").split())
    x2, y2 = map(float, input("coordinates second point (x2, y2): ").split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

# Menu to run the programs
def main():
    display_current_datetime()
    circle_area()
    random_number_from_list()
    shuffle_list()
    gcd_and_lcm()
    factorial()
    week_number_of_date()
    distance_between_points()

if __name__ == "__main__":
    main()
