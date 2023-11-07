import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
idx_list_in = [0] * (n + 1)

for i in range(n):
    idx_list_in[inorder[i]] = i


def make_preorder(in_f, in_e, post_f, post_e):
    if in_f > in_e or post_f > post_e:
        return

    root = postorder[post_e]
    root_in_idx = idx_list_in[root]

    print(root, end=" ")
    make_preorder(in_f, root_in_idx - 1, post_f, post_f + (root_in_idx - 1 - in_f))
    make_preorder(root_in_idx + 1, in_e, post_f + (root_in_idx - 1 - in_f) + 1, post_e - 1)


make_preorder(0, n - 1, 0, n - 1)
