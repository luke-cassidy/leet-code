import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {

        Solution solution = new Solution();

        char[] s = new char[] { 'h', 'e', 'l', 'l', 'o' };
        solution.reverseString(s);
        System.out.println("s: " + Arrays.toString(s));

        s = new char[] { 'a', 'b', 'c', 'd', 'e', 'f' };
        solution.reverseString(s);
        System.out.println("s: " + Arrays.toString(s));
    }

}

class Solution {
    public void reverseString(char[] s) {
        char temp;
        for (int i = 0; i < s.length / 2; i++) {
            temp = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i - 1] = temp;
        }
    }
}
