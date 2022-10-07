case = int(input())
allPer = []

for i in range(case):
    cnt = 0
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    mean = sum(arr)/n
    for e in arr:
        if e>mean:
            cnt +=1
    per = "{:.3%}".format(cnt/n)
    allPer.append(per)

for i in allPer:
    print(i)