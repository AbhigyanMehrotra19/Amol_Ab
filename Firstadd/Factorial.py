def recur(x):
    if x == 0 or x == 1:
        return x
    return x*recur(x-1)
