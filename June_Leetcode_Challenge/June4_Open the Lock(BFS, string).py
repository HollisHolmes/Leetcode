class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        Trying to find shortest path in an undirected unweighted graph -> BFS
        BFS level by level ignoring deadzones unless the deadzone is the final value.
        '''
        from collections import deque
        q = deque()
        q.append('0000')
        visited = set()
        visited.add('0000')
        deadset = set(deadends)
        moves = 0
        # DFS
        while q:
            # Only move through the number of nodes in this level
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return moves
                # Get edges unless the one you are at is a deadend
                if cur not in deadset:
                    # Can change each number up or down by one
                    for i in range(len(cur)):
                        # Change up
                        new_ind = (int(cur[i]) + 1) % 10
                        new_cur = cur[:i] + str(new_ind) + cur[i+1:]
                        if new_cur not in visited:
                            visited.add(new_cur)
                            q.append(new_cur)
                        # Change down
                        new_ind = (int(cur[i]) - 1) % 10
                        new_cur = cur[:i] + str(new_ind) + cur[i+1:]
                        if new_cur not in visited:
                            visited.add(new_cur)
                            q.append(new_cur)

            # You finished checking all nodes at this level, so now it will take one more move
            moves += 1

        return -1



        
