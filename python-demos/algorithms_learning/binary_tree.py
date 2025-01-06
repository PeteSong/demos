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


def print_tree(node: Optional[TreeNode], space: int = 0, ident: int = 4) -> None:
    if node is None:
        print(f'{" " * space}#')
        return
    print_tree(node.right, space + ident)
    print(f'{" " * space}{node.val}')
    print_tree(node.left, space + ident)


def array_to_tree(a: Optional[list[int]]) -> Optional[TreeNode]:
    """
    General Binary Tree Representation:
      Similar to level-order traversal, but even if the child nodes of a certain
      node do not exist, leave a position in the array and fill it with None.
    """

    def get_child_node(v: Optional[int]) -> Optional[TreeNode]:
        if v is None:
            return None
        else:
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
        child_node = get_child_node(a[i])
        node.left = child_node
        q.append(child_node)

        i += 1
        if i < a_len:
            child_node = get_child_node(a[i])
            node.right = child_node
            q.append(child_node)
            i += 1
    return root


def tree_to_array(root: Optional[TreeNode]) -> Optional[list[Optional[int]]]:
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
    return v_q


def same_arrays(a1: list[Any], a2: list[Any]) -> bool:
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
    # a = [4, 2, 6, 1, 3, 5, 7]
    # a = [4, 2, 6, 1, None, 5, None]
    a = [4, 2, None, None, None, None]
    root = array_to_tree(a)
    print_tree(root)
    print(tree_to_array(root))
