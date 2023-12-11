input_ = open("./input.txt", "r").read().strip().splitlines()

connectables = {
    "|":  "LJ7F",
    "-": "LJ7F"
}

def get_connections(piece, piece_square):
    if (piece == "L" and piece_square.get("right") == "-") and (piece == "L" and piece_square.get("up") == "|"):
        return get_piece_square(piece_square.get("right_coords") if piece == "-" else piece_square.get("up_coords"),input_)

    if (piece == "J" and piece_square.get("left") == "-") and (piece == "J" and piece_square.get("up") == "|"):
        return get_piece_square(piece_square.get("left_coords") if piece == "-" else piece_square.get("up_coords"),input_)

    if (piece == "F" and piece_square.get("right") == "-") and (piece == "F" and piece_square.get("down") == "|"):
        return get_piece_square(piece_square.get("right_coords") if piece == "-" else piece_square.get("down_coords"),input_)

    if (piece == "7" and piece_square.get("left") == "-") and (piece == "7" and piece_square.get("down") == "|"):
        return get_piece_square(piece_square.get("left_coords") if piece == "-" else piece_square.get("down_coords"),input_)
        

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
        "down_coords": (x, y + 1)
    }

def remap(start_piece_position, loop_map):
    piece_square = get_piece_square(start_piece_position, loop_map) 
    l_s = get_piece_square((1,3), input_)
    x = get_connections("L", l_s)
    print(x)
    print(piece_square)
    # piece_square = get_piece_square(piece_square["right_coords"], loop_map)
    # print(piece_square)


loop = []
start_position = find_piece("S")
remap(start_position, input_)
