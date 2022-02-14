package com.leetcode.climbingstairs;

public class Solution {

    private int[] memo;

    // recursive solution
    public int climbStairs1(int n) {
        memo = new int[n];
        return climbStairsRecur(n);
    }

    public int climbStairsRecur(int n) {
        if (memo[n - 1] != 0) {
            return memo[n - 1];
        } else if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }

        int val = climbStairsRecur(n - 1) + climbStairsRecur(n - 2);
        memo[n - 1] = val;
        return val;
    }

    ////////////////

    // iterative solution
    public int climbStairs(int n) {
        int fMinus1 = 1;
        int fMinus2 = 0;
        int val = fMinus1 + fMinus2;
        for(int i = 2; i <= n; i++) {
            fMinus2 = fMinus1;
            fMinus1 = val;
            val = fMinus1 + fMinus2;
        } 
        return val;
    }

}
