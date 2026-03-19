nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
unnested = []
for sublist in nested:
    for element in sublist:
        unnested.append(element)


print(unnested)
