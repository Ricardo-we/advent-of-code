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

def walk(initial_step, ):
    current_place = initial_step
    total_movements = 0
    moveset_index = 0

    while not current_place.endswith("Z"):
        if moveset_index > len(movements) - 1:
            moveset_index = 0
            continue

        if movements[moveset_index] == "L":
            current_place = formatted_map.get(current_place)[0]
            total_movements += 1
        elif movements[moveset_index] == "R":
            current_place = formatted_map.get(current_place)[1]
            total_movements += 1

        print(current_place)


        moveset_index += 1

    return total_movements


# current_place = "MLA"
# current_place_2 = "BQA"
# walks = []
# for key in formatted_map.keys():
#     if key.endswith("A"):
#         walks.append(walk(key))

# print(sum(walks))

# print(walk(current_place) + walk(current_place_2) + 1)


total_movements = 0
moveset_index = 0
places = [key for key in formatted_map.keys() if key.endswith("A")]
# current_place = "MLA"
# current_place_2 = "BQA"
def is_z_in_all(places):
    for place in places:
        if not place.endswith("Z"):
            return False
    return True

print(places)

while not is_z_in_all(places):
    if moveset_index > len(movements) - 1:
        moveset_index = 0
        continue

    for place in places:
        if movements[moveset_index] == "L":
            places[places.index(place)] = formatted_map.get(place)[0]
        elif movements[moveset_index] == "R":
            places[places.index(place)] = formatted_map.get(place)[1]
            
        total_movements += 1

        # if place.endswith("Z.

    moveset_index += 1


print(total_movements)