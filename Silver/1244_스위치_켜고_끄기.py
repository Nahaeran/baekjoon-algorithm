N = int(input())
switches = list(map(int, input().split()))
num_students = int(input())
# m_list = []
# w_list = []
for _ in range(num_students):
    s, n = map(int, input().split())
    if s == 1:
        share = N // n
        for s in range(1, share + 1):
            ni = n * s - 1
            switches[ni] = int(not switches[ni])
    else:
        idx = n - 1
        switches[idx] = int(not switches[idx])
        temp = 1
        while True:
            i1 = idx + temp
            i2 = idx - temp
            if 0 <= i1 < N and 0 <= i2 < N and switches[i1] == switches[i2]:
                switches[i1] = int(not switches[i1])
                switches[i2] = int(not switches[i2])
            else:
                break
            temp += 1

# for i in range(len(m_list)):
#     share = N // m_list[i][1]
#     for s in range(1, share + 1):
#         ni = m_list[i][1] * s - 1
#         switches[ni] = int(not switches[ni])
#
# for i in range(len(w_list)):
#     idx = w_list[i][1] - 1
#     switches[idx] = int(not switches[idx])
#     temp = 1
#     while True:
#         i1 = idx + temp
#         i2 = idx - temp
#         if 0 <= i1 < N and 0 <= i2 < N and switches[i1] == switches[i2]:
#             switches[i1] = int(not switches[i1])
#             switches[i2] = int(not switches[i2])
#         else:
#             break
#         temp += 1

for i in range(0, N, 20):
    print(*switches[i:i+20])