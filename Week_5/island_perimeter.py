class Solution:
    def perimeter(self, grid, row, col, visited):
        tup = (row, col)
        if tup in visited:
            return
        visited.add(tup)
        if row - 1 < 0 or grid[row - 1][col] == 0:
            self.perm += 1
        if row + 1 > len(grid) - 1 or  grid[row + 1][col] == 0:
            self.perm += 1
        if col - 1 < 0 or grid[row][col - 1] == 0:
            self.perm += 1
        if col + 1 > len(grid[0]) - 1 or grid[row][col + 1] == 0:
            self.perm += 1
        if row - 1 >= 0:
            if grid[row - 1][col] == 1:
                self.perimeter(grid, row - 1, col, visited)
        if col - 1 >= 0:
            if grid[row][col - 1] == 1:
                self.perimeter(grid, row, col - 1, visited)
        if row + 1 < len(grid):
            if grid[row + 1][col] == 1:
                self.perimeter(grid, row + 1, col, visited)
        if col + 1 < len(grid[0]):
            if grid[row][col + 1] == 1:
                self.perimeter(grid, row, col + 1, visited)
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perm = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.perimeter(grid, row, col, set())
                    return self.perm