package com.leetcode.mergesortedarray;

public class Solution {
    // initial solution
    public void merge1(int[] nums1, int m, int[] nums2, int n) {
        if (nums1.length == 0 || nums2.length == 0) {
            return;
        }

        int[] result = new int[n + m];

        int pointer1 = 0;
        int pointer2 = 0;

        for (int i = 0; i < n + m; i++) {
            if (pointer1 == m) {
                System.arraycopy(nums2, pointer2, result, i, n - pointer2);
                break;
            } else if (pointer2 == n) {
                System.arraycopy(nums1, pointer1, result, i, m - pointer1);
                break;
            }

            if (nums1[pointer1] < nums2[pointer2]) {
                result[i] = nums1[pointer1];
                pointer1++;
            } else {
                result[i] = nums2[pointer2];
                pointer2++;
            }
        }

        System.arraycopy(result, 0, nums1, 0, m + n);
    }

    // optimal solution
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (nums1.length == 0 || nums2.length == 0) {
            return;
        }

        int pointer1 = m - 1;
        int pointer2 = n - 1;

        for (int i = m + n - 1; i >= 0; i--) {
            if (pointer2 < 0) {
                return;
            } else if (pointer1 < 0 || nums2[pointer2] >= nums1[pointer1]) {
                nums1[i] = nums2[pointer2];
                pointer2--;
            } else {
                nums1[i] = nums1[pointer1];
                pointer1--;
            }
        }
    }
}
