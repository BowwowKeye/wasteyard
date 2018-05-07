statement=raw_input('Please enter your statement:\n')
revert=[]
for letter in statement:
    if ord(letter)>90:
        revert.append(letter.upper())
    else:
        revert.append(letter.lower())
print ''.join(revert)
