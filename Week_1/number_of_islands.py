# Number of Islands: Given a 2d grod map of 1's(land) and 0's (water), counts the number of islands.
class Solution:
    # b_first(grid, tup, visited): Adds (row, col) tuples to set of visited islands
    def b_first(self, grid, tup, visited) -> None: 
        invalid_row = tup[0] < 0 or tup[0] > len(grid) - 1
        invalid_col = tup[1] < 0 or tup[1] > len(grid[0]) - 1
        if  not (invalid_row or invalid_col or tup in visited or grid[tup[0]][tup[1]] == "0"):
            visited.add(tup)
            self.b_first(grid, (tup[0] - 1, tup[1]), visited)
            self.b_first(grid, (tup[0] + 1, tup[1]), visited)
            self.b_first(grid, (tup[0], tup[1] - 1), visited)
            self.b_first(grid, (tup[0], tup[1] + 1), visited)
    # numIslands(grid): Finds number of islands (Groups of 1's) in a matrix
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() 
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    tup = (row, col)
                    if not tup in visited:
                        island_count += 1
                    self.b_first(grid,tup, visited)
        return island_count