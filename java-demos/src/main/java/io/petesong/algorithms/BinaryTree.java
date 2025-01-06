package io.petesong.algorithms;


import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.stream.Collectors;

/**
 * Binary tree.
 */
public class BinaryTree {
  private static TreeNode getNode(Integer val) {
    if (Objects.isNull(val)) {
      return null;
    }
    return new TreeNode(val);
  }


  /**
   * Generate a binary tree from an array.
   *
   * @param a Array of Integer
   * @return root node.
   */
  public static TreeNode fromArray(Integer[] a) {
    if (Objects.isNull(a) || a.length == 0) {
      return null;
    }
    var root = new TreeNode(a[0]);
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    var i = 1;
    while (q.size() > 0 && i < a.length) {
      TreeNode node = q.remove();
      if (Objects.isNull(node)) {
        continue;
      }
      var childNode = getNode(a[i]);
      node.setLeft(childNode);
      q.add(childNode);

      i++;
      if (i < a.length) {
        childNode = getNode(a[i]);
        node.setRight(childNode);
        q.add(childNode);
        i++;
      }
    }
    return root;
  }

  /**
   * Convert a binary tree to an array which is of General Binary Tree Representation.
   *
   * @param root                     Root node of the binary tree
   * @param shouldStripTrailingNulls strip trailing nulls or not
   * @return array of Integer
   */
  public static Integer[] toArray(TreeNode root, boolean shouldStripTrailingNulls) {
    if (Objects.isNull(root)) {
      return new Integer[0];
    }
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    List<Integer> values = new ArrayList<>();
    while (q.size() > 0) {
      var node = q.remove();
      if (Objects.nonNull(node)) {
        values.add(node.getVal());
        q.add(node.getLeft());
        q.add(node.getRight());
      } else {
        values.add(null);
      }
    }
    if (shouldStripTrailingNulls) {
      stripTrailingNulls(values);
    }
    Integer[] result = values.stream().toArray(Integer[]::new);
    return result;
  }

  /**
   * Convert a binary tree to an array which is of General Binary Tree Representation.
   *
   * @param root Root node of the binary tree
   * @return an array of Integer
   */
  public static Integer[] toArray(TreeNode root) {
    return toArray(root, true);
  }

  /**
   * Print the binary tree.
   *
   * @param root   Root node of the binary tree
   * @param space  space count
   * @param indent indent count
   */
  public static void print(TreeNode root, int space, int indent) {
    space += indent;
    if (Objects.isNull(root)) {
      System.out.printf("%s#%n", " ".repeat(space));
      return;
    }
    print(root.getRight(), space, indent);
    System.out.printf("%s%d%n", " ".repeat(space), root.getVal());
    print(root.getLeft(), space, indent);
  }

  /**
   * Print the binary tree.
   *
   * @param root Root node of the binary tree
   */
  public static void print(TreeNode root) {
    print(root, 0, 2);
  }

  /**
   * Strip the trailing nulls.
   *
   * @param l list of Integer
   * @return self of l
   */
  private static List<Integer> stripTrailingNulls(List<Integer> l) {
    while (l.size() > 0 && Objects.isNull(l.getLast())) {
      l.removeLast();
    }
    return l;
  }

  /**
   * Check two arrays are same of not after removing the trailing nulls.
   *
   * @param a1 one Integer array
   * @param a2 another Integer array
   * @return true or false
   */
  public static boolean areArraysEqual(Integer[] a1, Integer[] a2) {
    if (Arrays.equals(a1, a2)) {
      return true;
    }
    var l1 = Arrays.stream(a1).collect(Collectors.toList());
    var l2 = Arrays.stream(a2).collect(Collectors.toList());
    l1 = stripTrailingNulls(l1);
    l2 = stripTrailingNulls(l2);
    return l1.equals(l2);
  }

  /**
   * Main method.
   *
   * @param args Arguments
   */
  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    // Integer[] a = {4, 2, 6, 1, 3, 5, 7};
    Integer[] a = {4, 2, 6, 1, null, 5, 7};
    var root = BinaryTree.fromArray(a);
    BinaryTree.print(root);
    var a1 = BinaryTree.toArray(root);
    System.out.println(Arrays.toString(a));
    System.out.println(Arrays.toString(a1));
    System.out.printf("Same: %b", areArraysEqual(a, a1));
  }
}
