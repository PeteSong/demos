package io.petesong.leetcode;

import io.petesong.algorithms.BinaryTree;
import io.petesong.algorithms.TreeNode;
import io.petesong.leetcode.LeetCode101.Solution;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * LeetCode101 test.
 */
public class LeetCode101Test {
  static Stream<Arguments> booleanIntegerArrayProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(true, null),
        Arguments.arguments(true, new Integer[0]),

        // normal cases
        Arguments.arguments(true, new Integer[]{1, 2, 2, 3, 4, 4, 3}),
        Arguments.arguments(true, new Integer[]{1, 2, 2, 3, null, null, 3}),
        Arguments.arguments(false, new Integer[]{1, 2, 2, 3, null, 3, null})
    );
  }

  @ParameterizedTest
  @MethodSource("booleanIntegerArrayProvider")
  void testIsSymmetric(boolean expected, Integer[] a) {
    TreeNode root = BinaryTree.fromArray(a);
    boolean actualResult = new Solution().isSymmetric(root);
    Assertions.assertEquals(expected, actualResult);
  }

}
