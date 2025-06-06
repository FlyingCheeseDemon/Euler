# the product of two three digit numbers has 5 or 6 digits
# 100*100 = 10000
# 999*999 is just smaller than 1000000

def is_palindrome(num):
    numstr = str(num)
    if numstr[::-1] == numstr:
        return True
    return False

biggest_palindrome = 0
for i in range(100,999):
    for j in range(100,999):
        prod = i*j
        if is_palindrome(prod) and prod > biggest_palindrome:
            biggest_palindrome = prod

print(biggest_palindrome)