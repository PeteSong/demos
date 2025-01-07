package io.petesong.leetcode;

import io.petesong.algorithms.BinaryTree;
import io.petesong.algorithms.TreeNode;

import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

/**
 * 101. Symmetric Tree
 * https://leetcode.com/problems/symmetric-tree/description/
 */
class LeetCode101 {

  static class Solution {
    public boolean isSymmetric(TreeNode root) {
      if (Objects.isNull(root)) {
        return true;
      }
      Queue<TreeNode> q = new LinkedList<>();
      q.add(root.left());
      q.add(root.right());
      while (q.size() > 0) {
        TreeNode n1 = q.remove();
        TreeNode n2 = q.remove();
        if (Objects.isNull(n1) && Objects.isNull(n2)) {
          continue;
        }
        if (Objects.isNull(n1) || Objects.isNull(n2)) {
          return false;
        }
        if (n1.val() != n2.val()) {
          return false;
        }
        q.add(n1.left());
        q.add(n2.right());
        q.add(n1.right());
        q.add(n2.left());
      }
      return true;
    }
  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    var a = new Integer[]{1, 2, 2, 3, 4, 4, 3};
    var root = BinaryTree.fromArray(a);
    boolean isPassed = new LeetCode101.Solution().isSymmetric(root) == true;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
