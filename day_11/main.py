import math
import copy
input_ = [list(row) for row in open("./input.txt", "r").read().splitlines()]

def get_galaxies_distance(a,b):
    # return math.sqrt(math.pow(abs(b[0] - a[0]),2)  + math.pow(abs(b[1] - a[1]),2))
    return abs(b[0] - a[0])  + abs(b[1] - a[1])

def expand_universe(universe):
    expanded_universe = copy.deepcopy(universe)
    expand_col_indexes = []
    expand_row_indexes = []

    for x in range(len(universe[0])):
        need_to_expand_vertical = True

        for y in range(len(expanded_universe)):
            if expanded_universe[y][x] == "#":
                need_to_expand_vertical = False
                break
            
        if need_to_expand_vertical:
            expand_col_indexes.append(x)

    x = 0
    for x_ in expand_col_indexes:
        for row in expanded_universe:
            row.insert(x_ + x, ".")
        x += 1

    for x in range(len(expanded_universe)):
        row = expanded_universe[x]
        need_to_expand_horizontal = True

        for col in row:
            if col != ".":
                need_to_expand_horizontal = False
                break

        if need_to_expand_horizontal: 
            expand_row_indexes.append(x)


    y = 0
    for y_ in expand_row_indexes:
        expanded_universe.insert(y_ + y, ["."] * len(expanded_universe[0]))
        y += 1

    return expanded_universe

    
count = 0
num_coords = []
input_ = expand_universe(input_)

print(''.join(''.join(row) + "\n" for row in input_))

for i, row in enumerate(input_):
    for j, char in enumerate(row):
        if char == "#":
            count += 1
            input_[i][j] = count
            num_coords.append((i, j))

result = 0
for i, coords in enumerate(num_coords):
    for ii, prev_coords in enumerate(num_coords[:i]):
        if i == ii:
            continue
        galaxies_dist = get_galaxies_distance(prev_coords, coords)
        result += galaxies_dist

print(result * 100_000_000_000)
print(result == 9599070)

# for l in 2, 1_000_000: print(sum(map(get_galaxies_distance, [xs, ys])))
# 
# print(result + 999_999_999)