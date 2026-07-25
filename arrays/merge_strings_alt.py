def merge_strings(word1,word2):
    combined = []
    i = 0

    while i < len(word1) or i < len(word2):
        if i < len(word1):
            combined.append(word1[i])

        if i < len(word2):
            combined.append(word2[i])

        i+= 1

    return "".join(combined)