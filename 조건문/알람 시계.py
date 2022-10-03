h, m = map(int, input().split())

if(m >= 45):
    m -= 45
    print(h, m)
else :
    if(h==0):
        h = 23
    else:
        h -= 1
    m = m-45 + 60
    print(h, m)