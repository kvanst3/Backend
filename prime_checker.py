lst = [*range(1, 101)]
prime_lst = []

for num in lst:
    for i in range(num):
        is_prime = True
        if (i+1) != num and (i+1) != 1:
            if num % (i+1) == 0:
                is_prime = False
                break
    if is_prime:
        prime_lst.append(num)

print(prime_lst)
