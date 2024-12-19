def startA(x):
    if x == '0':
        dfa = 1  # Move to state B
    else:
        dfa = -1  
    return dfa

def stateB(x):
    if x == '0':
        dfa = 2  # Move to state C
    else:
        dfa = -1
    return dfa

def stateC(x):
    if x == '0':
        dfa = 3  # Move to state D
    elif x == '1':
        dfa = 4  # Move to state E
    else:
        dfa = -1
    return dfa

def stateD(x):
    if x == '0':
        dfa = 5  # Move to state F
    else:
        dfa = -1  
    return dfa

def stateF(x):
    if x == '0':
        dfa = 3  # Go back to state D
    elif x == '1':
        dfa = 4  # Move to state E
    else:
        dfa = -1
    return dfa

def stateE(x):
    if x == '1':
        dfa = 6  # Move to state G
    else:
        dfa = -1
    return dfa

def stateG(x):
    if x == '1':
        dfa = 6  # Stay in state G
    else:
        dfa = -1
    return dfa

def ex2(String):
    dfa = 0 
    for ch in String:
        if dfa == 0:
            dfa = startA(ch)
        elif dfa == 1:
            dfa = stateB(ch)
        elif dfa == 2:
            dfa = stateC(ch)
        elif dfa == 3:
            dfa = stateD(ch)
        elif dfa == 5:
            dfa = stateF(ch)
        elif dfa == 4:
            dfa = stateE(ch)
        elif dfa == 6:
            dfa = stateG(ch)
        else:
            return "The string does not belong to the language (00)+1+"
        
        if dfa == -1:
            return "The string does not belong to the language (00)+1+"
    
    if dfa == 4 or dfa == 6:
        return "The string belongs to the language (00)+1+"
    else:
        return "The string does not belong to the language (00)+1+"

# Test examples
s1 = "001"
s2 = "00001"
s3 = "0101"
s4 = "1110"

print(s1, ex2(s1), '\n')
print(s2, ex2(s2), '\n')
print(s3, ex2(s3), '\n')
print(s4, ex2(s4), '\n')
