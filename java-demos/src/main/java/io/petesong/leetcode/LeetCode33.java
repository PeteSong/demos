package io.petesong.leetcode;

import java.util.Objects;

/**
 * 33. Search in Rotated Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 */
class LeetCode33 {

  static class Solution {
    boolean validArgs(int[] nums, int target) {
      if (Objects.isNull(nums) || nums.length == 0 || nums.length > 5000) {
        return false;
      }
      if (target < (int) -1e4 || target > (int) 1e4) {
        return false;
      }
      return true;
    }

    boolean shiftLeft(int leftVal, int midVal, int rightVal, int key) {
      if (leftVal <= midVal) {
        if (leftVal <= key && key < midVal) {
          return true;
        } else {
          return false;
        }
      } else {
        if (midVal < key && key <= rightVal) {
          return false;
        } else {
          return true;
        }
      }
    }

    int searchRotatedSortedArray(int[] a, int key) {
      int left = 0;
      int right = a.length - 1;
      while (left <= right) {
        int mid = (left + right) >>> 1;
        int leftVal = a[left];
        int midVal = a[mid];
        int rightVal = a[right];
        if (key == midVal) {
          return mid;
        }
        if (shiftLeft(leftVal, midVal, rightVal, key)) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }
      return -1;
    }

    public int search(int[] nums, int target) {
      if (!validArgs(nums, target)) {
        return -1;
      }
      return searchRotatedSortedArray(nums, target);
    }

  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    int[] nums = {4, 5, 7, 9, 0, 2, 3};
    int target = 0;
    boolean isPassed = new LeetCode33.Solution().search(nums, target) == 4;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
