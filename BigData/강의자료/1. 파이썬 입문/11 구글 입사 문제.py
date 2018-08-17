#range(1,10001)

count = 0
for i in range(10000):
    for j in str(i):
        if j == '8':
            count += 1 # count = count + 1
print (count)

str(list(range(10000))).count('8')

