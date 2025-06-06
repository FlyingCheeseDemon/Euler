import tools as tls

# huge performance gains vs the original

def is_prime(num,lop):
    for p in lop:
        if tls.divisible(num,p):
            return False
    return True

list_of_primes = []
i = 2
while len(list_of_primes) < 10001:
    if is_prime(i,list_of_primes):
        list_of_primes.append(i)
    i += 1

print(list_of_primes[-1])