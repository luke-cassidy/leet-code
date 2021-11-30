from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

# resursive solution


class Solution:
    # essentially dfs
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root: Optional[TreeNode], level: int):
            if not root:
                return

            if level < len(result):
                result[level].append(root.val)
            else:
                result.append([root.val])

            traverse(root.left, level+1)
            traverse(root.right, level+1)  # type: ignore

        result: List[List[int]] = []
        traverse(root, 0)
        return result


print("Solution None -> []: {} ".format(Solution().levelOrder(None)))
print("Solution [0] -> [0]: {} ".format(Solution().levelOrder(TreeNode())))
print("Solution [0, 1, 2] -> [[0],[1, 2]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1), right=TreeNode(2)))))
print("Solution [0, 1, 2, 3, 4, 5, 6] -> [[0], [1, 2], [3, 4, 5, 6]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(5), right=TreeNode(6))))))
print("Solution [0, 1, null, 2, null, 3, null] -> [[0], [1], [2], [3]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1, left=TreeNode(2, left=TreeNode(3)))))))
print("Solution [0, null, 1, null, 2, null, 3] -> [[0], [1], [2], [3]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1, left=TreeNode(2, left=TreeNode(3)))))))
print("Solution [0, 1, null, 2, null, 3, null, 4] -> [[0], [1], [2], [3], [4]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1, left=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))))))
print("Solution [0, null, 1, null, 2, null, 3, null, 4, null] -> [[0], [1], [2], [3], [4]]: {} ".format(
    Solution().levelOrder(TreeNode(right=TreeNode(1, right=TreeNode(2, left=TreeNode(3, left=TreeNode(4))))))))
print("Solution [0, 1, 2, null, 3, 4, null, null, 5, 6, null, 7, 8, 9, 10, 11, null] -> [[0], [1, 2], [3, 4], [5, 6], [7, 8, 9, 10], [11]]: {} ".format(
    Solution().levelOrder(TreeNode(left=TreeNode(1, right=TreeNode(3, right=TreeNode(5, TreeNode(7, left=TreeNode(11)), TreeNode(8)))), right=TreeNode(2, left=TreeNode(4,  left=TreeNode(6, TreeNode(9), TreeNode(10))))))))
