package io.petesong.leetcode;

import io.petesong.leetcode.LeetCode2235.Solution;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * LeetCode2235 test.
 */
public class LeetCode2235Test {
  static Stream<Arguments> intIntIntProvider() {
    return Stream.of(
        Arguments.arguments(0, 0, 0),
        Arguments.arguments(1, 1, 2),
        Arguments.arguments(9, 9, 18),
        Arguments.arguments(-9, 9, 0),
        Arguments.arguments(-9, -9, -18)
    );
  }

  @ParameterizedTest
  @MethodSource("intIntIntProvider")
  void fizzBuzz(int num1, int num2, int expected) {
    int actualResult = new Solution().sum(num1, num2);
    assertEquals(expected, actualResult);
  }

}
