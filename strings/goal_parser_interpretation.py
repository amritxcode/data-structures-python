def goal_parser(command):
    goal = []
    i= 0

    while i < len(command):
        if command[i] == "G":
            goal.append("G")
            i+= 1
        elif command[i:i+2] == "()":
            goal.append("o")
            i += 2
        elif command[i:i+4] == "(al)":
            goal.append("al")
            i+= 4

    return "".join(goal)