"""
# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
"""

import heapq
from collections import Counter


class Solution:
    def valid_arg(self, nums: list[int], k: int) -> bool:
        if nums is None or not isinstance(nums, list) or (nums_len := len(nums)) == 0 or nums_len > 10**5:
            return False
        if k is None or not isinstance(k, int) or k < 1 or k > len(set(nums)):
            return False
        return all(isinstance(num, int) and -(10**4) <= num <= 10**4 for num in nums)

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if not self.valid_arg(nums, k):
            raise ValueError("Invalid arguments")
        counter = Counter(nums)
        # use `Counter.most_common`
        # return [elem for elem, _ in counter.most_common(k)]

        # use min-heap
        min_heap = []
        for num, freq in counter.items():
            item = freq, num
            if len(min_heap) < k:
                heapq.heappush(min_heap, item)
            else:
                heapq.heappushpop(min_heap, item)
        return [num for _, num in min_heap]


def main() -> None:  # pragma: no cover
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))


if __name__ == "__main__":
    main()
