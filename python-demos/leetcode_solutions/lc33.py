"""
# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


class Solution:
    def valid_args(self, nums: list[int], target: int) -> bool:
        if nums is None or (not isinstance(nums, list)) or len(nums) == 0:
            return False
        if not isinstance(target, int):
            return False
        return True

    def search(self, nums: list[int], target: int) -> int:
        def binary_search_on_rotated_list() -> int:
            def need_shift_left() -> bool:
                if left_val <= mid_val:
                    if left_val <= target < mid_val:
                        return True
                    else:
                        return False
                else:
                    if mid_val < target <= right_val:
                        return False
                    else:
                        return True

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                left_val, mid_val, right_val = nums[left], nums[mid], nums[right]
                if mid_val == target:
                    return mid
                if need_shift_left():
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if not self.valid_args(nums, target):
            return -1

        return binary_search_on_rotated_list()

    def search2(self, nums: list[int], target: int) -> int:
        if not self.valid_args(nums, target):
            return -1
        if target in nums:
            return nums.index(target)
        return -1


def main() -> None:  # pragma: no cover
    f = Solution().search

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert f(nums, target) == 4

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    assert f(nums, target) == 3

    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    assert f(nums, target) == 4

    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 1
    assert f(nums, target) == 5

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert f(nums, target) == -1

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 4
    assert f(nums, target) == 0

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    assert f(nums, target) == 6


if __name__ == "__main__":
    main()
