# Definition for a binary tree node.
from typing import List, Optional, Tuple, Union, cast


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if root == None:
            return result

        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result


# iterative solution

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


# test cases
print("Solution (None) ([]]) {}".format(Solution().inorderTraversal(None)))
print("Solution (1) ([0]]) {}".format(Solution().inorderTraversal(TreeNode())))
print("Solution (2) ([1,0]]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=1)))))
print("Solution (2) ([1,0,2]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=2)))))
print("Solution (3) ([-2,-1,-3,0,2,1,3]) {}".format(Solution().inorderTraversal(
    TreeNode(val=0, left=TreeNode(val=-1, left=TreeNode(val=-2), right=TreeNode(-3)), right=TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))))))
