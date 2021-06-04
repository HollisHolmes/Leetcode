# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        '''
        Could either retrace the path by keeping track of parent pointers then reversing the path list
        or
        Keep track of the path on the fly.
            Key part here is to not pass same path object to both cur.left stack add and cur.right stack
                This will cause them both to point to the same object, so when items get added
                to either list later, it will get added to both
            SO, pass path.copy() to avoid this issue.
        '''
        if not root: return None
        parent = {root: None}
        stack = [(root, targetSum, [])]
        paths = []
        while stack:
            cur, target, path = stack.pop()
            target -= cur.val
            path.append(cur.val)
            if target == 0 and not cur.left and not cur.right:
                paths.append(path)
            if cur.left:
                stack.append((cur.left, target, path.copy()))
            if cur.right:
                stack.append((cur.right, target, path.copy()))
        return paths
                
