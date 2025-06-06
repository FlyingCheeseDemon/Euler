sum_of_squares = 0
sum = 0
for i in range(1,101):
    sum_of_squares += i*i
    sum += i

sqare_of_sums = sum*sum
print(sum_of_squares-sqare_of_sums)