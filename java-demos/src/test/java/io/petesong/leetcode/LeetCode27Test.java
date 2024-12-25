package io.petesong.leetcode;

import io.petesong.leetcode.LeetCode27.Solution;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * LeetCode27 test.
 */
public class LeetCode27Test {
  static Stream<Arguments> intArrayIntIntProvider() {
    return Stream.of(
        Arguments.arguments(null, 0, 0),
        Arguments.arguments(new int[0], 0, 0),
        Arguments.arguments(new int[1], -1, 0),
        Arguments.arguments(new int[1], 110, 0),
        Arguments.arguments(new int[101], 110, 0),

        Arguments.arguments(new int[]{3, 2, 2, 3}, 2, 2),
        Arguments.arguments(new int[]{0, 1, 2, 2, 3, 0, 4, 2}, 2, 5),
        Arguments.arguments(new int[]{0, 1, 2, 2, 3, 0, 4, 2}, 98, 8)
    );
  }

  @ParameterizedTest
  @MethodSource("intArrayIntIntProvider")
  void removeElement(int[] nums, int val, int expected) {
    int actualResult = new Solution().removeElement(nums, val);
    Assertions.assertEquals(expected, actualResult);
  }

}
