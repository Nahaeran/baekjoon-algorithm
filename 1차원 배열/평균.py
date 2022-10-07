n = int(input())
arr1 = list(map(int, input().split()))

M = max(arr1)

def newScore(n):
    return n / M * 100

arr2 = list(map(newScore, arr1))
print(sum(arr2)/len(arr2))