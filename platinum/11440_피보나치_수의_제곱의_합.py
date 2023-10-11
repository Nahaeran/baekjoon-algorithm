n = int(input())
dic = {}
m = 1000000007
def fibo(n):
    a = n // 3
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if not n in dic.keys():
            if n > 100:
                dic[n] = (fibo(a) * fibo(n-a+1) + fibo(a-1) * fibo(n-a)) % m
            else:
                dic[n] = (fibo(n-1) + fibo(n-2)) % m
    return dic[n]
print((fibo(n) % m) * (fibo(n+1) % m) % m)