# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        if root.val == key:
            if root.right is None:
                return root.left
            if  root.left is None:
                return root.right

            current_node = root.right
            while current_node.left:
                current_node = current_node.left
            root.val = current_node.val
            root.right = self.deleteNode(root.right, current_node.val)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        return root
