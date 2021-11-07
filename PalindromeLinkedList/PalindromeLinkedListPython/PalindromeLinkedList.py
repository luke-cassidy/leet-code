# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "[" + self.str_recur() + "]"

    def str_recur(self):
        if self.next != None:
            return str(self.val) + ", " + self.next.str_recur()
        else:
            return str(self.val)


class Solution:
    def isPalindromeXOR(self, head: ListNode) -> bool:
        # this is incorrect but interesting
        curr, mid, count, agg = head, head, 0, 0

        while curr != None:
            if count % 2 != 0:
                mid = mid.next
            agg ^= curr.val
            count += 1
            curr = curr.next

        return True if agg == 0 or agg ^ mid.val == 0 else False

    def isPalindrome(self, head: ListNode) -> bool:
        curr, mid, prev_mid, count = head, head, None, 0

        # reverse first half of the list
        while curr != None:
            if count % 2 != 0:
                temp = mid.next
                mid.next = prev_mid
                prev_mid = mid
                mid = temp
            count += 1
            curr = curr.next

        # ignore middle val
        if count % 2 != 0:
            mid = mid.next

        # compare both halves
        while mid != None:
            if mid.val != prev_mid.val:
                return False
            else:
                mid = mid.next
                prev_mid = prev_mid.next

        return True

head = None
ans = Solution.isPalindrome(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, None)
ans = Solution.isPalindrome(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, None))
ans = Solution.isPalindrome(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, ListNode(1, None)))
ans = Solution.isPalindrome(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
ans = Solution.isPalindrome(Solution(), head)
print("ans: {}".format(ans))
