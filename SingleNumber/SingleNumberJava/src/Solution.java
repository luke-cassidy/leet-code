import java.util.HashSet;

public class Solution {

    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        Integer ans = solution.singleNumber(new int[] { 2, 2, 1 });
        System.out.println("ans: " + ans);
    }

    public int singleNumber(int[] nums) {
        HashSet<Integer> intSet = new HashSet<>();
        for (Integer num : nums) {
            if (intSet.contains(num)) {
                intSet.remove(num);
            } else {
                intSet.add(num);
            }
        }
        return intSet.iterator().next();
    }
}