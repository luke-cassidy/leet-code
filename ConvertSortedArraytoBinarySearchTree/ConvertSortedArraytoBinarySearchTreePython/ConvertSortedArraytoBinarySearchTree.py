from typing import List, Optional

from modules.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        middle = len(nums) // 2

        root = TreeNode(nums[middle])

        leftCurr: TreeNode = root
        rightCurr: TreeNode = root

        for i in range(middle - 1):
            leftCurr.left = TreeNode(i)
            rightCurr.left = TreeNode(middle + i)
            leftCurr = leftCurr.left
            rightCurr = rightCurr.left

        return root


print("Solution None -> []: {} ".format(Solution().sortedArrayToBST([])))
print("Solution [0] -> [0]: {} ".format(Solution().sortedArrayToBST([0])))
print("Solution [0, 1, 2] -> [0, 1, 2]: {} ".format(
    Solution().sortedArrayToBST([0, 1, 2])))
