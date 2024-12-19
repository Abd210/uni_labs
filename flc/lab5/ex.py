def dfa(word):
    currentState = "A"  
    for char in word:
        if currentState == "A":
            if char == '1':
                currentState = "B"
            else:
                return False
        elif currentState == "B":
            if char != '1':
                return False
    
    return currentState == "B"

# Examples
print(dfa("1"))      
print(dfa("111"))    
print(dfa("1110"))   
print(dfa("0"))      