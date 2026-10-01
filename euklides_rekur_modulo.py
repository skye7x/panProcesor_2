def betterEuclidRecur(a, b):
    if a == 0:
        return b
    return betterEuclidRecur(b % a, a)
print(betterEuclidRecur(1230, 528))