my_list = ["a", "b", "a", "c", "a", "b"]
counter = {}
for element in my_list:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1