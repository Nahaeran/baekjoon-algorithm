import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = [[0] * N for _ in range(N)]

for i in range(N):
    for start in range(N - i):
        end = start + i # 회문 확인할 끝지점과 시작지점 설정
        if start == end: # 단어가 1글자면
            check[start][end] = 1 # 회문이니 체크
        elif num[start] == num[end]: # 첫문자랑 끝문자랑 같으면
            if start + 1 == end: # 단어가 2글자면
                check[start][end] = 1 #회문이니 체크
            elif check[start+1][end-1] == 1: # 만약 가운데 애들이 회문이면
                check[start][end] = 1 # 얘는 결국 회문이니 체크

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(check[S - 1][E - 1])
