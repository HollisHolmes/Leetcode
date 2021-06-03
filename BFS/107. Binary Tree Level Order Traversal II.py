# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        '''
        BFS the tree in O(n) time, yielding an level-order traversal.
        Then in O(n) total time, reverse the ordering of each of the levels.
        '''
        from collections import deque

        if root is None: return []

        q = deque()
        q.append(root)
        levels = []
        while q:
            cur_level = []
            # move through only the number of nodes in the current level
            for _ in range(len(q)):
                cur = q.popleft()
                cur_level.append(cur.val)
                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)
            levels.append(cur_level)

        return levels[-1::-1]
                
