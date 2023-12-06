import re
import numpy as np

input_ = open("./input.txt").readlines()
time = list(map(int, ' '.join(input_[0].split()).split(": ")[1].split(" ")))
distance = list(map(int, ' '.join(input_[1].split()).split(": ")[1].split(" ")))

time = int(''.join(str(x) for x in time))
distance = int(''.join(str(x) for x in  distance))

# velocities = {
#     "1": 1, 
#     "2": 2,
#     "3": 4,
#     "4": 3,
#     "5": 10,
#     "6": 6,
#     "7": 0,
# }

def solution(time, distance):
    result = []
    for pressed_time in range(1, time + 1):
        restant_time = time - pressed_time
        traveled = restant_time * pressed_time

        # print(f"Pressed time: {pressed_time}mm/s")
        # print(f"Restant time: {restant_time}ms")
        # print(f"Traveled: {traveled}mm")
        # print("....................")

        if(traveled > distance):
            result.append(traveled)

    # print("--------END TIME----------")
    return len(result) if len(result) > 0 else 1 



if __name__ == "__main__":
    print(time, distance)
    result = 1
    result *= solution(time,distance)
    print(result)