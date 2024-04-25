num = int(input())

if num <= 1:
    is_prime = False
elif num <= 3:
    is_prime = True
elif num % 2 == 0 or num % 3 == 0:
    is_prime = False
else:
    is_prime = True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            is_prime = False
            break
        i += 6

print(is_prime)