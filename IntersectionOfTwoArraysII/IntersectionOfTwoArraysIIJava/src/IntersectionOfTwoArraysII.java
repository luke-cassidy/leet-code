import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;

public class IntersectionOfTwoArraysII {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] nums1 = new int[] { 1, 2, 2, 1 };
        int[] nums2 = new int[] { 2, 2 };

        int[] ans = solution.intersect2(nums1, nums2);
        System.out.println("ans: " + Arrays.toString(ans));

        nums1 = new int[] { 4, 9, 5 };
        nums2 = new int[] { 9, 4, 9, 8, 4 };
        ans = solution.intersect2(nums1, nums2);
        System.out.println("ans: " + Arrays.toString(ans));

        nums1 = new int[] { 1, 1, 1, 1 };
        nums2 = new int[] { 2, 2, 2, 2 };
        ans = solution.intersect2(nums1, nums2);
        System.out.println("ans: " + Arrays.toString(ans));

        nums1 = new int[] {};
        nums2 = new int[] { 1, 2, 3, 4 };
        ans = solution.intersect2(nums1, nums2);
        System.out.println("ans: " + Arrays.toString(ans));
    }
}

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> nums1Map = new HashMap<>();
        for (int num : nums1) {
            nums1Map.put(num, nums1Map.containsKey(num) ? nums1Map.get(num) + 1 : 1);
        }

        HashMap<Integer, Integer> intersectMap = new HashMap<>();
        int count = 0;
        for (int num : nums2) {
            if (nums1Map.containsKey(num)) {
                if (intersectMap.containsKey(num)) {
                    if (intersectMap.get(num) < nums1Map.get(num)) {
                        intersectMap.put(num, intersectMap.get(num) + 1);
                        count++;
                    }
                } else {
                    intersectMap.put(num, 1);
                    count++;
                }
            }
        }

        int[] result = new int[count];
        int i = 0;

        for (Entry<Integer, Integer> entry : intersectMap.entrySet()) {
            for (int j = 0; j < entry.getValue(); j++) {
                result[i + j] = entry.getKey();
            }
            i += entry.getValue();
        }

        return result;
    }

    public int[] intersect2(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> nums1Map = new HashMap<>();
        for (int num : nums1) {
            nums1Map.put(num, nums1Map.containsKey(num) ? nums1Map.get(num) + 1 : 1);
        }

        HashMap<Integer, Integer> intersectMap = new HashMap<>();
        int[] result = new int[nums1.length + nums2.length];
        int count = 0;
        for (int num : nums2) {
            if (nums1Map.containsKey(num)) {
                if (intersectMap.containsKey(num)) {
                    if (intersectMap.get(num) < nums1Map.get(num)) {
                        intersectMap.put(num, intersectMap.get(num) + 1);
                        result[count] = num;
                        count++;
                    }
                } else {
                    intersectMap.put(num, 1);
                    result[count] = num;
                    count++;
                }
            }
        }

        return Arrays.copyOfRange(result, 0, count);
    }

}
