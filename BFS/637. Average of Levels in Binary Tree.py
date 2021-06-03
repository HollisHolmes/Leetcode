# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        '''
        BFS through tree level by level
        Check the number of nodes in each level and keep a running sum of values in each level
        Add level_sum to an output list
        '''
        from collections import deque
        if root is None: return None
        q = deque()
        q.append(root)
        level_avgs = []

        while q:
            level_sum = 0
            level_count = len(q)
            for _ in range(level_count):
                cur = q.popleft()
                level_sum += cur.val

                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)

            level_avgs.append(level_sum / level_count)
        return level_avgs

        
