def finalValueAfterOperations(operations):
    X = 0
    for i in operations:
        if i[0:] == "--X" or i[0:] == "X--":
            X -= 1
        elif i[0:] == "X++" or i[0:] == "++X":
            X += 1
    return X

print(finalValueAfterOperations(["--X","X++","X++"]))