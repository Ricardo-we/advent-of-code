input_data = open("./input.txt", "r").read()

grid = input_data.splitlines()
ys, xs, stars = [0]*len(grid), [0]*len(grid[0]), 0

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "#":
            stars += 1
            xs[x] += 1
            ys[y] += 1


def dists(counts):
    weight, seen = 1 - stars, 0
    dist, coeff = 0, 0
    for pos, c in enumerate(counts):
        for _ in range(c):
            dist += weight*pos
            weight += 2
        seen += c
        if c == 0:
            coeff += seen * (stars - seen)
    return dist, coeff


ydist, ycoeff = dists(ys)
xdist, xcoeff = dists(xs)
dist, coeff = ydist + xdist, ycoeff + xcoeff

print("Part 1:", dist + 1 * coeff)
# print("Part 2:", dist + 999_999 * coeff)
