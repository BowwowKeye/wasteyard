import string
import keyword
letterdigits=string.letters+string.digits
initials=string.letters+'_'
keywords=keyword.kwlist
for item in keywords:
    print item,
print
identifier=raw_input('please input the identifier:\n')
if identifier in keywords:
    print "Illegal identifier : Python keyword"
    exit()
if identifier[0] in initials:
    for item in identifier[1:]:
        if item not in letterdigits:
            print "Illegal identifier : Identifier must contain only alphabet or digits"
            exit()
else:
    print "Illegal identifier: The first letter must be in alphabet or _"
    exit()
print "OK"
