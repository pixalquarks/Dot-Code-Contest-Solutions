def removeAdjacents(n, k, s):
    if len(s) <= 1:
        return s
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
            continue
        c = stack.pop()
        if (ord(c) - 97) != (ord(char) - 97 - k) % 26:
            stack.append(c)
            stack.append(char)

    res = "".join(stack)
    return res


print(removeAdjacents(6, 10, "axishi"))
