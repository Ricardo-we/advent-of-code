from collections import deque
input_ = open("./input.txt", "r").read().strip().splitlines()

OFFSETS = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
    ".": [],
}

COL_LEN, ROW_LEN = len(input_), len(input_[0])

def add_points(a, b) :
    return a[0] + b[0], a[1] + b[1]

def get_neighbors(i, j):
    result = []
    for y, x in list(get_next_piece(get_piece_square((i,j), input_))):
        next_y, next_x = add_points((i,j), (y,x))
        if not (0 <= next_y < COL_LEN and 0 <= next_x < ROW_LEN):
            continue
        result.append((next_y, next_x))
    return result

def get_next_piece(piece_square,):
    piece = piece_square.get("piece")
    
    if piece == "S":
        result = []
        for y,x in [(1,0), (-1,0), (0,1), (0,-1)]:
            piece_y,piece_x = piece_square.get("y"), piece_square.get("x")
            next_y, next_x = add_points((y,x), piece_square.get("origin"))

            if not (0 <= next_y < COL_LEN and 0 <= next_x < ROW_LEN):
                continue

            if (piece_y,piece_x) in list(get_neighbors(next_y, next_x)):
                result.append((next_y, next_x))
        return result

    return OFFSETS[piece_square.get("piece")]


def find_piece(piece_name):
    for row in input_:
        for col in row:
            if col == piece_name:
                return (input_.index(row), row.index(col))

def get_piece_square(start_piece_position, loop_map):
    x, y = start_piece_position
    left = loop_map[y][x - 1] if x - 1 >= 0 else None
    right = loop_map[y][x + 1] if x + 1 < len(loop_map[y]) else None
    up = loop_map[y - 1][x] if y - 1 >= 0 else None
    down = loop_map[y + 1][x] if y + 1 < len(loop_map) else None

    return {
        "x": x,
        "y": y,
        "left": left,
        "right": right,
        "up": up,
        "down": down,
        "left_coords": (x - 1, y),
        "right_coords": (x + 1, y),
        "up_coords": (x, y - 1),
        "down_coords": (x, y + 1),
        "coords_list": [(x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1),],
        "piece": loop_map[y][x],
        "origin": (x,y)
    }

def remap(start_piece_position, loop_map):
    visited = set()
    dists = {}
    queue = deque([(start_position,0)])
    
    while len(queue) > 0:
        top, dist = queue.popleft()
        if top in visited:
            continue

        visited.add(top)
        dists[top] = dist
        
        for neighbor in list(get_neighbors(*top)):
            if neighbor in visited:
                continue
            queue.append((neighbor, dist + 1))
    return dists   

start_position = find_piece("S")
loop = remap(start_position, input_)

print(max(loop.values()) )