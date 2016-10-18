def int2bin(n, count=4):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])
