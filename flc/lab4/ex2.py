import re

def starts_with_digit(string):
    pattern = re.compile(r'^\d')
    return bool(pattern.match(string))

print(starts_with_digit("123abc")) 

print(starts_with_digit("abc123")) 


print("ex8")

def ends_with_digit(string):
    pattern = re.compile(r'\d$')
    return bool(pattern.search(string))

print(ends_with_digit("abc123")) 

print(ends_with_digit("123abc")) 


print("ex9")

def contains_digit(string):
    pattern = re.compile(r'\d')
    return bool(pattern.search(string))

print(contains_digit("abc123"))  

print(contains_digit("abcdef"))
