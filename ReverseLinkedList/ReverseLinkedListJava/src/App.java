public class App {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null)))));
        ListNode ans = solution.reverseList(head);
        System.out.println("ans: " + ans);
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        } else {
            ListNode newNode = reverseList(head.next);
            head.next.next = head;
            head.next = null;
            return newNode;
        }
    } 
}

class ListNode {
    int val;
    ListNode next;

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    @Override
    public String toString() {
        return "[" + toStringRecur() + "]";
    }

    String toStringRecur() {
        if(next != null) {
            return Integer.toString(val) + ", " + next.toStringRecur();
        } else {
            return Integer.toString(val);
        }
    }
}