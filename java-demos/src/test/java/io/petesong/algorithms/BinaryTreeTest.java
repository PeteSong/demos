package io.petesong.algorithms;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * BinaryTree.java test.
 */
public class BinaryTreeTest {
  static Stream<Arguments> treeNodeIntegerArrayProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(null, null),
        Arguments.arguments(null, new Integer[0])
    );
  }

  @ParameterizedTest
  @MethodSource("treeNodeIntegerArrayProvider")
  void testEdgeCases(TreeNode expected, Integer[] a) {
    TreeNode actualResult = BinaryTree.fromArray(a);
    Assertions.assertEquals(expected, actualResult);
  }

  static Stream<Arguments> integerArrayProvider() {
    return Stream.of(
        // Normal cases
        Arguments.arguments((Object) new Integer[]{4, 2, 6, 1, 3, 5, 7}),
        Arguments.arguments((Object) new Integer[]{4, 2, 6, 1, null, 5, null})
    );
  }

  @ParameterizedTest
  @MethodSource("integerArrayProvider")
  void testNormalCases(Integer[] a) {
    TreeNode root = BinaryTree.fromArray(a);
    BinaryTree.print(root);
    Integer[] a1 = BinaryTree.toArray(root);
    Assertions.assertTrue(BinaryTree.areArraysEqual(a, a1));
  }

  @Test
  void shouldReturnEmptyArrayWhenToArrayWithNull() {
    var result = BinaryTree.toArray(null);
    Assertions.assertTrue(result.length == 0);
  }
}
