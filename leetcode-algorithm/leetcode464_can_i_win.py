def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    li = list(range(1, maxChoosableInteger + 1))
    if sum(li) < desiredTotal:
        return False

    memo = {}

    def dp(lst, remain_total):
        if lst[-1] >= remain_total:
            return True
        for i in range(len(lst)):
            input_lst = lst[:i] + lst[i + 1:]
            input_total = remain_total - lst[i]
            if memo.get((input_lst, input_total)) == None:
                memo[(input_lst, input_total)] = dp(input_lst, input_total)
            if memo.get((input_lst, input_total)) == False:
                return True
        print(memo)
        return False

    return dp(tuple(li), desiredTotal)


print(canIWin(10, 40))