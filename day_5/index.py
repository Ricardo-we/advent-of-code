
file = open("./input_1.txt", "r")
sample_input = file.read()
sample_input = sample_input.split("\n\n")
file.close()

seeds = list(map(int, sample_input[0].split(":")[1].strip().split(" ")))
almanac = sample_input[1:]
seeds_full_map = {}

def process_map(map_,seeds):
    original_values = seeds.copy()

    for i, original_value in enumerate(original_values): 
        for map_row in map_.split("\n")[1:]: 
            range_start, source_range_start, range_length = list(map(int, map_row.split(" ")))
            
            if original_value > range_start or  range_start + range_length < original_value or original_value - source_range_start < 0:
                continue

            original_values[i] = range_start + (original_value - source_range_start)
            break;

    return original_values

for map_ in almanac:
   seeds = process_map(map_, seeds)

print(seeds)

def solution():
    pass