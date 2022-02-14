package com.leetcode.besttimetobuyandsellstock;

public class Solution {

    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }

        int maxProfit = 0;
        int low = Integer.MAX_VALUE;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < low) {
                low = prices[i];
            } else if (prices[i] - low > maxProfit) {
                maxProfit = prices[i] - low;
            }
        }

        return maxProfit;
    }
}
