n = int(input())

def fractal_rectangle(num):
    if num == 1:
        return ["*"]

    result = []
    lst = fractal_rectangle(num // 3)

    # 첫 번째 줄
    for e in lst:
        result.append(e * 3)
    # 두 번째 줄
    for e in lst:
        result.append(e + (" " * (num // 3)) + e)
    # 세 번째 줄
    for e in lst:
        result.append(e * 3)

    return result

# 출력
rectangle = fractal_rectangle(n)
for i in range(n):
    print(rectangle[i])
