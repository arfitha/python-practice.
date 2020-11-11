def unichar(s):
    chars=set()
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True
print(unichar('apple'))
print(unichar('bat'))    