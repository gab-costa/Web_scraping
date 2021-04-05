import re
string = 'xixi gq bhbx'

print(re.search(r'^bonito', string)) # show where the word start and finish

print(re.findall(r'bonito', string))

print(re.sub('bonito','feio',string))


################### the other manner

print(re.search(r'^x.*', string))