"""
# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/
"""


class Solution:
    def valid_args(self, nums: list[int], val: int):
        if nums is None or (not isinstance(nums, list)) or len(nums) == 0 or len(nums) > 100:
            return False
        if not isinstance(val, int) or val > 100 or val < 0:
            return False
        return True

    def removeElement(self, nums: list[int], val: int) -> int:
        if not self.valid_args(nums, val):
            return 0
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            if nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
        return p1


def main() -> None:  # pragma: no cover
    test_inputs = [([3, 2, 2, 3], 3, 2), ([2], 3, 1)]

    for nums, val, expected in test_inputs:
        k = Solution().removeElement(nums, val)
        print(nums[:k])
        assert k == expected


if __name__ == "__main__":
    main()
