"""
# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/
"""

from typing import Optional

from algorithms_learning.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = [root.left, root.right]
        while q:
            t1 = q.pop()
            t2 = q.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right)


def main() -> None:  # pragma: no cover
    #
    #        4
    #      /   \
    #    2       2
    #   / \     / \
    #  1   3   3   1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(1)
    assert Solution().isSymmetric(root)
    assert Solution().isSymmetric2(root)


if __name__ == "__main__":
    main()
