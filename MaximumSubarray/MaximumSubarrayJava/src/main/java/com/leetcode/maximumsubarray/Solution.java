package com.leetcode.maximumsubarray;

public class Solution {
    // initial solution
    public int maxSubArray1(int[] nums) {
        int max = nums[0];
        int current = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (current <= 0) {
                current = nums[i];
            } else {
                current += nums[i];
            }

            if (current > max) {
                max = current;
            }
        }
        return max;
    }

    // resursive solution
    public int maxSubArray(int[] nums) {
        return maxSubArrayRecur(nums, nums.length - 1)[1];
    }

    private int[] maxSubArrayRecur(int[] nums, int i) {
        if (i == 0) {
            // first element is curr subArrayVal, second is maxSubArrayVal so far
            return new int[] { nums[i], nums[i] };
        }

        int[] subArrayState = maxSubArrayRecur(nums, i - 1);
        // update curr subArrayVal
        subArrayState[0] = subArrayState[0] < 0 ? nums[i] : subArrayState[0] + nums[i];
        // update max subArrayVal
        subArrayState[1] = Math.max(subArrayState[1], subArrayState[0]);
        // return subArrayState
        return subArrayState;
    }
}
