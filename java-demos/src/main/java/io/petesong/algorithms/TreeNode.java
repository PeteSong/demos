package io.petesong.algorithms;

import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

/**
 * Tree node for binary tree.
 */
public class TreeNode {
  @Getter
  @Accessors(fluent = true)
  private int val;

  @Getter @Setter
  @Accessors(fluent = true)
  private TreeNode left;

  @Getter @Setter
  @Accessors(fluent = true)
  private TreeNode right;

  /**
   * Instructor without parameters.
   */
  public TreeNode() {
  }

  /**
   * Instructor with one parameter.
   *
   * @param val value of int
   */
  public TreeNode(int val) {
    this.val = val;
  }

  /**
   * Instructor with three parameters.
   *
   * @param val Value
   * @param left Left node
   * @param right Right node
   */
  public TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
