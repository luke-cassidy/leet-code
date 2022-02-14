package com.leetcode.maximumsubarray;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class SolutionTest {

    @Test
    public void test_whenArrayHasOneValue() {
        Solution solution = new Solution();
        assertEquals(1, solution.maxSubArray(new int[]{1}));
    }

    @Test
    public void test_whenArrayHasTwoPositiveValues() {
        Solution solution = new Solution();
        assertEquals(3, solution.maxSubArray(new int[]{1,2}));
    }

    @Test
    public void test_whenArrayHasTwoNegativeValues() {
        Solution solution = new Solution();
        assertEquals(-1, solution.maxSubArray(new int[]{-1,-2}));
    }

    @Test
    public void test_whenArrayHasOnePositive_andOneNegativeValue() {
        Solution solution = new Solution();
        assertEquals(1, solution.maxSubArray(new int[]{1, -1}));
    }

    @Test
    public void test_whenArrayHasOnePositive_andOneNegativeValue_andNegativeIsFirst() {
        Solution solution = new Solution();
        assertEquals(1, solution.maxSubArray(new int[]{-1, 1}));
    }

    @Test
    public void test_whenArrayHasManyPositive_andManyNegativeValues_andSolutionIsSubArray() {
        Solution solution = new Solution();
        assertEquals(6, solution.maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4}));
    }

    @Test
    public void test_whenArrayHasManyPositive_andManyNegativeValues_andSolutionIsWholeArray() {
        Solution solution = new Solution();
        assertEquals(23, solution.maxSubArray(new int[]{5,4,-1,7,8}));
    }


}
