from typing import List

# def sorting_func(number):
#     result_negative = 0
#     result_positive = 0
#     for num in number:
#         if num < 0:
#             result_negative += num
#         elif num > 0:
#             result_positive += num
#     return result_positive, result_negative
#
#
# info = (sorting_func(int(x) for x in input().split()))
#
# print(info[1])
# print(info[0])
#
# if abs(info[1]) > info[0]:
#     print(f"The negatives are stronger than the positives")
#
# else:
#     print(f"The positives are stronger than the negatives")


def print_nums(number: List[int]) -> None:

    sum_negatives = sum(x for x in number if x < 0)
    sum_positives = sum(x for x in number if x > 0)

    print(sum_negatives)
    print(sum_positives)

    if sum_positives > abs(sum_negatives):
        print(f"The positives are stronger than the negatives")

    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
print_nums(numbers)