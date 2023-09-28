import sys
input = sys.stdin.readline

memory = {1:1,2:1,3:2,4:3,5:5}
INF = 1000000000
def Fibo(n):
  if memory.get(n):
    return memory[n]
  else:
    if n%2 == 1:
      memory[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2)%INF
    else:
      memory[n] = (Fibo(n+1)-Fibo(n-1))%INF
    return memory[n]


a,b = map(int,input().split())
print((Fibo(b+2)-Fibo(a+1))%INF)