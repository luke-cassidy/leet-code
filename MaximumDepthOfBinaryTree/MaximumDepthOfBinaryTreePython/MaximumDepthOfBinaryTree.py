# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        leftDepth = 1
        rightDepth = 1
        if root.left != None:
            leftDepth = leftDepth + self.maxDepth(root.left)

        if root.right != None:
            rightDepth = rightDepth + self.maxDepth(root.right)

        return max([leftDepth, rightDepth])


print("Solution None: {}".format(Solution.maxDepth(Solution(), None)))
print("Solution Empty: {}".format(Solution.maxDepth(Solution(), TreeNode())))
print("Solution left 1: {}".format(
    Solution.maxDepth(Solution(), TreeNode(left=TreeNode()))))
print("Solution right 1: {}".format(
    Solution.maxDepth(Solution(), TreeNode(right=TreeNode()))))
print("Solution left 1, right 1: {}".format(Solution.maxDepth(
    Solution(), TreeNode(left=TreeNode(), right=TreeNode()))))
print("Solution left 3, right 0: {}".format(Solution.maxDepth(
    Solution(), TreeNode(left=TreeNode(left=TreeNode(left=TreeNode()))))))
print("Solution left 0, right 3: {}".format(Solution.maxDepth(
    Solution(), TreeNode(right=TreeNode(right=TreeNode(right=TreeNode()))))))
print("Solution left 3, right 3: {}".format(Solution.maxDepth(Solution(), TreeNode(left=TreeNode(
    left=TreeNode(left=TreeNode())), right=TreeNode(right=TreeNode(right=TreeNode()))))))
print("Solution left 2, right 4: {}".format(Solution.maxDepth(Solution(), TreeNode(left=TreeNode(
    left=TreeNode()), right=TreeNode(right=TreeNode(right=TreeNode(right=TreeNode())))))))