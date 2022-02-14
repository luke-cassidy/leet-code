package com.leetcode.climbingstairs;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {

    @Test
    public void test_whereNEquals1() {
        assertEquals(1, new Solution().climbStairs(1));
    }

    @Test
    public void test_whereNEquals2() {
        assertEquals(2, new Solution().climbStairs(2));
    }

    @Test
    public void test_whereNEquals3() {
        assertEquals(3, new Solution().climbStairs(3));
    }

    @Test
    public void test_whereNEquals4() {
        assertEquals(5, new Solution().climbStairs(4));
    }

    @Test
    public void test_whereNEquals5() {
        assertEquals(8, new Solution().climbStairs(5));
    }

}
