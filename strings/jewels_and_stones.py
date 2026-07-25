def num_jewels(jewels, stones):

    total_jewels = 0
    for i in stones:
        if i in jewels:
            total_jewels += 1

    return (total_jewels)

print(num_jewels("aAb", "aaAAABB"))