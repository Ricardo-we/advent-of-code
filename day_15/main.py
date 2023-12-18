def string_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list

print(sum(string_to_ascii("rn")))
print(sum(string_to_ascii("cm")))
