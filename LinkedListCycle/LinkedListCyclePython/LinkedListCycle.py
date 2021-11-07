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
    def hasCycleHashSet(self, head: ListNode) -> bool:
        instances = set()
        curr = head
        while curr != None:
            if id(curr) not in instances:
                instances.add(id(curr))
                curr = curr.next
            else:
                return True

        return False

    def hasCycle(self, head: ListNode) -> bool:
        slow_curr = head
        fast_curr = head.next if head != None else None

        while fast_curr != None:
            if id(fast_curr) == id(slow_curr):
                return True
            else:
                slow_curr = slow_curr.next
                fast_curr = fast_curr.next.next if fast_curr.next != None else None

        return False


head = None
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, None)
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, None)
head.next = head
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, None))
head.next.next = head
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

pos = ListNode(2, None)
head = ListNode(1, pos)
pos.next = ListNode(3, ListNode(4, pos))
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

pos = ListNode(2, None)
head = ListNode(3, pos)
pos.next = ListNode(0, ListNode(4, pos))
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, None))
head.next.next = head
ans = Solution.hasCycle(Solution(), head)
print("ans: {}".format(ans))
