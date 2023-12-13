import math
input_ = [list(row) for row in open("./input.txt", "r").read().splitlines()]


# SOLUTION IDEA
# 1. Find possible combinations of galaxies
# 2. b_coords - a_coords, this will return de difference between the two galaxies

def get_galaxies_distance(a,b):
    # return math.sqrt(math.pow(abs(b[0] - a[0]),2)  + math.pow(abs(b[1] - a[1]),2))
    return abs(b[0] - a[0])  + abs(b[1] - a[1])

    
count = 0
num_coords = []

for i, char in enumerate(input_):
    for j, char_ in enumerate(char):
        if char_ == "#":
            count += 1
            input_[i][j] = count
            num_coords.append((i, j))

result = 0
for i, coords in enumerate(num_coords):
    universe_size = 0
    for ii, prev_coords in enumerate(num_coords[:i]):
        if i == ii:
            continue
        # print(coords, prev_coords)
        galaxies_dist = get_galaxies_distance(prev_coords, coords)
        universe_size += 1
        result += galaxies_dist * universe_size

print(result)