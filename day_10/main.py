input_ = open("./input.txt", "r").read().strip().splitlines()

OFFSETS = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
}

def add_points(a, b ) :
    return a[0] + b[0], a[1] + b[1]


def get_next_piece(piece_square, prev_piece_square=None):
    pass
    # piece = piece_square.get("piece")
    # is_s_conenction = piece == "S" and (piece_square.get("right") in "-7J" or piece_square.get("left") in "L-F" or piece_square.get("down") in "|JL" or piece_square.get("up") in "|7F")
    # is_l_connection = piece == "L" and piece_square.get("right") in "-7J" and piece_square.get("up") in "|7F"
    # is_j_connection = piece == "J" and piece_square.get("left") in "-LF" and piece_square.get("up") in "|F7"
    # is_f_connection = piece == "F" and piece_square.get("right") in "-J7" and piece_square.get("down") in "|JL"
    # is_7_connection = piece == "7" and piece_square.get("left") in "-FL" and piece_square.get("down") == "|JL"
    # is_vertical_pipe = piece == "|" and (piece_square.get("down") in "|JL" or  piece_square.get("up") in "|7F")
    # is_horiz_pipe = piece == "-" and (piece_square.get("left") in "-FL" or  piece_square.get("right") in "-J7")

    # if is_vertical_pipe:
    #     return get_piece_square(
    #         piece_square.get("down_coords") if piece_square.get("down") in "|JL" else piece_square.get("up_coords"),
    #         input_
    #     )
        
    # if is_horiz_pipe:
    #     return get_piece_square(
    #         piece_square.get("left_coords") if piece_square.get("left") in "-FL"  else piece_square.get("right_coords"),
    #         input_
    #     )
    
    # if is_s_conenction: 
    #     result = []
    #     for coords in piece_square.get("coords_list"):
    #         result.append(get_piece_square(coords, input_))
    #     return result
    
    # # if not prev_piece_square: 
    # #     return None

    # print( prev_piece_square.get("piece"), piece_square.get("right"))

    # if is_l_connection:
    #     return get_piece_square(
    #         # piece_square.get("right_coords") if piece_square.get("right") == "-" else piece_square.get("up_coords"),
    #         piece_square.get("right_coords") if piece_square.get("right") != prev_piece_square.get("piece") else piece_square.get("up_coords"),
    #         input_
    #     )  

    # if is_j_connection:
    #     return get_piece_square(
    #         # piece_square.get("left_coords") if piece_square.get("left") == "-" else piece_square.get("up_coords"),
    #         piece_square.get("left_coords") if piece_square.get("left") != prev_piece_square.get("piece") else piece_square.get("up_coords"),
    #         input_
    #     )  

    # if is_f_connection:
    #     return get_piece_square(
    #         # piece_square.get("right_coords") if piece_square.get("right") == "-" else piece_square.get("down_coords"),
    #         piece_square.get("right_coords") if piece_square.get("right") != prev_piece_square.get("piece") else piece_square.get("down_coords"),
    #         input_
    #     )  

    # if is_7_connection:
    #     return get_piece_square(
    #         # piece_square.get("left_coords") if piece_square.get("right") == "-" else piece_square.get("down_coords"),
    #         piece_square.get("left_coords") if piece_square.get("left") != prev_piece_square.get("piece") else piece_square.get("down_coords"),
    #         input_
    #     )  

    

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
    piece_square = get_piece_square(start_piece_position, loop_map)
    loop = [piece_square]
    paths = []
    max_moves = 0

    # for piece in get_next_piece(piece_square):
    #     piece_square = get_next_piece(piece)
    #     prev_piece_square = piece_square
        
    #     if not piece_square or piece_square.get("piece") == "S": 
    #         continue

    #     while True:
    #         prev_piece_square = piece_square
    #         piece_square = get_next_piece(piece_square, prev_piece_square)
    #         max_moves += 1
            
    #         if max_moves > 4:
    #             print(max_moves)
    #             break

    #         if not piece_square or piece_square.get("piece") == "S":
    #             break
            
    #     if max_moves > 0:
    #         return max_moves

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


    
    prev_piece_square = None
    
    piece_square = get_next_piece(piece_square, prev_piece_square)
    prev_piece_square = piece_square

    piece_square = get_next_piece(piece_square[1], prev_piece_square)
    prev_piece_square = piece_square

    piece_square = get_next_piece(piece_square, prev_piece_square)
    prev_piece_square = piece_square
    
    piece_square = get_next_piece(piece_square, prev_piece_square)
    print(piece_square)

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