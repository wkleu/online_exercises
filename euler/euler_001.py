number_of_test_cases = int(input())
test_cases = []

for x in range(0, number_of_test_cases):
    test_case = int(input())
    test_cases.append(test_case)


def sum_multiples(num, limit):
    no_of_multiples = (limit - 1) // num
    return no_of_multiples * (no_of_multiples + 1) // 2 * num


def find_sum_of_all_multiples_of_3_and_5(input_amount):
    sum_of_div_by_3 = sum_multiples(3, input_amount)
    sum_of_div_by_5 = sum_multiples(5, input_amount)
    sum_of_div_by_15 = sum_multiples(15, input_amount)

    return sum_of_div_by_3 + sum_of_div_by_5 - sum_of_div_by_15


for test_case in test_cases:
    print(find_sum_of_all_multiples_of_3_and_5(test_case))
