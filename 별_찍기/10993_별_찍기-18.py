n = int(input())

def get_width(num):
    if num == 1:
        return 1
    return (2 * get_width(num) + 3)

def get_height(num):
    if num == 1:
        return 1
    return (2 * get_height(num) + 1)

def triangle(num):
    if num == 1:
        return ["*"]
    
    result = []
    before_stars = triangle(num-1)

    # 짝수면 뒤집힌 삼각형 모양
    if num % 2 == 0:
        pass
    else: 
        pass


result = triangle(n)

# 2n+3