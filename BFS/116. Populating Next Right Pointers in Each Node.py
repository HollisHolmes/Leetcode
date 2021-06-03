"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        BFS level by level keeping track of a previous and current node
        tree so we do not need to worry about cycles
        '''
        if root is None: return root
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            prev = None
            for _ in range(len(q)):
                cur = q.popleft()
                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)
                if prev is not None:
                    prev.next = cur
                prev = cur
        return root
                
