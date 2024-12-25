"""
Model Name: search.py
Description: Search algorithms
Author: Peter Song
Date: 2024-12-22
Version: 0.0.1
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
