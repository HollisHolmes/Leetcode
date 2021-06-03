# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        BSF tree level by level, each level add the value of the last node to an output list
        '''
        from collections import deque
        if root is None: return None
        q = deque()
        q.append(root)
        last_list = []
        while q:
            last = None
            for _ in range(len(q)):
                cur = q.popleft()
                last = cur.val
                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)
            if last is not None:
                last_list.append(last)
        return last_list
                
