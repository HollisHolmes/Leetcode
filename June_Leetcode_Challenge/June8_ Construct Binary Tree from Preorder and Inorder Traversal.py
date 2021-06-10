# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def tree_from_list(preorder, inorder):
            if not preorder: return None
            # get the root
            root_val = preorder[0]
            root = TreeNode(root_val)

            #split into right and left tree
            index = inorder.index(root_val)

            # construct left and right subtree recursively
            root.left = tree_from_list(preorder[1:index+1], inorder[:index])
            root.right = tree_from_list(preorder[index+1:], inorder[index+1:])

            return root

        return tree_from_list(preorder, inorder)
