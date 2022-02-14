package com.leetcode.besttimetobuyandsellstock;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {

    @Test
    public void test_whereNEquals0() {
        int[] prices = new int[0];
        assertEquals(0, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals1() {
        int[] prices = new int[1];
        assertEquals(0, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals2_withNoProphit() {
        int[] prices = new int[] {2,1};
        assertEquals(0, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals2_withProphit() {
        int[] prices = new int[]{1,2};
        assertEquals(1, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals3_withNoProphit() {
        int[] prices = new int[]{3,2,1};
        assertEquals(0, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals3_withProphit() {
        int[] prices = new int[]{1,2,3};
        assertEquals(2, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals5_with2Prophits_andLatterIsCorrect() {
        int[] prices = new int[]{1,2,3,1,5};
        assertEquals(4, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals5_with2Prophits_andFormerIsCorrect() {
        int[] prices = new int[]{4,3,6,4,5};
        assertEquals(3, new Solution().maxProfit(prices));
    }

    @Test
    public void test_whereNEquals7_withMulitpleProphits_andOverallIsCorrect() {
        int[] prices = new int[]{5,1,4,2,3,2,6};
        assertEquals(5, new Solution().maxProfit(prices));
    }
}
