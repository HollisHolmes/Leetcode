# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
        DFS the tree since there is a unique path to each leaf, no need to check for cycles.
        '''
        # If you reach None node, return False
        if root is None: return False
        # Check target sum
        target = targetSum - root.val
        # If you are a leaf and the sum matches, you found a match
        if root.left is None and root.right is None and target == 0:
            return True
        # Else, check if there is a match in your right or left children
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
