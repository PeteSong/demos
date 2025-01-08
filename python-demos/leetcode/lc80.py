"""
# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
"""


class Solution:
    def valid_args(self, nums: list[int]) -> bool:
        if nums is None or not isinstance(nums, list) or len(nums) == 0:
            return False
        return True

    def removeDuplicates(self, nums: list[int]) -> int:
        if not self.valid_args(nums):
            return -1
        if (nums_len := len(nums)) <= 2:
            return nums_len
        p = 0
        for i in range(nums_len):
            if p < 2 or nums[p - 2] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p

    def removeDuplicates2(self, nums: list[int]) -> int:
        if not self.valid_args(nums):
            return -1

        if len(nums) <= 2:
            return len(nums)

        p = 0
        v = nums[0]
        c = 1
        for num in nums[1:]:
            if num == v:
                c += 1
                if c > 2:
                    continue
                p += 1
                nums[p] = v
            else:
                v = num
                p += 1
                nums[p] = v
                c = 1
        return p + 1


def main() -> None:  # pragma: no cover
    inputs = [[1, 1, 1, 2, 2, 3], [0, 0, 1, 1, 1, 1, 2, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4]]
    for nums in inputs:
        nums_copy = nums.copy()
        k = Solution().removeDuplicates(nums_copy)
        print(nums_copy[:k])
    for nums in inputs:
        nums_copy = nums.copy()
        k = Solution().removeDuplicates2(nums_copy)
        print(nums_copy[:k])


if __name__ == "__main__":
    main()
