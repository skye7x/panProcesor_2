def euclidIter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
a = 315
b = 504
print(euclidIter(a, b))