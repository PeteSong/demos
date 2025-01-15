"""
* 219. Contains Duplicate II
* https://leetcode.com/problems/contains-duplicate-ii/description/
"""


class Solution:
    def valid_args(self, nums: list[int], k: int):
        if (
            nums is None
            or k <= 0
            or not isinstance(nums, list)
            or (nums_len := len(nums)) <= 1
            or len(set(nums)) == nums_len
        ):
            return False
        return True

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if not self.valid_args(nums, k):
            return False
        nums_len = len(nums)
        if k > nums_len - 1:
            k = nums_len - 1
        for i in range(nums_len - 1):
            window_right_idx = min(i + k + 1, nums_len)
            for j in range(i + 1, window_right_idx):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        if not self.valid_args(nums, k):
            return False
        nums_len = len(nums)
        if k > nums_len - 1:
            k = nums_len - 1
        nums_map = {}
        for i, v in enumerate(nums):
            if v in nums_map and abs(nums_map[v] - i) <= k:
                return True
            nums_map[v] = i
        return False


def main() -> None:  # pragma: no cover
    nums = [1, 2, 3, 1]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))


if __name__ == "__main__":
    main()
