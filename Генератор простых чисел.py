def primes():
    now = 2
    primeset = set()
    while True:
        isprime=True
        for prime in primeset:
            if now % prime == 0:
                isprime=False
                break
        if isprime:
            primeset.add(now)
            yield now
        now+=1
p=primes()
for i in range(50):
    print(next(p))