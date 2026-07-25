def manual_replace(address):
    char_list = list(address)
    for i in range(len(char_list)):
        if char_list[i] == ".":
            char_list[i] = "[.]"
    return "".join(char_list)


# Example usage:
print(manual_replace("1.1.1.1.1"))

