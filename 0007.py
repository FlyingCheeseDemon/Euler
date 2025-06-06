import tools as tls

inx = 1
num = 2
while inx < 10002:
    if tls.is_prime(num):
        inx += 1
        if tls.divisible(inx,100):
            print(f"inx: {inx}")
    num += 1
print(num-1)