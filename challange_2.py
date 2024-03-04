
def max_sum_equal_digit_sum(A):
    digit_sums = {}
    for num in A:
        num_sum = 0
        while num > 0:
            num_sum += num % 10
            num //= 10
        if num_sum in digit_sums:
            digit_sums[num_sum].append(num)
        else:
            digit_sums[num_sum] = [num]

    max_sum = -1
    for num1 in A:
        for num2 in A:
            if num1 != num2:
                num1_sum = 0
                while num1 > 0:
                    num1_sum += num1 % 10
                    num1 //= 10
                if num2_sum := (num_sum - num1_sum) in digit_sums:
                    if num2 in digit_sums[num2_sum]:
                        max_sum = max(max_sum, num1 + num2)

    return max_sum