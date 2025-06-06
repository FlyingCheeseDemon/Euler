# find all primes < 20
import tools as tls

prime_prod = 1
for i in range(2,20):
    if tls.is_prime(i):
        prime_prod *= i

number = prime_prod
while True:
    failed = False
    for j in range(1,21):
        if not tls.divisible(number,j):
            print(f"{number} not divisible by {j}")
            failed = True
            break
    if not failed:
        print(number)
        break
    number += prime_prod