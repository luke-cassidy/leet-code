import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 2, 3, 4, 5, 6, 7 };
        new Solution().rotate(nums, 3);
        System.out.println("ans: " + Arrays.toString(nums));
    }

    public void rotate(int[] nums, int k) {
        for (int i = nums.length - 1; i >= 0; i--) {
            int temp = nums[i];
            nums[i] = nums[i - (nums.length - 1 - k) % nums.length];
            nums[i - (nums.length - 1 - k) % nums.length] = temp;
        }
    }
}
