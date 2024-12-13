package io.petesong.leetcode;

import java.util.stream.Stream;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

/**
 * LeetCode13 test.
 */
public class LeetCode13Test {
  static Stream<Arguments> stringIntProvider() {
    return Stream.of(
        Arguments.arguments(null, 0),
        Arguments.arguments("", 0),
        Arguments.arguments("A", 0),
        Arguments.arguments("MCMXCIV", 1994)
    );
  }

  @ParameterizedTest
  @MethodSource("stringIntProvider")
  void romanToInt(String s, int expected) {
    int actualResult = new LeetCode13.Solution().romanToInt(s);
    Assertions.assertEquals(actualResult, expected);
  }

}
