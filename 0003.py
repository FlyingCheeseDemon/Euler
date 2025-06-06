number = 600851475143

def is_prime(number):
    # it's not elegant, but it works
    for i in range(2,number-1):
        if int(number/i) == number/i:
            return False
    return True

def remove_factor(num):
    if is_prime(num):
        return num, 1
    
    for i in range(2,num):
        if is_prime(i) and (int(num/i) == num/i):
            return i, int(num/i)

factors = [] 
while number != 1:
    factor, number = remove_factor(number)
    print(factor, number)
    factors.append(factor)

print(factors)