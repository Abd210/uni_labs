list1 = ["Math", "English", "History", "Chemistry", "Biology"]

#ex1 
print(list1[1])

#ex2
print(len(list1))
 
#ex3
print(list1[1], list1[2], list1[3])

#ex4
print(list1[-4])

#ex5
list2 = list1.copy()
list2.remove("Chemistry")
print(list2)

#ex6
list3 = list1.copy()
list3.insert(2, "Geography")
print(list3)

#ex7
list4 = list1.copy()
list4[list4.index("English")] = "Romanian"
print(list4)
