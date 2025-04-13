"""
# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/
"""

from collections import Counter, defaultdict


class Solution:
    def valid_arg(self, words: list[str], k: int) -> bool:
        if words is None or not isinstance(words, list) or (nums_len := len(words)) == 0 or nums_len > 500:
            return False
        if k is None or not isinstance(k, int) or k < 1 or k > len(set(words)):
            return False
        return all(isinstance(word, str) and 1 <= len(word) <= 10 for word in words)

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        if not self.valid_arg(words, k):
            raise ValueError("Invalid arguments")

        counter = Counter(words)
        freq_words = defaultdict(list)

        for word, freq in counter.items():
            freq_words[freq].append(word)

        result = []
        for freq in sorted(freq_words.keys(), reverse=True):
            if len(result) >= k:
                break
            result.extend(sorted(freq_words[freq]))
        return result[:k]


def main() -> None:  # pragma: no cover
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(words, k))
    k = 3
    print(solution.topKFrequent(words, k))
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(solution.topKFrequent(words, k))


if __name__ == "__main__":
    main()
