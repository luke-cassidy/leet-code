# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if root == None:
            return result

        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result


# initial iterative solution

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if root == None:
            return result

        nodeStack: List[TreeNode] = [root]
        leftStack: List[bool] = [False]
        rightStack: List[bool] = [False]

        while nodeStack:
            currNode: TreeNode = nodeStack[-1]
            if currNode.left != None and not leftStack[-1]:
                leftStack[-1] = True
                nodeStack.append(currNode.left)
                leftStack.append(False)
                rightStack.append(False)
                continue

            if not rightStack[-1]:
                result.append(currNode.val)

            if currNode.right != None and not rightStack[-1]:
                rightStack[-1] = True
                nodeStack.append(currNode.right)
                leftStack.append(False)
                rightStack.append(False)
                continue

            nodeStack.pop()
            leftStack.pop()
            rightStack.pop()

        return result


# proper stacked iterative solution

class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        curr = root
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left

            prev = stack.pop()
            result.append(prev.val)
            curr = prev.right

        return result

# morris traversal


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        curr = root
        while curr != None:
            if curr.left != None:
                subCurr = curr.left
                while subCurr.right != None:
                    subCurr = subCurr.right
                subCurr.right = curr
                temp = curr.left
                curr.left = None
                curr = temp
            else:
                result.append(curr.val)
                curr = curr.right

        return result


# test cases
print("Solution (None) ([]]) {}".format(Solution().inorderTraversal(None)))
print("Solution (1) ([0]]) {}".format(Solution().inorderTraversal(TreeNode())))
print("Solution (2) ([1,0]]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=1)))))
print("Solution (2) ([1,0,2]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=2)))))
print("Solution (3) ([-2,-1,-3,0,2,1,3]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=-1, left=TreeNode(val=-2), right=TreeNode(-3)), right=TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))))))
