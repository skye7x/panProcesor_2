def euclidRecur(a, b):
    if a == b:
        return a
    if a > b:
        return euclidRecur(a - b, b)
    return euclidRecur(b - a, a)
print(euclidRecur(315, 504))