class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def loop_grid(grid, visited):
            '''
            Loop through all items in the grid, keeping track to never count an island twice.
            If current grid item is a zero, just continue to the next.
            If the current grid item is a one, and we haven't visited it before, caculate the size of this island
            '''
            max_area = 0
            good_rows = range(len(grid))
            good_cols = range(len(grid[0]))
            # loop through rows
            for i, row in enumerate(grid):
                # loop through cols
                for j, land in enumerate(row):
                    # check that we haven't already seen this node
                    if (i, j) in visited:
                        continue
                    # if it is part of an island, calculate its area and check against max
                    if land == 1:
                        area = get_island_area(i, j, visited, good_rows, good_cols)
                        max_area = max(max_area, area)
                    else:
                        visited.add((i, j))
            return max_area

        def get_island_area(i, j, visited, good_rows, good_cols):
            '''
            Given i, j the indices of part of an island, DFS from here to find all land areas reachable from this               section, and calculate the size of the island.
            '''
            # initialize starting conditions
            area = 0
            island_stack = [(i, j)]
            visited.add((i,j))
            # Stack for DFS (avoids recursive calls) keep checking for islands while there is a node in stack
            while island_stack:
                # get current indices
                cur = island_stack.pop()
                row, col = cur[0], cur[1]
                # check left, right, up, down indices
                for shift in (-1, 1):
                    for check_row, check_col in ((row+shift, col), (row, col+shift)):
                        # check you are in the bounds of the grid
                        if check_row in good_rows and check_col in good_cols:
                            # check it is part of the island
                            if (check_row, check_col) not in visited and grid[check_row][check_col] == 1:
                                # if its part of island, add it to stack and visited
                                island_stack.append((check_row, check_col))
                                visited.add((check_row, check_col))
                # after each node in the island we check, add 1 to the overall area of the island
                area += 1
            return area

        visited = set()
        return loop_grid(grid, visited)
            
