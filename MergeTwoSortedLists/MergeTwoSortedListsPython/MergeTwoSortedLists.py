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
    def mergeTwoListsIter(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        lists = sorted([l1, l2], key=lambda x: x.val)

        fst_curr, sec_curr, prev = lists[0].next, lists[1], lists[0]
        while fst_curr != None and sec_curr != None:
            if sec_curr.val < fst_curr.val:
                sec_next = sec_curr.next
                prev.next = sec_curr
                prev.next.next = fst_curr
                prev = sec_curr
                sec_curr = sec_next
            else:
                prev = fst_curr
                fst_curr = fst_curr.next

        if fst_curr != None:
            prev.next = fst_curr
        elif sec_curr != None:
            prev.next = sec_curr

        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1 = None
l2 = None
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(1, None)
l2 = None
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = None
l2 = ListNode(1, None)
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(1, None)
l2 = ListNode(1, ListNode(3, ListNode(4)))
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, None)
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(4, None)
l2 = ListNode(1, ListNode(3, ListNode(4)))
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(4, None)
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
ans = Solution().mergeTwoLists(l1, l2)
print("ans: {}".format(ans))
