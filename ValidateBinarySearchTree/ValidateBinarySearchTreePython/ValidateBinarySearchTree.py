from math import inf
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution


class Solution1:
    def isValidBST(self, root: Optional[TreeNode], rightParent: Optional[TreeNode] = None, leftParent: Optional[TreeNode] = None) -> bool:
        if root == None:
            return True

        if rightParent != None and root.val >= rightParent.val:
            return False

        if leftParent != None and root.val <= leftParent.val:
            return False

        return self.isValidBST(root.left, root, leftParent) and self.isValidBST(root.right, rightParent, root)


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(currentNode: Optional[TreeNode], upperbound: float, lowerbound: float) -> bool:
            if not currentNode:
                return True

            if currentNode.val <= lowerbound or currentNode.val >= upperbound:
                return False

            return validate(currentNode.left, currentNode.val, lowerbound) and validate(currentNode.right, upperbound, currentNode.val)

        return validate(root, inf, -inf)

# iterative in-order solution


class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack iterative inorder traversal
        def traverse(root: TreeNode) -> List[int]:
            result: List[int] = []
            stack: List[TreeNode] = []
            curr = root
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

            return result

        if not root:
            return True

        # loop through comaring order
        prev: Optional[int] = None
        for curr in traverse(root):
            if prev != None and curr <= prev:
                return False
            prev = curr

        return True

# recursive in-order solution


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive inorder traversal
        def traverse(root: Optional[TreeNode]) -> List[int]:
            result: List[int] = []
            if not root:
                return result

            result += traverse(root.left)
            result.append(root.val)
            result += traverse(root.right)
            return result

        # loop through comaring order
        prev: Optional[int] = None
        for curr in traverse(root):
            if prev != None and curr <= prev:
                return False
            prev = curr

        return True


# test cases
print("Solution (None) (True) {}".format(Solution().isValidBST(None)))
print("Solution (1) (True) {}".format(Solution().isValidBST(TreeNode())))
print("Solution (2) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-1), right=TreeNode(val=1)))))
print("Solution (2) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=0), right=TreeNode(val=0)))))
print("Solution (3) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, left=TreeNode(val=-20), right=TreeNode(-5)), right=TreeNode(val=10)))))
print("Solution (3) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, left=TreeNode(val=-20), right=TreeNode(0)), right=TreeNode(val=10)))))
print("Solution (3) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, left=TreeNode(val=-20, right=TreeNode(val=-15))), right=TreeNode(val=10, right=TreeNode(val=20))))))
print("Solution (3) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, left=TreeNode(val=-20, right=TreeNode(val=-10))), right=TreeNode(val=10, right=TreeNode(val=20))))))
print("Solution (3) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10), right=TreeNode(val=10, right=TreeNode(val=5))))))
print("Solution (3) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, right=TreeNode(val=-5, right=TreeNode(val=-2)))))))
print("Solution (3) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, left=TreeNode(val=-10, right=TreeNode(val=-5, right=TreeNode(val=0)))))))
print("Solution (4) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, right=TreeNode(val=10, right=TreeNode(val=20, right=TreeNode(val=30, left=TreeNode(val=25))))))))
print("Solution (4) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, right=TreeNode(val=10, right=TreeNode(val=20, right=TreeNode(val=30, left=TreeNode(val=20))))))))
print("Solution (4) (True) {}".format(Solution().isValidBST(
    TreeNode(val=0, right=TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=2, left=TreeNode(val=1))))))))
print("Solution (4) (False) {}".format(Solution().isValidBST(
    TreeNode(val=0, right=TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=2, left=TreeNode(val=0))))))))
