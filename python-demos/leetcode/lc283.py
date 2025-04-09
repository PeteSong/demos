"""
* 283. Move Zeroes
* https://leetcode.com/problems/move-zeroes/description/
"""


class Solution:
    def valid_args(self, nums: list[int]) -> bool:
        if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) < 1:
            return False
        if nums_len > 10**4:
            return False
        return all(isinstance(num, int) and -(2**31) <= num <= 2**31 - 1 for num in nums)

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not self.valid_args(nums):
            raise ValueError("Invalid input")

        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != p:
                    nums[p] = nums[i]
                    nums[i] = 0
                p += 1

    def move_zeros_to_head(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not self.valid_args(nums):
            raise ValueError("Invalid input")

        p = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                if i != p:
                    nums[p] = nums[i]
                    nums[i] = 0
                p -= 1

    def moveZeroes2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not self.valid_args(nums):
            raise ValueError("Invalid input")

        nums_len = len(nums)
        p = nums_len
        i = nums_len - 1
        while i >= 0:
            if nums[i] == 0:
                j = i
                while j < p - 1:
                    nums[j] = nums[j + 1]
                    j += 1
                p -= 1
                nums[p] = 0
            i -= 1


def main() -> None:  # pragma: no cover
    import copy

    inputs = [[0, 1, 0, 3, 12], [0]]

    for nums in copy.deepcopy(inputs):
        print(nums)
        Solution().moveZeroes(nums)
        print(nums)
        print()

    for nums in copy.deepcopy(inputs):
        print(nums)
        Solution().move_zeros_to_head(nums)
        print(nums)
        print()

    for nums in copy.deepcopy(inputs):
        print(nums)
        Solution().moveZeroes2(nums)
        print(nums)
        print()


if __name__ == "__main__":
    main()
