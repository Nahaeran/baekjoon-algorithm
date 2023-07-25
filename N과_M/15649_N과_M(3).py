from itertools import product

m, n = map(int, input().split(" "))
li = list(range(1, m+1))

for line in product(li, repeat=n):
    print(*line)