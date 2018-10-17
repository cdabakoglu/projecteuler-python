# This solution takes too long to reach answer. I did'n import any modules, I try to solve that pure Python.

i = 20
tot = 0
while True:
    for a in range(1,21):
        if i % a == 0:
            tot += 1
        else:
            tot = 0
            print("Not that:",i)
            i += 1

    if(tot >= 20):
        print("ANSWER:",i)
        break



# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
