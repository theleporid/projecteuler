fib_cache = {1: 1, 2: 2}
def fib(n):
    if n in fib_cache.values():
        return fib_cache[n]
    return fib(n-2) + fib(n-1)

n = 1
t = 0
while True:
    f = fib(n)
    if f >= 4_000_000:
        break
    if f % 2 == 0:
        t += f
    n += 1
    
print(t)
