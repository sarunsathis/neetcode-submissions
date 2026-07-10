class Solution:

    def islandArea(self,grid,i,j) -> int :
        if grid[i][j] == 1 :
            grid[i][j] = 0
        area = 1
        if i > 0 and grid[i-1][j] != 0:
            area += self.islandArea(grid,i-1,j)
        if i < len(grid)-1 and grid[i+1][j] != 0 :
            area += self.islandArea(grid,i+1,j)
        if j > 0 and grid[i][j-1] != 0 :
            area += self.islandArea(grid,i,j-1)
        if j < len(grid[i])-1 and grid[i][j + 1] != 0 :
            area += self.islandArea(grid,i,j+1)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        i = j = area = 0
        while i < len(grid) :
            j = 0
            while j < len(grid[i]) :
                if grid[i][j] == 1 :
                    area = max(self.islandArea(grid,i,j),area)
                j += 1
            i += 1
        return area