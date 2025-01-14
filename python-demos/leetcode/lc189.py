"""
* 189. Rotate Array
* https://leetcode.com/problems/rotate-array/description/
"""


class Solution:
    def valid_args(self, nums: list[int], k: int) -> bool:
        if nums is None or not isinstance(nums, list) or len(nums) == 0 or k <= 0:
            return False
        return True

    def rotate(self, nums: list[int], k: int) -> None:
        if not self.valid_args(nums, k):
            return
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums: list[int], k: int) -> None:
        if not self.valid_args(nums, k):
            return
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def rotate3(self, nums: list[int], k: int) -> None:
        if not self.valid_args(nums, k):
            return
        double_list = []
        double_list.extend(nums)
        double_list.extend(nums)
        nums_len = len(nums)
        k = k % nums_len
        for i in range(nums_len):
            nums[i] = double_list[nums_len - k + i]

    def rotate4(self, nums: list[int], k: int) -> None:
        if not self.valid_args(nums, k):
            return
        copied_array = nums[:]
        nums_len = len(nums)
        k = k % nums_len
        for i in range(nums_len):
            nums[(i + k) % nums_len] = copied_array[i]


def main() -> None:  # # pragma: no cover
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    assert [5, 6, 7, 1, 2, 3, 4] == nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate2(nums, k)
    assert [5, 6, 7, 1, 2, 3, 4] == nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate3(nums, k)
    assert [5, 6, 7, 1, 2, 3, 4] == nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate4(nums, k)
    assert [5, 6, 7, 1, 2, 3, 4] == nums


if __name__ == "__main__":
    main()
