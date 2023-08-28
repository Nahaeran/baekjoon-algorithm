def removeKdigits(num: str, k: int) -> str:
    # N = len(num)
    # removed_subset = []
    # for i in range(1<<N):
    #     subset = []
    #     for j in range(N):
    #         if i & (1<<j):
    #             subset.append(num[j])
    #     if subset and len(subset) == N - k:
    #         removed_subset.append(subset)
    # if removed_subset:
    #     all_num = ["".join(x) for x in removed_subset]
    #     result = str(int(min(all_num)))
    # else:
    #     result = "0"
    # return result
    N = len(num)
    if N == k:
        return "0"

    while k != 0:
        # li = []
        for i in range(len(num)):
            temp = num.replace(num[i], "", 1)
            # li.append(temp)
            if num > temp:
                num = temp
                break

        # num = min(li)
        k -= 1
    num = num.lstrip("0")
    if num == "":
        return "0"
    return num
    # if lst:
    #     new_num = min(lst)
    #     result = removeKdigits(new_num, k - 1)
    #     return result

    # N = len(num)
    # if N == k:
    #     return "0"
    # # removed = ""
    # min_num = num
    # for i in range(1 << N):
    #     subset = ""
    #     for j in range(N):
    #         if i & (1 << j):
    #             subset += num[j]
    #     if len(subset) == N - k and min_num > subset:
    #         min_num = str(int(subset))
    # # if removed_subset:
    # #     all_num = ["".join(x) for x in removed_subset]
    # #     result = str(int(min(all_num)))
    # # else:
    # #     result = "0"
    # return min_num

test_num = input("num: ")
test_k = int(input("k: "))
print(removeKdigits(test_num, test_k))

