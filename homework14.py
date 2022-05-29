import random


def sort_nums(nums):
    sorted_nums = nums.copy()
    for i in range(len(sorted_nums)):
        for j in range(i, len(sorted_nums)):
            if sorted_nums[i] > sorted_nums[j]:
                sorted_nums[i], sorted_nums[j] = sorted_nums[j], sorted_nums[i]

    return sorted_nums


numbers = [random.randint(0, 100) for _ in range(10)]
print('Initial list:', numbers)
print('Sorted list:', sort_nums(numbers))
