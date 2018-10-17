i = 2
n = 600851475143

numbers = list()

while i <= n:
    if n % i == 0:
        n = n // i
        numbers.append(i)
    else:
        i += 1

print(max(numbers))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
