
file = open("./input_1.txt", "r")
sample_input = file.read()
sample_input = sample_input.split("\n\n")
file.close()

seeds = sample_input[0].split(":")[1].strip().split(" ")
almanac = sample_input[1:]

def process_map(map_):
    for x in map_.split("\n")[1:]: 
        range_start, source_range_start, range_length = x.split(" ") 


for map_ in almanac:
    process_map(map_)
# print(almanac)

def solution():
    pass