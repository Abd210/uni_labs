
import re

a = "rectangle"
b = "square"
c = "sphere"
d = "triangle"
e = "cone"
f = "cube"
g = "cylinder"

strings = [a, b, c, d, e, f, g]

pattern = re.compile(r'^[cs].*e$')

for string in strings:
    if pattern.match(string):
        print(string)

print("               ")
print("ex2: ")
print("               ")


words = "car, cat, dog, pool, bath, cone, cube, ring, int"

words_list = words.split(", ")

pattern = re.compile(r'^\w{4}$')

for word in words_list:
    if pattern.match(word):
        print(word)

print("               ")
print("ex3: ")
print("               ")

words_list = ["square", "triangle", "cube", "sphere", "circle", 
              "pentagon", "hexagon", "rectangle", "parallelogram", "trapezoid"]

pattern = re.compile(r'.*re$')

for word in words_list:
    if pattern.match(word):
        print(word)

print("               ")
print("ex4: ")
print("               ")

geo = ("A square has 4 sides, a triangle has 3, a pentagon has 5, "
       "a hexagon has 6. While a square has 4 equal sides, "
       "a triangle can have 0, 2 or 3 equal sides.")

digits = re.findall(r'\d', geo)
print("Digits:", digits)

non_digits = re.findall(r'\D+', geo)
print("Non-digits:", non_digits)

print("               ")
print("ex5: ")
print("               ")

link = ("https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-"
        "the-war-for-gloria-read-until-you-understand-and-the-end-of-bias")

date_pattern = re.compile(r'/(\d{4})/(\d{2})/(\d{2})/')
match = date_pattern.search(link)

if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

print("               ")
print("ex6: ")
print("               ")

date = "2025-12-02"

new_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date)
print("New date format:", new_date)
