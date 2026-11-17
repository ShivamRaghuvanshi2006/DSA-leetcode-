class Solution:
    def islandPerimeter(self, grid):
        p = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    p += 4
                    if r and grid[r-1][c]: p -= 2
                    if c and grid[r][c-1]: p -= 2
        return p
