def wealthiest(accounts):
    richest = 0
    for i in accounts:
        if sum(i) >= richest:
            richest = sum(i)
    return richest


print(wealthiest([[7,1,3],[1,9,5],[3,2,1],[7,3],[3,5]]))