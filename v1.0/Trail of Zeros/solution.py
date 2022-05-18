def trailingZeros(n, arr):
    res = 0
    for elem in arr:
        res = res ^ elem

    i, zeros = 5, 0
    while i <= res:
        zeros += res // i
        i *= 5
    return zeros
