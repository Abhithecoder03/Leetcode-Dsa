class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                perimeter += 1 if i == 0 or not grid[i - 1][j] else 0
                perimeter += 1 if i == len(grid) - 1 or not grid[i + 1][j] else 0
                perimeter += 1 if j == 0 or not grid[i][j - 1] else 0
                perimeter += 1 if j == len(grid[0]) - 1 or not grid[i][j + 1] else 0
        return perimeter

        