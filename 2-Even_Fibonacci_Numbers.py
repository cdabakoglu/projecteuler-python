a = 1
b = 2
fiboList = [1]
while b <= 4000000:
    fiboList.append(b)
    a,b = b, a+b


total = 0
for x in fiboList:
    if x % 2 == 0:
        total += x

print(total)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
