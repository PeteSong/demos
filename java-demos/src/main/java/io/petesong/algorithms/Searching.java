package io.petesong.algorithms;

import java.util.Objects;

/**
 * Searching algorithms.
 */
public class Searching {
  /**
   * Binary search.
   *
   * @param a int array
   * @param key key to find
   * @return index in the arry, or -1 if no found.
   */
  public static int binarySearch(int[] a, int key) {
    if (Objects.isNull(a) || a.length == 0) {
      return -1;
    }
    int left = 0;
    int right = a.length - 1;
    return binarySearch(a, key, left, right);
  }

  /**
   * Binary search.
   *
   * @param a int array
   * @param key key to find
   * @param left from index
   * @param right to index
   * @return index in the array or -1 if not found.
   */
  public static int binarySearch(int[] a, int key, int left, int right) {
    if (Objects.isNull(a) || a.length == 0) {
      return -1;
    }
    while (left <= right) {
      int mid = (left + right) >>> 1;
      int midVal = a[mid];
      if (midVal == key) {
        return mid;
      }
      if (midVal < key) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return -1;
  }
}
