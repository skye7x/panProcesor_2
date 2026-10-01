def sito_fast(n):
    sito = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if sito[i]:
            sito[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))
    return [i for i in range(2, n + 1) if sito[i]]
print(sito_fast(50))