package com.leetcode.mergesortedarray;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class SolutionTest {

    @Test
    public void test_whenBothArraysAreEmpty() {
        Solution solution = new Solution();
        int[] nums1 = new int[0];
        int[] nums2 = new int[0];
        solution.merge(nums1, nums1.length - nums2.length, nums2, nums2.length);
        assertArrayEquals(new int[0], nums1);
    }

    @Test
    public void test_whenSecondArrayIsEmpty() {
        Solution solution = new Solution();
        int[] nums1 = new int[] { 1 };
        int[] nums2 = new int[0];
        solution.merge(nums1, nums1.length - nums2.length, nums2, nums2.length);
        assertArrayEquals(new int[] { 1 }, nums1);
    }

    @Test
    public void test_whenFirstArray_isLessThanSecondArray() {
        Solution solution = new Solution();
        int[] nums1 = new int[] { 0, 1, 0, 0, 0 };
        int[] nums2 = new int[] { 2, 3, 4 };
        solution.merge(nums1, nums1.length - nums2.length, nums2, nums2.length);
        assertArrayEquals(new int[] { 0, 1, 2, 3, 4 }, nums1);
    }

    @Test
    public void test_whenSecondArray_isLessThanFirstArray() {
        Solution solution = new Solution();
        int[] nums1 = new int[] { 2, 3, 4, 0, 0 };
        int[] nums2 = new int[] { 0, 1 };
        solution.merge(nums1, nums1.length - nums2.length, nums2, nums2.length);
        assertArrayEquals(new int[] { 0, 1, 2, 3, 4 }, nums1);
    }

    @Test
    public void test_whenArraysAreMixed() {
        Solution solution = new Solution();
        int[] nums1 = new int[] { 0, 4, 5, 0, 0, 0, 0};
        int[] nums2 = new int[] { 2, 3, 5, 6 };
        solution.merge(nums1, nums1.length - nums2.length, nums2, nums2.length);
        assertArrayEquals(new int[] { 0, 2, 3, 4, 5, 5, 6 }, nums1);
    }

}
