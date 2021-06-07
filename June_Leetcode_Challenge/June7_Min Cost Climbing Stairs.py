class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Dynamic programming where subproblems are which stair you are on and cost incurred to that point.
        Topological sort since we are always moving up the stairs, subproblems only depend on prev stairs.
        Choises are to move up one or two stairs, so we minimize over the cost of those choices.
        Return the cost at the end.

        Can save space by using the same array instead of a seperate one for the DP table.
        '''
        DP = [0 for _ in range(len(cost)+1)]
        for i in range(len(cost)+1):
            if i in (0, 1):
                DP[i] = 0
            else:
                DP[i] = min(DP[i-1]+cost[i-1], DP[i-2]+cost[i-2])
        return DP[-1]
