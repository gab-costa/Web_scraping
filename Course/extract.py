import re
x = 'my 2 favorite numbers are 34 and 78'
y = re.findall('[1-9]+', x)
print(y)

# non-greeding match // if I dont use the ?, the find will pick up the full setence
line1 = 'From: using the: character'
find1 = re.findall('^F.+?:', line1) # ^ means when start, .+? one or more character but not greedy, : the last
print(find1)

