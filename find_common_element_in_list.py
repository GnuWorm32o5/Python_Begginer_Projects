my_list = ["a", "b", "a", "c", "a", "b"]
counter = {}
for element in my_list:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1

print(counter)
result = (max(counter, key=counter.get))
print(f"The most common element in this list is: {result}")
