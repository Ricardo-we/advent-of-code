input_ = open("./input.txt", "r").read().strip().splitlines()

connectables = {
    "|":  "LJ7F",
    "-": "LJ7F"
}

def get_connections(piece, piece_square):
    if piece == "S":
        if piece_square.get("right"):
            return get_piece_square(piece_square.get("right_coords"), input_)
        if (piece_square.get("up") == "-"):
            return get_piece_square(piece_square.get("up_coords"), input_)
        if (piece_square.get("up") == "|"):
            return get_piece_square(piece_square.get("up_coords"), input_)
        if (piece_square.get("down") == "|"):
            return get_piece_square(piece_square.get("down_coords"), input_)

            
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
        "down_coords": (x, y + 1),
        "coords_list": [(x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1),],
        "piece": loop_map[y][x]
    }

def remap(start_piece_position, loop_map):
    piece_square = get_piece_square(start_piece_position, loop_map)
    loop = [piece_square]
    paths = []

    while True:
        if piece_square.get("piece") == "S":
            for coords in piece_square.get("coords_list"):
                next_piece = get_piece_square(coords, loop_map)
                # print(coords, piece_square)
                # print(next_piece.values()vb )
                # print(get_connections(coords, piece_square))
                # path = get_piece_square(coords, loop_map)
                # paths.append(get_piece_square(coords, loop_map))
            break

        piece_square = get_connections(start_piece_position, piece_square)
        loop.append(piece_square)
        if piece_square == None or (piece_square and piece_square.get("piece") == "S"):
            break
        print(piece_square)

    return loop

start_position = find_piece("S")
loop = remap(start_position, input_)

print(len(loop))