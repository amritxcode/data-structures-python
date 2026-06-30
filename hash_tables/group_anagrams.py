def groupAnagrams(strs):
    map = {}
    for i in strs:
        sort = "".join(sorted(i))
        if sort not in map:
            map[sort] = [i]

        elif sort in map:
            map[sort].append(i)
        
    return(sorted(map.values(), key= len))