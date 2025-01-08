"""
Model Name: binary_tree.py
Description: Binary tree
Author: Peter Song
Date: 2025-12-30
Version: 0.0.1
"""

import copy
from typing import Any, Optional, Self


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node: Optional[TreeNode], space: int = 0, indent: int = 4) -> None:
    space += indent
    if node is None:
        print(f'{" " * space}#')
        return
    print_tree(node.right, space)
    print(f'{" " * space}{node.val}')
    print_tree(node.left, space)


def symmetric_tree2(root: Optional[TreeNode]) -> bool:
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


def symmetric_tree(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    return symmetric_nodes(root.left, root.right)


def symmetric_nodes(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    return symmetric_nodes(node1.left, node2.right) and symmetric_nodes(node1.right, node2.left)


def array_to_tree(a: Optional[list[int]]) -> Optional[TreeNode]:
    """
    General Binary Tree Representation:
      Similar to level-order traversal, but even if the child nodes of a certain
      node do not exist, leave a position in the array and fill it with None.
    """

    def get_node(v: Optional[int]) -> Optional[TreeNode]:
        if v is None:
            return None
        return TreeNode(val=v)

    if a is None or (a_len := len(a)) == 0:
        return None
    root = TreeNode(val=a[0])
    q: list[Optional[TreeNode]] = [root]
    i = 1
    while q and i < a_len:
        node = q.pop(0)
        if node is None:
            continue
        child_node = get_node(a[i])
        node.left = child_node
        q.append(child_node)

        i += 1
        if i < a_len:
            child_node = get_node(a[i])
            node.right = child_node
            q.append(child_node)
            i += 1
    return root


def tree_to_array(root: Optional[TreeNode], should_strip_trailing_nones: bool = False) -> Optional[list[Optional[int]]]:
    if root is None:
        return None
    q: list[Optional[TreeNode]] = [root]
    v_q: list[Optional[int]] = []
    while q:
        node = q.pop(0)
        if node:
            v_q.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            v_q.append(None)
    if should_strip_trailing_nones:
        while v_q and v_q[-1] is None:
            v_q.pop()
    return v_q


def arrays_equal(a1: list[Any], a2: list[Any]) -> bool:
    if a1 == a2:
        return True
    if a1 is None or a2 is None:
        return False
    a1_copy = copy.deepcopy(a1)
    a2_copy = copy.deepcopy(a2)
    while a1_copy and a1_copy[-1] is None:
        a1_copy.pop()
    while a2_copy and a2_copy[-1] is None:
        a2_copy.pop()
    return a1_copy == a2_copy


def main() -> None:  # pragma: no cover
    a = [4, 2, 6, 1, 3, 5, 7]
    # a = [4, 2, 6, 1, None, 5, None]
    # a = [4, 2, None, None, None, None]
    root = array_to_tree(a)
    print_tree(root)
    print(tree_to_array(root))


if __name__ == "__main__":
    main()
