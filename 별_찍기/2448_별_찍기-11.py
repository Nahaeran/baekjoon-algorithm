n = int(input())

def fractal_triangle(num):
    if num == 3:
        return ["  *   ", " * *  ", "***** "]
    
    result = []
    lst = fractal_triangle(num // 2)

    # 첫 번째 줄
    for e in lst:
        result.append(f"{e:^{2 * num}}")
    # 두 번째 줄
    for e in lst:
        result.append(2 * e)

    return result

# 출력
triangle = fractal_triangle(n)
for i in range(n):
    print(triangle[i])
