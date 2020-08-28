import java.util.Arrays;

public class RotateArray {
    public static void main(String[] args) throws Exception {
        int[] nums = new int[] {1, 2, 3, 4, 5, 6, 7, 8};
        Solution solution = new Solution();
        solution.rotate(nums, 0);
        System.out.println("nums: " + Arrays.toString(nums));
    }
}

class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        int lastVal = nums[0];
        int modifier = 0;

        for(int i = 0; i < nums.length; i++) {
            int nextIndex = ((i + 1) * k ) % nums.length + modifier;
            int temp;
            if(nextIndex == modifier) {
                modifier++;
                temp = nums[(nextIndex + 1) % nums.length];
            } else {
                temp  = nums[nextIndex];
            }
            nums[nextIndex] = lastVal;
            lastVal = temp;
        }
    }

}
