from typing import List, Optional

from modules.tree import TreeNode


# inital incorrect solution, due to misinterpreting question
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convertToTree(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None

            root = TreeNode(nums[-1])
            curr = root
            for i in range(len(nums) - 2, -1, -1):
                curr.left = TreeNode(nums[i])
                curr = curr.left

            return root

        if len(nums) == 0:
            return None

        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        root.left = convertToTree(nums[:middle])
        root.right = convertToTree(nums[middle + 1:])

        return root

# recursive solution


class Solution2:
    # apperently slicing takes O(n) time, therefore O(n * log(n)) overall
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return None

        middle = length // 2
        curr = TreeNode(nums[middle])
        if length >= 2:
            curr.left = self.sortedArrayToBST(nums[:middle])
            curr.right = self.sortedArrayToBST(nums[middle + 1:])
        return curr


class Solution:
    # without slicing
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructTree(nums: List[int], lower: int, upper: int) -> Optional[TreeNode]:
            if lower == upper:
                return None

            middle = (lower + upper) // 2
            curr = TreeNode(nums[middle])
            curr.left = constructTree(nums, lower, middle)
            curr.right = constructTree(nums, middle + 1, upper)

            return curr

        return constructTree(nums, 0, len(nums))


print("Solution None -> None: {} ".format(Solution().sortedArrayToBST([])))
print("Solution [0] -> [0]: {} ".format(Solution().sortedArrayToBST([0])))
print(
    "Solution [-1, 0] -> [0, -1, None]: {} ".format(Solution().sortedArrayToBST([-1, 0])))
print(
    "Solution [-1, 0, 1] -> [0, -1, 1]: {} ".format(Solution().sortedArrayToBST([-1, 0, 1])))
print("Solution [-2, -1, 0, 1] -> [0, -1, 1, -2, None]: {} ".format(
    Solution().sortedArrayToBST([-2, -1, 0, 1])))
print("Solution [-2, -1, 0, 1, 2] -> [0, -1, 2, -2, None, 1, None]: {} ".format(
    Solution().sortedArrayToBST([-2, -1, 0, 1, 2])))
