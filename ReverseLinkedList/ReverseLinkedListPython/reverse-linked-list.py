# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "["  + self.str_recur() + "]"

    def str_recur(self):
        if self.next != None:
            return str(self.val) + ", " + self.next.str_recur()
        else:
            return str(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        currentNode = head
        while currentNode != None:
            result = ListNode(currentNode.val, result)
            if currentNode.next == None:
                break
            currentNode = currentNode.next
        return result

    def reverseList2(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList3(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            newList = self.reverseList3(head.next)
            head.next.next = head
            head.next = None
            return newList



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ans = Solution().reverseList(head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ans = Solution().reverseList2(head)
print("ans: {}".format(ans))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ans = Solution().reverseList3(head)
print("ans: {}".format(ans))