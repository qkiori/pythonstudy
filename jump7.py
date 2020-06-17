i = 7
j = 100
for a in range(0, j):
    a += 1
    if a % i == 0 or a % 10 == i or a//10 == i:
        print(str(a) + '   ****' + str(i))
    else:
        print(a)
