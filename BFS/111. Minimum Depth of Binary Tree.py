# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        BFS keeping track of level, return level when you first find a leaf
        node is a leaf if left and right children are none
        since it is a tree we do not need to keep track of a visited set to defend against cycles
        '''
        if root is None: return 0
        from collections import deque
        q = deque()
        q.append(root)
        level = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                left, right = cur.left, cur.right
                if left is None and right is None:
                    return level
                for child in (left, right):
                    if child is not None:
                        q.append(child)
            level += 1
        
