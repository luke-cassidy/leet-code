# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.levelOrderTraverse())

    def levelOrderTraverse(self) -> List[Optional[int]]:
        result: List[Optional[int]] = []
        queue: List[Optional[TreeNode]] = [self]

        while queue:
            node = queue.pop()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(node)

        return result
