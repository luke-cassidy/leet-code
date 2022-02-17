package com.leetcode.validparentheses;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class SolutionTest {

    @Test
    public void test_1CharInvalid() {
        Solution solution = new Solution();
        assertFalse(solution.isValid("("));
        assertFalse(solution.isValid("}"));
        assertFalse(solution.isValid("["));
    }

    @Test
    public void test_2CharValid() {
        Solution solution = new Solution();
        assertTrue(solution.isValid("()"));
        assertTrue(solution.isValid("{}"));
        assertTrue(solution.isValid("[]"));
    }

    @Test
    public void test_invalidSeries() {
        Solution solution = new Solution();
        assertFalse(solution.isValid("(){}["));
        assertFalse(solution.isValid("(){[]"));
        assertFalse(solution.isValid("){}[]"));
    }

    @Test
    public void test_validSeries() {
        Solution solution = new Solution();
        assertTrue(solution.isValid("(){}[]"));
    }

    @Test
    public void test_invalidNested() {
        Solution solution = new Solution();
        assertFalse(solution.isValid("({[)]}"));
        assertFalse(solution.isValid("({[}]})"));
        assertFalse(solution.isValid("({][})"));
    }

    @Test
    public void test_validNested() {
        Solution solution = new Solution();
        assertTrue(solution.isValid("({[]})"));
    }

    @Test
    public void test_stuff() {
        Solution solution = new Solution();
        assertTrue(solution.isValid("()"));
        assertTrue(solution.isValid("(()(()))"));
        assertFalse(solution.isValid("(())())"));
        assertTrue(solution.isValid("({[]})"));
        assertFalse(solution.isValid("({[}])"));
        assertFalse(solution.isValid("({[)]}"));
    }
}
