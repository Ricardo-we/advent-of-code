
OFFSETS = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
}



def add_points(a: GridPoint, b: GridPoint) -> GridPoint:
    """
    add a pair of 2-tuples together. Useful for calculating a new position from a location and an offset
    """
    return a[0] + b[0], a[1] + b[1]

def possible_moves(current: GridPoint, c: str) -> tuple[GridPoint, GridPoint]:
    res = tuple(add_points(current, o) for o in OFFSETS[c])
    assert len(res) == 2
    return res

def find_start_adjacent(grid: Grid, grid_size: int, start: GridPoint) -> GridPoint:
    result = []
    for neighbor in neighbors(start, 4, max_size=grid_size - 1, ignore_negatives=True):
        if grid[neighbor] == ".":
            continue

        if start in possible_moves(neighbor, grid[neighbor]):
            result.append(neighbor)

    assert (
        len(result) == 2
    ), f"didn't find exactly 2 points that could reach start: {result}"
    return result[0]

def part_1(self) -> int:
        grid = parse_grid(self.input)
        start = next(k for k, v in grid.items() if v == "S")
        points = [start]

        current = find_start_adjacent(grid, len(self.input), start)

        while True:
            last = points[-1]
            points.append(current)
            a, b = possible_moves(current, grid[current])

            if (a == start or b == start) and last != start:
                return ceil(len(points) / 2)

            current = a if b == last else b