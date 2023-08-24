def check(x1, y1, p1, q1, x2, y2, p2, q2):
    points1 = [(x1, y1), (x1, q1), (p1, y1), (p1, q1)]
    points2 = [(x2, y2), (x2, q2), (p2, y2), (p2, q2)]

    for dot in points1:
        if (x2 < dot[0] < p2 and dot[1] == y2) or\
                (x2 < dot[0] < p2 and dot[1] == q2) or\
                (dot[0] == x2 and y2 < dot[1] < q2) or\
                (dot[0] == q2 and y2 < dot[1] < q2):
            return 'b'

        if dot in points2:
            return 'c'
    for dot in points2:
        if (x1 < dot[0] < p1 and dot[1] == y1) or\
                (x1 < dot[0] < p1 and dot[1] == q1) or\
                (dot[0] == x1 and y1 < dot[1] < q1) or\
                (dot[0] == q1 and y1 < dot[1] < q1):
            return 'b'

    if p1 < x2 or q1 < y2 or p2 < x2 or q2 < y1:
        return 'd'
    return 'a'


for _ in range(4):
    points = map(int, input().split())
    print(check(*points))