def accepts(word):
    return bool(word) and word[0] == word[-1]

print(accepts("aba"))  # True
print(accepts("abc"))  # False
