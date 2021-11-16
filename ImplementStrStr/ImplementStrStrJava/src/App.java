public class App {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        String haystack = "hello", needle = "ll";
        int ans = solution.strStr(haystack, needle);
        System.out.println("ans: " + ans);

        haystack = "aaaa";
        needle = "aba";
        ans = solution.strStr(haystack, needle);
        System.out.println("ans: " + ans);

        haystack = "aaaa";
        needle = "";
        ans = solution.strStr(haystack, needle);
        System.out.println("ans: " + ans);

        haystack = "";
        needle = "aaaa";
        ans = solution.strStr(haystack, needle);
        System.out.println("ans: " + ans);

        haystack = "";
        needle = "";
        ans = solution.strStr(haystack, needle);
        System.out.println("ans: " + ans);
    }
}

class Solution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}
