"""
Model Name: search.py
Description: Search algorithms
Author: Peter Song
Date: 2024-12-22
Version: 0.0.1

Model Name: arrays.py
Description: Algorithms on arrays
Author: Peter Song
Date: 2025-01-14
Version: 0.0.2
Changes:
  rename from "search.py" to "arrays.py"
"""


def binary_search(nums: list[int], target: int, left: int = 0, right: int = None) -> int:
    """Binary search on sorted list"""
    if nums is None or len(nums) == 0:
        return -1
    if right is None:
        right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = nums[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def reverse(nums: list[int], p1: int = 0, p2: int = 0) -> None:
    if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) <= 1:
        return
    if p1 <= 0:
        p1 = 0
    if p2 is None or p2 <= 0 or p2 > nums_len - 1:
        p2 = nums_len - 1
    while p1 < p2:
        nums[p1], nums[p2] = nums[p2], nums[p1]
        p1 += 1
        p2 -= 1


def bubble_sort(nums: list[int]) -> list[int]:
    """
    每次比较相邻两个元素，将较大的元素“冒泡”到数组末尾。
    """
    if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) == 0:
        return nums
    for i in range(nums_len):
        swapped = False
        for j in range(0, nums_len - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


def insertion_sort(nums: list[int]) -> list[int]:
    """
    将元素插入到已排序部分的正确位置。
    """
    if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) == 0:
        return nums
    for i in range(1, nums_len):
        val = nums[i]
        j = i - 1
        while j >= 0 and val < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = val
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    """
    每次从未排序部分找到最小的元素，放到已排序部分的末尾。
    """
    if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) == 0:
        return nums
    for i in range(nums_len):
        min_idx = i
        for j in range(i + 1, nums_len):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums
