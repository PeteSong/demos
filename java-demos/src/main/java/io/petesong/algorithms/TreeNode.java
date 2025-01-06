package io.petesong.algorithms;

import lombok.Getter;
import lombok.Setter;

/**
 * Tree node for binary tree.
 */
class TreeNode {
  @Getter
  private int val;

  @Getter @Setter
  private TreeNode left;

  @Getter @Setter
  private TreeNode right;

  public TreeNode() {
  }

  public TreeNode(int val) {
    this.val = val;
  }

  public TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
