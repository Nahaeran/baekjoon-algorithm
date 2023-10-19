import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
head = 0
node_list = [False] * (N + 1)
checked = [False] * (N + 1)
result = ''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = []
        self.right = []

    def add_left(self, l):
        self.left.append(l)

    def add_right(self, r):
        self.right.append(r)


def traversal(num):
    global result
    node = node_list[num]
    for l in node.left:
        if not checked[l]:
            traversal(l)
    if not checked[num]:
        result += f"{num} "
        checked[num] = True
    for r in node.right:
        if not checked[r]:
            traversal(r)


for i in range(M):
    p, n = map(int, sys.stdin.readline().split())
    if i == 0 or n == head:
        head = p
    if not node_list[p]:
        node_list[p] = Node(p)
    if not node_list[n]:
        node_list[n] = Node(n)
    node_list[p].add_right(n)
    node_list[n].add_left(p)

traversal(head)
for i in range(1, N + 1):
    if not checked[i] and node_list[i]:
        traversal(i)
    elif not node_list[i]:
        result += f'{i} '
print(result[:-1])
