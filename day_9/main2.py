with open("./input.txt", "r") as f:
    input_ = f.read().split("\n")

input_ = [[int(col) for col in row.split(" ")] for row in input_]

def process_row(row):
    changed_row = []
    rows = []
    
    for i in range(len(row) - 1):
        prev = row[i]
        current = row[i + 1]
        changed_row.append(current - prev)
    
    return changed_row      

def extrapolate(row_history):
    for i, row in enumerate(row_history):
        if i == 0:
            print(row)
            row.insert(0, 0)
            continue

        prev_row_first_element = row_history[i - 1][0]
        row.insert(0,row[0] - prev_row_first_element )
        
    return row_history[-1][0]

generated_rows = []

for i, row in enumerate(input_):
    generated_rows.append([row])
    while not all([col == 0 for col in row]):
        changed_row = process_row(row)
        row = changed_row
        generated_rows[i].append(changed_row)

result = 0
for generated_row in generated_rows:
    result += extrapolate(generated_row[::-1])
    
print(result)
            
