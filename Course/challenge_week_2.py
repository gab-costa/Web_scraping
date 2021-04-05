import re
import math
f = open('data.txt', 'r')


numbers = re.findall('[0-9]+', f.read())

sum = 0
for x in range(0,98):
    sum+=int(numbers[x])

print(sum)


