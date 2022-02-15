package com.leetcode.numberof1bits;

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight1(int n) {
        return Integer.bitCount(n);
    }

    // bit shifting solution
    public int hammingWeight(int n) {
        int count = 0;
        while(n != 0) {
            count = count + (n & 1);
            n >>>= 1;
        }
        return count;
    }
}
