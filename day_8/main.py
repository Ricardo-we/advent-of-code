input_ = open("./input_1.txt", "r").readlines()
movements = [*input_[0].replace("\n", "")]
full_map = input_[1:]
formatted_map = {}

for i in range(len(full_map)):
    if  full_map[i] == '' or full_map[i] == '\n':
        continue

    full_map[i] = full_map[i].replace("\n", "")
    key = full_map[i].split(" = ")[0]
    formatted_map[key] = full_map[i].split(" = ")[1][1:-1].split(", ")

current_place = "AAA"
total_movements = 0
moveset_index = 0

while current_place != "ZZZ":
    if moveset_index > len(movements) - 1:
        moveset_index = 0
        continue

    if movements[moveset_index] == "L":
        current_place = formatted_map[current_place][0]
        total_movements += 1
    elif movements[moveset_index] == "R":
        current_place = formatted_map[current_place][1]
        total_movements += 1

    print(current_place)


    moveset_index += 1


print(total_movements)
