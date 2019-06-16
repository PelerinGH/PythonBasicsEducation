primes=[2]
def is_prime(n):
    if n==1:
        return True
    if n in primes:
        return True
    elif n<primes[-1]:
        return False
    else:
        last=primes[-1]+1
        sq = int(float(n)**(1 / 2)+1)
        print("sq",sq+1)
        while last <= sq:
            for i in primes:
                if last%i==0:
                    break
            else:
                primes.append(last)
                if n==last:
                    return True
                elif n%last==0:
                    return False
            last+=1
        else:
            primes.append(n)
            return True
T=int(input())
for i in range(T):
    n=int(input())
    res=is_prime(n)
    print("Prime" if res else "Not prime")
    print(primes)