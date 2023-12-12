input_ = open("./input.txt", "r").read().strip().splitlines()

# connectables = {
#     "|":  "LJ7F",
#     "-": "LJ7F"
# }

def get_next_piece(piece_square):
    piece = piece_square.get("piece")
    is_s_conenction = piece == "S" and (piece_square.get("right") in "-7J" or piece_square.get("left") in "L-F" or piece_square.get("down") in "|JL" or piece_square.get("up") in "|7F")
    is_l_connection = piece == "L" and piece_square.get("right") == "-" and piece_square.get("up") == "|"
    is_j_connection = piece == "J" and piece_square.get("left") == "-" and piece_square.get("up") == "|"
    is_f_connection = piece == "F" and piece_square.get("right") == "-" and piece_square.get("down") == "|"
    is_7_connection = piece == "7" and piece_square.get("left") == "-" and piece_square.get("down") == "|"
    is_vertical_pipe = piece == "|" and (piece_square.get("down") in "|JL" or  piece_square.get("up") in "|7F")
    is_horiz_pipe = piece == "-" and (piece_square.get("left") in "-FL" or  piece_square.get("right") in "-J7")

    if is_vertical_pipe:
        return get_piece_square(
            piece_square.get("down_coords") if piece_square.get("down") in "|JL" else piece_square.get("up_coords"),
            input_
        )
        
    if is_horiz_pipe:
        return get_piece_square(
            piece_square.get("left_coords") if piece_square.get("left") in "-FL"  else piece_square.get("right_coords"),
            input_
        )
    
    if is_s_conenction:
        result = []
        for coords in piece_square.get("coords_list"):
            result.append(get_piece_square(coords, input_))
        return result

    if is_l_connection:
        return get_piece_square(
            piece_square.get("right_coords") if piece_square.get("right") == "-" else piece_square.get("up_coords"),
            input_
        )  

    if is_j_connection:
        return get_piece_square(
            piece_square.get("left_coords") if piece_square.get("right") == "-" else piece_square.get("up_coords"),
            input_
        )  

    if is_f_connection:
        return get_piece_square(
            piece_square.get("right_coords") if piece_square.get("right") == "-" else piece_square.get("down_coords"),
            input_
        )  

    if is_7_connection:
        return get_piece_square(
            piece_square.get("left_coords") if piece_square.get("right") == "-" else piece_square.get("down_coords"),
            input_
        )  

    

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
    max_moves = 0

    for piece in get_next_piece(piece_square):
        piece_square = get_next_piece(piece)
        if not piece_square or piece_square.get("piece") == "S": 
            continue
        while True:
            piece_square = get_next_piece(piece_square)
            print(piece_square)
            max_moves += 1
            if not piece_square or piece_square.get("piece") == "S":
                break
            
        if max_moves > 0:
            return max_moves

        # print("---PIECE---",piece)
        # print(get_next_piece(piece))
    
    # while True:
    #     piece_square = get_next_piece(piece_square)
    #     if type(piece_square) == list:
    #         for piece in piece_square:
    #             print(piece)
        #         loop.append(piece)
        #     break
        # print(piece_square)
        # loop.append(piece_square)

        # if not piece_square or piece_square.get("piece") == "S":
        #     break


    
    # piece_square = get_piece_square(piece_square.get("right_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("right_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("down_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("down_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("left_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("left_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("up_coords"), loop_map)
    # piece_square = get_piece_square(piece_square.get("up_coords"), loop_map)

    return loop

start_position = find_piece("S")
loop = remap(start_position, input_)

print(len(loop))