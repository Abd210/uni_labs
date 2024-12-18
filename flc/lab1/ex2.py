dict1 = {"Fname": "Jane", "Lname": "Doe", "age": 23}

#ex1
print( dict1["Lname"])

#ex2
dict2 = dict1.copy()
dict2["age"] = 21
print( dict2)

#ex3
dict1["occupation"] = "student"
print( dict1)

#ex4
dic3 = dict1.copy()
dic3.pop("Fname")
print(dic3)

#ex5
print( list(dict1.items()))

#ex6
print( list(dict1.values()))

#ex7
dict1.setdefault("hobby", "chess")
print( dict1)

#ex8
dict1.clear()
print(dict1)
