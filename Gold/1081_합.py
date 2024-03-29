def decimal_sum(num, idx):
    if num < 0:
        return 0

    sum_lst = 0
    if idx == 1:
        sum_lst += num // 10 ** idx * 45
        sum_lst += sum(range(num % 10 ** idx + 1))

        return sum_lst

    if idx >= 2:
        digit_now = (num % 10 ** idx - num % 10 ** (idx - 1)) // 10 ** (idx - 1)

        sum_lst += (num - num % (10 ** idx)) // 10 * 45

        for i in range(1, digit_now):
            sum_lst += i * 10 ** (idx - 1)
        sum_lst += (num % 10 ** idx - num % 10 ** (idx - 1)) // 10 ** (idx - 1) * (num % 10 ** (idx - 1) + 1)
        return sum_lst + decimal_sum(num, idx - 1)


num1, num2 = map(int, input().split())
print(decimal_sum(num2, len(str(num2))) - decimal_sum(num1 - 1, len(str(num1))))