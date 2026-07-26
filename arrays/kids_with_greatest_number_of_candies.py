def kidsWithCandies(candies, extraCandies):
    if not candies:
        return []
    
    greatest = []
    max_candies = candies[0]

    for candy in candies:
        if max_candies < candy:
            max_candies = candy

    for candy in candies:
        check = candy + extraCandies
        if check >= max_candies:
            greatest.append(True)
        else:
            greatest.append(False)

    return greatest

print(kidsWithCandies([2,3,5,1,3],3))