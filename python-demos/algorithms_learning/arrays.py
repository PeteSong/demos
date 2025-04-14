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

from collections import deque
from collections.abc import Generator


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
    if nums is None or not isinstance(nums, list):
        return nums

    nums_len = len(nums)
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
    Insert the element into its correct position in the sorted portion.
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
    Find the smallest element from the unsorted portion each time and place it at the end of the sorted portion.
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


def quick_sort(nums: list[int]) -> list[int]:
    """
    Choose a pivot element and divide the array into two parts:
    elements smaller than the pivot go on the left,
    and elements larger than the pivot go on the right.
    选择一个基准元素，将数组分成两部分，小于基准的在左，大于基准的在右。
    """
    if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) == 0:
        return nums

    if (nums_len := len(nums)) <= 1:
        return nums

    pivot = nums[nums_len // 2]
    left = [n for n in nums if n < pivot]
    middle = [n for n in nums if n == pivot]
    right = [n for n in nums if n > pivot]
    return quick_sort(left) + middle + quick_sort(right)


NLE_TYPES = (int, float, str, bool)
NLE = int | float | str | bool
NestedList = NLE | list["NestedList"]


def _is_valid_nested_list(_nums: NestedList) -> bool:
    if isinstance(_nums, NLE_TYPES):
        return True

    if isinstance(_nums, list):
        return all(_is_valid_nested_list(_n) for _n in _nums)

    return False


def flatten_list_recurision(nums: NestedList) -> list[NLE]:
    if not _is_valid_nested_list(nums):
        raise ValueError("Input should be a valid nested list")

    if not isinstance(nums, list):
        return [nums]

    result = []
    for n in nums:
        result.extend(flatten_list_recurision(n))
    return result


def flatten_list_generator(nums: NestedList) -> Generator[NLE, None, None]:
    if not _is_valid_nested_list(nums):
        raise ValueError("Input should be a valid nested list")

    if not isinstance(nums, list):
        yield nums
        return

    for n in nums:
        yield from flatten_list_generator(n)


def flatten_list(nums: NestedList) -> list[NLE]:
    if not _is_valid_nested_list(nums):
        raise ValueError("Input should be a valid nested list")

    if not isinstance(nums, list):
        return [nums]

    result = []
    stack = deque(nums)
    # stack.append(nums)
    while stack:
        elem = stack.popleft()
        if not isinstance(elem, list):
            result.append(elem)
        else:
            stack.extendleft(reversed(elem))
    return result


def rotate90(matrix: list[list[int]], clockwise=True) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    def _valid_args(matrix: list[list[int]]) -> bool:
        if matrix is None or not isinstance(matrix, list) or (matrix_len := len(matrix)) == 0:
            return False
        if any(row is None or not isinstance(row, list) or len(row) != matrix_len for row in matrix):
            return False
        if any(elem is None or not isinstance(elem, int) for row in matrix for elem in row):
            return False
        return True

    if not _valid_args(matrix):
        raise ValueError("Invalid argument")

    matrix_len = len(matrix)
    # transpose the matrix
    for i in range(matrix_len):
        for j in range(i + 1, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    if clockwise:
        # reverse each row
        for i in range(matrix_len):
            matrix[i].reverse()
    else:
        # reverse each column
        for i in range(matrix_len // 2):
            for j in range(matrix_len):
                matrix[i][j], matrix[matrix_len - i - 1][j] = matrix[matrix_len - i - 1][j], matrix[i][j]


if __name__ == "__main__":  # pragma: no cover
    # nums = [1, 2, [4.5, "5", ["A", 11]]]
    # nums = [1, [True, 2], 3.3, ["4", 5]]
    # print(flatten_list_recurision(nums))
    # print(flatten_list(nums))
    # print(list(flatten_list_generator(nums)))
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    rotate90(matrix)
    print(matrix)
    rotate90(matrix, False)
    print(matrix)
