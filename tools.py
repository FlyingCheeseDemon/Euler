def divisible(a,b):
    if int(a/b) == a/b:
        return True
    return False

def is_prime(number):
    # it's not elegant, but it works
    if number <= 1:
        return False
    for i in range(2,number-1):
        if divisible(number,i):
            return False
    return True