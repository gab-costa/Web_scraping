import re
email = 'my ema9il is  gabrielcosta@usp.br iuwqgp iqwuhd 265423 1287 lodj 20972 o92jhe xioquyhd hbjwqv' \
        'klqdhnjkl lucas@hjwg'
y = re.findall('\S+@+\S+',email )
print(y)

# stracting a host name - using find and strinbg slicing

data = 'From gabrielcosta@usp.br sat jan 5 09:14:16'

words = data.split()


gmail = words[1]
pieces = gmail.split('@')
print(pieces)

#the sofisticate method to do the same thing usinmg regular explressions

sofisticate = re.findall('@([^ ]*)', data)
print(sofisticate)

fg = 'hgsahg 23 ujygds 455 iwhd'
print(re.findall('[1-9]+', fg))



z = 'From: Using the : character'
k = re.findall('^F.+:', z)
print(k)