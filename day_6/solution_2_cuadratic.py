import re
import numpy as np
import math

input_ = open("./input.txt").readlines()

time = list(map(int, ' '.join(input_[0].split()).split(": ")[1].split(" ")))
distance = list(map(int, ' '.join(input_[1].split()).split(": ")[1].split(" ")))
time = int(''.join(str(x) for x in time))
distance = int(''.join(str(x) for x in  distance))

def quadratc(a,b,c):
    return [(-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a), (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)]

# y = x (h  - x)
# y = ax (b  - cx)

a = time
b = distance
c = 1

sol1,sol2 = quadratc(a,b,c)

print(sol1,sol2)
