from functools import lru_cache

@lru_cache(maxsize=None)
def fibTest(n):
    if n < 2:
        return n
    return fibTest(n - 1) + fibTest(n - 2)

result = [fibTest(i) for i in range(16)]

print(result)