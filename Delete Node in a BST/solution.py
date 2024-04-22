# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val

            root.right = self.deleteNode(root.right, cur.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
