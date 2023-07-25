n = int(input())

def make_box(num):
    if num == 1:
        return ["*"]
    
    width = 4 * num - 3
    result = []
    before_box = make_box(num-1)

    # 첫 번째 줄
    result.append(f"{'*' * width}")
    # 두 번째 줄
    result.append(f"*{' ' * (width-2)}*")
    # 덩어리
    for e in before_box:
        result.append(f"* {e} *")
    # 마지막-1 줄
    result.append(f"*{' ' * (width-2)}*")
    # 마지막 줄
    result.append(f"{'*' * width}")

    return result

box = make_box(n)
for line in box:
    print(line)