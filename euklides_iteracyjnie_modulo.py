def betterEuclidIter(a, b):
    while b != 0:
        zmienna = b
        print("zmienna =", zmienna)
        b = a % b
        a = zmienna
        print()
    return a
print(betterEuclidIter(48, 18))