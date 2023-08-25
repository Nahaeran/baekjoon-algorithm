w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dw = t % (2 * w)
dh = t % (2 * h)

p = p + dw
q = q + dh
if p > w:
    p = 2 * w - p
if q > h:
    q = 2 * h - q
if q < 0:
    q = -q
if p < 0:
    p = -p

print(p, q)