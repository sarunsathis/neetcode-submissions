class Solution:

    def findAllLands(self,grid, i,j) :
        if grid[i][j] == "1" :
            grid[i][j] = "0"

        if i > 0 and grid[i-1][j] != "0":
            self.findAllLands(grid,i-1,j)
        if i < len(grid)-1 and grid[i+1][j] != "0" :
            self.findAllLands(grid,i+1,j)
        if j > 0 and grid[i][j-1] != "0" :
            self.findAllLands(grid,i,j-1)
        if j < len(grid[i])-1 and grid[i][j + 1] != "0" :
            self.findAllLands(grid,i,j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        i = j = count = 0
        while i < len(grid) :
            j = 0
            while j < len(grid[i]) :
                if grid[i][j] == "1" :
                    count += 1
                    self.findAllLands(grid,i,j)
                j += 1
            i += 1
        return count
        