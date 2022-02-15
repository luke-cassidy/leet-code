package com.leetcode.numberof1bits;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class SolutionTest {

    @Test
    public void test_whenWeightIsZero() {
        Solution solution = new Solution();
        assertEquals(0, solution.hammingWeight(Integer.parseInt("0", 2)));
    }


    @Test
    public void test_whenWeightIs1() {
        Solution solution = new Solution();
        assertEquals(1, solution.hammingWeight(Integer.parseInt("1", 2)));
    }

    @Test
    public void test_whenWeightIs2() {
        Solution solution = new Solution();
        assertEquals(2, solution.hammingWeight(Integer.parseInt("10001", 2)));
    }

    @Test
    public void test_whenWeightIs3() {
        Solution solution = new Solution();
        assertEquals(3, solution.hammingWeight(Integer.parseInt("10101", 2)));
    }

    @Test
    public void test_whenWeightIs5() {
        Solution solution = new Solution();
        assertEquals(5, solution.hammingWeight(Integer.parseInt("11111", 2)));
    }

    @Test
    public void test_whenWeightIsnNeg2() {
        Solution solution = new Solution();
        assertEquals(31, solution.hammingWeight(-2));
    }
}
